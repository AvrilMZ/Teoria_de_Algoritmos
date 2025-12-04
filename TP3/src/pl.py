from typing import List, Dict, Tuple, Optional
import time
import pulp


def grupos_maestros_pl(
    values: List[float],
    k: int,
    time_limit: Optional[float] = None,
    verbose: bool = False,
) -> Tuple[float, List[List[int]]]:
    """
    Formulación MILP exacta (Modelo A) para minimizar sum_{i=1..k} (sum_{j in S_i} values[j])^2
    usando variables binarias z_{i,j} (asignación de elemento j al grupo i) y variables continuas
    u_{i,j,l} para representar z_{i,j} * z_{i,l} (solo j < l). El término sum_j values[j]^2 es constante
    y se omite del objetivo; el objetivo de la MILP es minimizar
        sum_{i=1..k} sum_{1<=j<l<=n} 2 * values[j] * values[l] * u_{i,j,l}

    Parámetros:
      - values: lista de valores (positivos)
      - k: número de grupos
      - time_limit: límite de tiempo (segundos) para el solver (opcional)
      - verbose: si True muestra mensajes del solver

    Devuelve (sum_squares, groups) donde sum_squares es el valor exacto de la suma de cuadrados
    calculado en Python a partir de la partición encontrada, y groups es una lista de k listas con
    los índices originales de los elementos asignados a cada grupo.
    """
    n = len(values)
    if k <= 0:
        raise ValueError("k debe ser >= 1")
    if n == 0:
        return 0.0, [[] for _ in range(k)]

    prob = pulp.LpProblem("Tribu_Del_Agua", pulp.LpMinimize)

    # variables binarias z_{i,j}
    z: Dict[Tuple[int, int], pulp.LpVariable] = {}
    for i in range(k):
        for j in range(n):
            z[(i, j)] = pulp.LpVariable(f"z_{i}_{j}", cat="Binary")

    # variables continuas u_{i,j,l} para j < l
    u: Dict[Tuple[int, int, int], pulp.LpVariable] = {}
    for i in range(k):
        for j in range(n):
            for l in range(j + 1, n):
                u[(i, j, l)] = pulp.LpVariable(
                    f"u_{i}_{j}_{l}", lowBound=0, upBound=1, cat="Continuous"
                )

    # (Opcional) variables S_i para reporte
    S: Dict[int, pulp.LpVariable] = {
        i: pulp.LpVariable(f"S_{i}", lowBound=0, cat="Continuous") for i in range(k)
    }

    # Objetivo: sum_i sum_{j<l} 2 * values[j] * values[l] * u_{i,j,l}
    obj_terms = []
    for i in range(k):
        for j in range(n):
            for l in range(j + 1, n):
                coef = 2.0 * values[j] * values[l]
                obj_terms.append(coef * u[(i, j, l)])
    prob += pulp.lpSum(obj_terms)

    # Restricción: cada elemento asignado a exactamente un grupo
    for j in range(n):
        prob += pulp.lpSum(z[(i, j)] for i in range(k)) == 1, f"assign_item_{j}"

    # Definición S_i = sum_j values[j] * z_{i,j}
    for i in range(k):
        prob += (
            S[i] == pulp.lpSum(values[j] * z[(i, j)] for j in range(n)),
            f"define_S_{i}",
        )

    # Linearización u_{i,j,l} = z_{i,j} * z_{i,l}  (j < l)
    for i in range(k):
        for j in range(n):
            for l in range(j + 1, n):
                zp = z[(i, j)]
                zq = z[(i, l)]
                upq = u[(i, j, l)]
                prob += upq <= zp, f"lin1_u_{i}_{j}_{l}"
                prob += upq <= zq, f"lin2_u_{i}_{j}_{l}"
                prob += upq >= zp + zq - 1, f"lin3_u_{i}_{j}_{l}"

    # prob += z[(0, 0)] == 1

    # Seleccionar solver CBC con time limit si se proporciona
    solver = pulp.PULP_CBC_CMD(msg=1 if verbose else 0, timeLimit=time_limit)

    start = time.perf_counter()
    prob.solve(solver)
    elapsed = time.perf_counter() - start

    # Reconstruir grupos según z
    groups: List[List[int]] = [[] for _ in range(k)]
    unassigned = []
    for j in range(n):
        assigned = False
        for i in range(k):
            val = pulp.value(z[(i, j)])
            if val is not None and val > 0.5:
                groups[i].append(j)
                assigned = True
                break
        if not assigned:
            unassigned.append(j)

    # Calcular suma de cuadrados real en Python
    sum_squares = 0.0
    for g in groups:
        s = sum(values[j] for j in g)
        sum_squares += s * s

    # ordenar índices dentro de cada grupo
    for g in groups:
        g.sort()

    # Información opcional
    if verbose:
        obj_val = pulp.value(prob.objective)
        try:
            mip_status = pulp.LpStatus[prob.status]
        except Exception:
            mip_status = str(prob.status)
        print(
            f"Solver status: {mip_status}, MILP objective (without const): {obj_val}, time={elapsed:.3f}s"
        )

    return sum_squares, groups, unassigned


def grupos_maestros_pl_wrapper(
    maestros: List[Tuple[str, float]], k: int
) -> Tuple[List[List[str]], float]:
    """
    Wrapper para que grupos_maestros_pl tenga la misma firma que bt y aprox.

    Parámetros:
      - maestros: lista de tuplas (nombre, fuerza)
      - k: número de grupos

    Devuelve (grupos, coeficiente) donde:
      - grupos: lista de k listas con nombres de maestros
      - coeficiente: suma de cuadrados de las fuerzas por grupo
    """
    # Extraer solo las fuerzas
    fuerzas = [f for _, f in maestros]

    # Llamar a la función original con tiempo límite de 5 minutos
    coeficiente, grupos_indices, sin_asignar = grupos_maestros_pl(fuerzas, k, time_limit=None)
    if len(sin_asignar) > 0:
        raise TimeoutError()


    # Convertir índices a nombres
    grupos = [[maestros[idx][0] for idx in grupo] for grupo in grupos_indices]

    return grupos, coeficiente
