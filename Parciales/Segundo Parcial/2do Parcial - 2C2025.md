# SEGUNDO PARCIAL - 2C2025

## EJERCICIO 1
$A_i$: "Constante entera, costo del mes i en Atenas"  
$R_i$: "Constante entera, costo del mes i en Roma"  
$C$: "Costo fijo de mudanza"  
$X_i$: "Variable binaria que indique si trabajó o no en Roma el mes i"  
$Y_i$: "Variable binaria que indique si trabajó o no en Atenas el mes i"  
$MAR_i$: "Variable binaria que indica si hubo una mudanza de Atenas a Roma"  
$MRA_i$: "Variable binaria que indica si hubo una mudanza de Roma a Atenas"  

$\min{\sum_{i = 1}^{n} A[i] \cdot X_i + \sum_{i = 1}^{n} R[i] \cdot Y_i + \sum_{i = 1}^{n} C \cdot (MAR_i + MRA_i)}$

ó

$\min{(\sum_{i = 1}^{n} A[i] \cdot X_i + (C \cdot {MRA}_i)) + (\sum_{i = 1}^{n} R[i] \cdot Y_i + (C \cdot {MAR}_i))}$

Donde:
- $X_i + Y_i = 1$, para todo i perteneciente a los meses
- ${MAR}_i \ge X_i - Y_{i-1}$
- ${MRA}_i \ge Y_i - X_{i-1}$ 

## EJERCICIO 2
```py
def crear_grafo(pases, S, T):
    jugadas = Grafo(True, list(pases.keys()))
    jugadas.agregar_vertice(T)
    
	for jugador in pases:
        if jugador is not S:
            nuevo_vertice = jugador + "_copia"
            jugadas.agregar_vertice(nuevo_vertice)
            jugador.agregar_arista(jugador, nuevo_vertice, 1)
            for pase in pases[jugador]:
                jugadas.agregar_arista(nuevo_vertice, pase, float("inf"))

    return jugadas

def bfs_jugadas(jugadas, red_residual, flujo_max, sumidero):
    corte = []

    cola = deque()
    cola.append(sumidero)
    while cola:
        v = cola.popleft()
        for w in red_residual.adyacentes(v):
            w.append(cola)
            if jugadas.peso_arista(v, w) - flujo_max[(v, w)] == 0: # ¿Tiene alcance?
                corte.append(w)

    return corte

def marcar_jugadores(pases):
    arquero = "arquero"
    arco = "arco"
    jugadas = crear_grafo(pases, arquero, arco)
    f, red = flujo(jugadas, arquero, arco)
    return bfs_jugadas(jugadas, red, f, arco)
```

Complejidad:
- Crear grafo: $O(n^2)$, siendo $n$ la cantidad de jugadores
- $O(V * E)$ = $O(n^3)$ -> Por aristas singulares
- Buscar el corte minimo: $O(V + E)$ = $O(n^2)$

Por lo tanto la complejidad resulta en $O(n^3)$

## EJERCICIO 3
Para verficar si Feedback Edge Set (FES) es un problema NP-Completo primero debemos verificar si se encuentra en NP.
El problema está en NP si tiene un verificador eficiente en tiempo polinomia

```py
def verificador(grafo, k, solucion):
    if len(solucion) > k:
        return False

    copia = grafo.copy()
    for v, w in solucion:
        if not grafo.estan_unidos(v, w):
            return False
        copia.eliminar_arista(v, w)
    
        g_entrada = {}
        
    conjunto = []
    
    for v in grafo:
        g_entrada[v] = 0

    for v in grafo:
        for w in grafo.adyacentes(v):
            g_entrada[w] += 1

    q = deque()
    for v in grafo:
        if g_entrada[v] == 0:
            q.append(v)
    while q:
        v = q.popleft()
        conjunto.append(v)
        for w in grafo.adyacentes(v):
            g_entrada[w] -= 1
            if g_entrada[w] == 0:
                q.append(w)

    return len(conjunto) == len(grafo): # Si hay ciclo la longitud del conjunto != a la del grafo -> devuelve false     
```
Dado que se puede realizar un verificador en tiempo polinominal, $O(V + E)$ con V = cantidad de vértices y E = cantidad de aristas, podemos confirmar que es parte de NP.

$Vertex\ Cover \le_P FES$



-> Si hay Vertex Cover hay FES:


<- Si hay FES hay Vertex Cover:


## EJERCICIO 4
Resulta en una n-aproximación.