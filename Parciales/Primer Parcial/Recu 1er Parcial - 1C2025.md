# RECUPERATORIO PRIMER PARCIAL - 1C2025

## Ejercicio 1
```py
def buscar_faltante(arr, inicio=0, fin=len(arr)):
	if inicio == 0 and arr[0] != 0:
		return 0
	if len(arr) == 1:
		return arr[0] + 1

	medio = (inicio + fin) // 2
	if arr[medio] != medio: # el indice tiene que ser igual al valor
		return buscar_faltante(arr, inicio, medio)
	return buscar_faltante(arr, medio + 1, fin)
```
**Complejidad**

La complejidad de este algoritmo se puede encontrar mediante el teorema maestro ya que es del tipo divide y conquista. Entonces dado:
- $T(n) = A \cdot T(\frac{n}{B}) + O(f(n)) \rightarrow A \ge 1 y B \gt 1$

donde $A$ es la cantidad de llamadas recursivas, $B$ la cantidad por la que se divide el problema, y $f(n)$ el costo adicional de trabajo realizado. En este algoritmo hay una llamada recursiva, el problema se divide en dos, y todos los trabajos son constantes:
- $T(n) = 1 \cdot T(\frac{n}{2}) + O(1)$

que al realizar el analisis de comparar $f(n)$ con $n^{log_B(A)}$:
- $O(1) = n^{log_2(1)}$

resultan iguales, entonces la complejidad en tiempo es:
- $O(log(n))$


## Ejercicio 2
```py
def matching_maximo(grafo):
	
```


## Ejercicio 3
```py
def es_camino_valido(c_actual, caminos):
	for v in c_actual:
		for camino in caminos:
			if v in camino:
				return False
	return True

def buscar_caminos(grafo, visitados, actual, parcial, caminos):
	if indice + 1 == len(grafo):
		if len(caminos) == 0 or es_camino_valido(parcial, caminos):
			return parcial.copy()
		return None
	
	for vecino in grafo.adyacentes(actual):
		if vecino not in visitados:
			visitados.append(actual)
			parcial.append(vecino)
			resultado = buscar_caminos(grafo, visitados, vecino, parcial, caminos)
			if resultado is not None:
				return resultado
			visitados.pop()
			parcial.pop()

	return None

def eliminar_camino(grafo, camino):
	for v in camino:
		grafo.borrar_vertice(v)
	return grafo

def path_selection(grafo):
	copia = grafo.copy()
	caminos = []
	actual = []
	while actual is not None:
		vertices = copia.obtener_vertices()
		actual = buscar_caminos(copia, [], vertices[0], [vertices[0]], caminos)
		caminos.append(actual)
		copia = eliminar_camino(grafo, actual)
	return caminos
```


## Ejercicio 4
Para este problema, si nos situamos en el momento $i$ del problema pudimos llegar ahi:
- Desde cualquier otra posicion cuya diferencia de distancia con $i$ sea igual o menor a su valor $(i - j)$.

Por lo que:
- $OPT[i] = \min{OPT[i - j] + 1}$

donde $j < i$ y $arr[j] - (i - j) \ge 0$

```py
def crear_opt(arr):
	prev = [-1] * len(arr)
	OPT = [float('inf')] * len(arr)
	OPT[0] = 0
	for i in range(1, len(arr)):
		for j in range(0, i):
			if arr[j] - (i - j) >= 0:
				if OPT[j] + 1 < OPT[i]: # si supera al ultimo OPT[j] que se uso...
					OPT[i] = OPT[j] + 1
					prev[i] = j
	return OPT, prev

def reconstruir_camino(arr):
	OPT, prev = crear_opt(arr)
	camino = []
	pos = len(arr) - 1
	while pos != -1: # porque prev esta inicializada con -1 (indica que no hay anterior)
		camino.append(pos)
		pos = prev[pos]
	camino.reverse()
	return camino
```
**Complejidad**

- Crear el OPT: $O(n^2)$, siendo $n$ la cantidad de elementos del arreglo. Ya que en el peor caso $j$ es igual a $i$ e $i$ es igual a $n$.
- Reconstruir camino: $O(n)$

Por lo tanto resulta en:
- $O(n^2)$