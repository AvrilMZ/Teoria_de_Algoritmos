# SEGUNDO PARCIAL - 1C2025


## Ejercicio 1
`solapamientos(intervalo)`: Devuelve todos los intervalos que se solapan con el intervalo.  
$C_i$: "Charla $i$"  
$X_i$: "Variable binaria, se da la charla $i$"  

$max(\sum_{i = 0}^{n} X_i)$ -> La función objetivo busca maximizar la cantidad de charlas seleccionadas, sumando todas las variables binarias de aquellas que se pueden dar.

Dado que:  
    $X_i + X_j \le 1$ para toda charla $C_j$ perteneciente a la salida de `solapamientos(intervalo)`. (basicamente si se da la charla $i$ y la $j$ se solapa, la $j$ no se puede dar)


## Ejercicio 2


## Ejercicio 3
Camino Hamiltoniano con inicio y fin: ¿existe un camino Hamiltoniano dentro del grafo que empiece en el vértice de inicio y termine en el vértice de fin?
Camino Hamiltoniano: ¿Existe un camino, tal que dado un grafo $G = (V, E)$, recorra todos los vertices del grafo una sola vez?

Para demostrar que camino Hamiltoniano con inicio y fin es un problema NP-Completo primero debemos demostrar que esta en NP:
```py
def verificador(grafo, camino, inicio, fin):
    if camino[0] != inicio or camino[-1] != fin:
        return False
    vertices = grafo.obtener_vertices()
    if len(vertices) != len(camino):
        return False
    anterior = inicio
    for i in range(1, len(camino)):
        if camino[i] not in vertices:
            return False
        elif not grafo.estan_unidos(anterior, camino[i]):
            return False
    return True
```
El verificador tiene complejidad O(n^2), siendo n la cantidad de vertices en camino. Por lo tanto confirmamos que camino Hamiltoniano con inicio y fin esta en NP.

Dado que Camino Hamiltoniano $\le_p$ Camino Hamiltoniano con inicio y fin podemos plantear en el vertice de fin uno extra que salga del mismo, esto seria para forzar al algoritmo a que finalice en ese lugar.

**Demostración:**  
-> Si existe Camino Hamiltoniano existe Camino Hamiltoniano con inicio y fin:  
    Dado un camino obtenido al ejecutar el algoritmo de camino Hamiltoniano sabemos que existe no puede pasar dos veces por el mismo vertice, es asi que el punto de finalizacion puede resultar en un vertice conectado a otros o simplemente a uno, en caso de que este conectado solo a uno si o si debera ser su punto de finalizacion confirmando la existencia de camino Hamiltoniano con inicio y fin.

-> Si existe Camino Hamiltoniano con inicio y fin existe Camino Hamiltoniano:  
    Dado un camino Hamiltoniano con inicio y fin existe un camino Hamiltoniano ya que ambos buscan un camino sin repetir vertices tal que haya pasado una vez por todos, el vertice de fin no influye en una solucion valida para un camino Hamiltoniano.


## Ejercicio 4
a. Un algoritmo greedy seria elegir el siguiente en base a un coeficiente, este podria conseguirse haciendo $w(v) / (cant. de adyacentes)$ -> incluyendo al actual, siendo v el vecino del vertice actual. Eligiriamos al vecino cuyo coeficiente sea mayor ya que nos garantizaria una mayor ganancia en cuanto a peso obtenido segun la cantidad de adyacentes que "bloquee".

b. Supongamos que u no pertenece al conjunto solucion, si u no pertence entonces existe un vecino v que si pertence con un coeficiente $w(v) / (grado(v) + 1)$ mayor, por lo que nos asegura que u fue considerado al momento de conseguir la solucion como asi tambien todos los vecinos de v. Por lo tanto, todo vertice no contenido en la solucion tiene un adyacente con coeficiente mayor o igual a él.

c. Dado que disponemos de una grilla $nxn$ donde cada celda tiene como máximo 4 adyacentes y como mínimo 2 (según corresponda), en el peor de los casos tendremos a un grupo vertices con pesos muy grandes juntos, con el vertice central con al menos 1 numero mas de peso, donde el vertice incluido en la solucion es el central. Podemos considerar que seria peor cuanto mas cantidad de adyacentes haya, ya que realizando la sumatoria resultariamos en una mayor cantidad de peso perdida, es asi que podemos aproximar un 4-aproximacion, siendo 4 los vecinos con pesos enormes los que se estan "perdiendo" por no estar incluidos, resultando en una perdida de 4 veces el peso del vertice incluido en la solucion.