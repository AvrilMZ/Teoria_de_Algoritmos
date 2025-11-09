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
        if origen in personas.keys() and flujo_max[origen]:
            cocineros[destino] = origen # dia i: persona

    if len(cocineros) != len(dias):
        return None
    return cocineros
```

Complejidad:  
- Crear la red: O(n * m), siendo n la cantidad de personas y m la cantidad de dias que tenia cada una asignada.
- Flujo maximo: O(V * E), siendo V la cantidad de vertices del grafo y E las aristas.
- Encontrar los cocineros: O(E)  
Por lo tanto la complejidad final es:  
    O(n * m)

## Ejercicio 3


## Ejercicio 4
