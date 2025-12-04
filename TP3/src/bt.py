def calcular_mejor_caso(habilidad_total, habilidad_restante, sumas, orden_sumas):
    """
    Calcula el coeficiente minimo que se obtendria a partir de la solucion parcial,
    recibida mediante `sumas` y `habilidad_restante`, suponiendo que la habilidad de
    los maestros aun no asignados se pudiera fraccionar.

    `orden_sumas` es una lista de los indices de `sumas` en orden de menor a mayor   
    """
    # Obtiene la habilidad del i-esimo grupo con mayor habilidad. Dado que orden_sumas 
    # esta en orden ascendente, hay que invertir el acceso.
    obtener_habilidad_grupo = lambda i: sumas[orden_sumas[len(sumas)-1-i]]
    cantidad_grupos = len(sumas)

    # La habilidad total de los maestros presentes en los grupos como estan en la solucion parcial.
    habilidad_ocupada = habilidad_total - habilidad_restante

    # La habilidad de los grupos que se dejan como estan
    habilidad_ignorada = 0
    coeficiente_ignorado = 0

    mejor_caso = 0 
    for i in range(cantidad_grupos):
        # Buscamos igualar la habilidad de todos los grupos a la del mayor grupo que podamos.
        habilidad_objetivo = obtener_habilidad_grupo(i)

        if i > 0:
            habilidad_ignorada += obtener_habilidad_grupo(i-1)
            coeficiente_ignorado += obtener_habilidad_grupo(i-1)**2

        nueva_habilidad_ocupada = habilidad_ignorada + habilidad_objetivo*(cantidad_grupos - i)
        habilidad_utilizada = nueva_habilidad_ocupada - habilidad_ocupada

        if habilidad_utilizada > habilidad_restante:
            # La habilidad a asignar no alcanza para igualar las habilidades de los grupos 
            # menores al objetivo. Reintentar con un grupo mas chico.
            continue

        # Si tras igualar la mayor cantidad de grupos posibles aun nos queda habilidad
        # a asignar, la distribuiremos equitativamente entre los grupos.
        habilidad_excedente = habilidad_restante - habilidad_utilizada
        habilidad_extra_por_grupo = habilidad_excedente/(cantidad_grupos-i)
        mejor_caso = coeficiente_ignorado + (cantidad_grupos - i)*(habilidad_objetivo + habilidad_extra_por_grupo)**2
        break

    return mejor_caso

def conseguir_grupos(
    maestros,
    grupos_actuales,
    sumas,
    habilidad_total,
    habilidad_restante,
    coef_record,
    coef_parcial,
    i,
) -> tuple[list, int]:
    cant_grupos = len(grupos_actuales)
    if i == len(maestros):
        return [g.copy() for g in grupos_actuales], coef_parcial

    # Ordenar indices de grupos por suma ascendente (llenar primero los mas vacios)
    indices_ordenados = sorted(range(cant_grupos), key=lambda j: sumas[j])
    mejor_caso = calcular_mejor_caso(habilidad_total, habilidad_restante, sumas, indices_ordenados)
    if mejor_caso >= coef_record:
        return None, coef_record

    nom, fuerza = maestros[i]
    mejor_sol = None
    vistos = set() 

    for j in indices_ordenados:
        # Si este grupo tiene la misma suma que el anterior daria el mismo resultado
        if sumas[j] in vistos:
            continue
        vistos.add(sumas[j])

        # Poda 3: Descarto si el coeficiente parcial ya supera el record
        nuevo_parcial = coef_parcial - sumas[j] ** 2 + (sumas[j] + fuerza) ** 2
        if nuevo_parcial >= coef_record:
            continue

        grupos_actuales[j].append(nom)
        sumas[j] += fuerza

        sol, coef = conseguir_grupos(
            maestros,
            grupos_actuales,
            sumas,
            habilidad_total,
            habilidad_restante - fuerza,
            coef_record,
            nuevo_parcial,
            i + 1,
        )
        if sol is not None and coef < coef_record:
            coef_record = coef
            mejor_sol = sol

        grupos_actuales[j].pop()
        sumas[j] -= fuerza

    return mejor_sol, coef_record


def heuristica_greedy(maestros, cant_grupos):
    """Genera una solucion inicial usando heuristica greedy para mejorar la poda"""
    grupos = [[] for _ in range(cant_grupos)]
    sumas = [0 for _ in range(cant_grupos)]

    # Asignar cada maestro al grupo con menor suma actual
    for nom, fuerza in maestros:
        idx_min = min(range(cant_grupos), key=lambda i: sumas[i])
        grupos[idx_min].append(nom)
        sumas[idx_min] += fuerza

    coef = sum(s**2 for s in sumas)
    return grupos, coef, sumas

def grupos_maestros_bt(lista_maestros, cant_grupos) -> tuple[list, int]:
    if cant_grupos <= 0:
        return [], 0
    elif cant_grupos == 1:
        return [[nom for nom, _ in lista_maestros]], sum(
            s**2 for _, s in lista_maestros
        )
    elif cant_grupos >= len(lista_maestros):
        grupos = [[nom] for nom, _ in lista_maestros]
        grupos += [
            [] for _ in range(cant_grupos - len(lista_maestros))
        ]  # Los sobrantes los devuelvo vacios
        return grupos, sum(s * s for _, s in lista_maestros)

    ordenados = sorted(lista_maestros, key=lambda x: x[1], reverse=True)
    grupos_actuales = [[] for _ in range(cant_grupos)]
    sumas = [0 for _ in range(cant_grupos)]
    total = sum(m for _, m in ordenados)

    # Obtener solucion inicial con heuristica greedy para mejorar la poda
    grupos_greedy, coef_greedy, _ = heuristica_greedy(ordenados, cant_grupos)

    grupos, coef = conseguir_grupos(
        ordenados, 
        grupos_actuales, 
        sumas, 
        habilidad_total=total, 
        habilidad_restante=total, 
        coef_record=coef_greedy, 
        coef_parcial=0, 
        i=0
    )

    # Si el backtracking no encuentra nada mejor (todas las ramas fueron podadas),
    # devolver la solucion greedy
    if grupos is None:
        return grupos_greedy, coef_greedy

    return grupos, coef
