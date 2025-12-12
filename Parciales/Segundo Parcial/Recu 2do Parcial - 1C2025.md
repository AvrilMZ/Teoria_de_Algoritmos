# RECUPERATORIO SEGUNDO PARCIAL - 1C2025


## Ejercicio 1
- $H_i$: "Constante binaria, habitante $i$"
- $R_i$: "Variable binaria, el habitante $i$ es representante"
- $N$: "Constante entera, numero de clubes"
- $M_{PP}$: "Variable entera, cantidad máxima de representantes de un partido politico"

- $H-PP(H_i, PP)$: "Constante binaria, el habitante pertenence al partido politico dado"
- $H-C(H_i, C)$: "Constante binaria, el habitante pertenece al club dado"

$\min(M)$ -> Buscamos minimizar la cantidad de simpatizantes a un mismo partido político

Donde:  
    - $\sum_{i = 0}^{n} H-PP(H_i, PP) * R_i \le M$ -> (para todo $PP$)  
    - $\sum_{i = 0}^{n} H-PP(H_i, PP) * R_i \le N/2$ -> constante * variable (para todo $PP$)  
    - $\sum_{i = 0}^{n} H-C(H_i, C) * R_i = 1$ -> (para todo $C$)  


## Ejercicio 2
Para resolver este problema podes plantear una red de flujo con vertices que respresentan a cada persona y vertices que representan a cada dia. La fuente va a estar conectada a cada persona mediante una arista dirigida de peso 2 (cantidad de dias max que puede cocinar alguien), luego las personas van a estar conectadas a los dias que esten disponibles a cocinar con una arista de peso 1, y finalmente los dias van a estar conectados al sumidero mediante una arista de peso 1 (limitando a que solo una persona pueda cocinar ese dia). Al ejecutar el algoritmo de Ford-Fulkerson obtendermos el flujo maximo, si solo nos centramos en el flujo de las aristas persona->dia aquellas que tengan flujo seran las que fueron asignadas a cocinar ese dia.

```py
from ff import flujo
from grafo import Grafo

# personas = {p1 = [dia1, dia3]} 
# dias = []
def crear_red(personas, dias, fuente, sumidero):
    red = Grafo(True, personas.keys())
    red.agregar_vertice(fuente)
    red.agregar_vertice(sumidero)
    
    for dia in dias:
        red.agregar_vertice(dia)
        red.agregar_arista(dia, sumidero)

    for persona in personas:
        red.agregar_arista(fuente, persona, 2)
        for dia in personas[persona]:
            red.agregar_arista(persona, dia)

    return red

def quien_cocina(personas, dias):
    fuente = "fuente"
    sumidero = "sumidero"
    red = crear_red(personas, dias, fuente, sumidero)
    flujo_max = flujo(red, fuente, sumidero)

    cocineros = {}
    for arista in flujo_max:
        origen, destino:
        if origen in personas.keys() and flujo_max[(origen, destino)]:
            cocineros[destino] = origen # dia i: persona

    if len(cocineros) != len(dias):
        return None
    return cocineros
```

Complejidad:  
- Crear la red: O(n^2), siendo n la cantidad de personas y cenas.
- Flujo maximo: O(n * n^2), siendo V la cantidad de vertices del grafo y E las aristas.
- Encontrar los cocineros: O(n^2)  
Por lo tanto la complejidad final es:  
    O(n^3)

## Ejercicio 3
Feedback Vertex Set: ¿existe un subset de vértices del grafo de tamaño a lo sumo k, tal que si eliminamos dichos vértices del grafo, este queda acíclico?  
Vertex Cover: ¿existe un subset de vertices del grafo de tamaño a lo sumo k, tal que todas las aristas tengan al menos un extremo dentro de la solucion?

Buscamos Vertex Cover $\le_p$ Feedback Vertex Set.  
Primero debemos ver si FVS se encuentra en NP:
```py
def tiene_ciclo(grafo):
    visitado = set()
    for v in grafo.obtener_vertices():
        if v not in visitado:
            if dfs_ciclo_no_dirigido(grafo, v, visitado, None):
                return True
    return False

def dfs_ciclo_no_dirigido(grafo, v, visitado, padre):
    visitado.add(v)
    for u in grafo.adyacentes(v):
        if u not in visitado:
            if dfs_ciclo_no_dirigido(grafo, u, visitado, v):
                return True
        elif u != padre: # Encontramos un ciclo
            return True
    return False

def verificador(grafo, subset, k):
    if len(subset) < k:
        return False
    vertices = grafo.obtener_vertices()
    for v in subset:
        if v not in vertices:
            return False
    grafo_reducido = grafo.copy()
    for v in grafo_reducido:
        if v in subset:
            grafo_reducido.borrar_vertice(v)
    return tiene_ciclo(grafo_reducido)
```
Dado que el verificador tiene complejidad O(v^2), siendo v los vertices del grafo reducido. Es asi que confirmamos que FVS se encuentra en NP.

...

-> Si existe Vertex Cover existe FVS:

-> Si existe FVS existe Vertex Cover:



## Ejercicio 4
