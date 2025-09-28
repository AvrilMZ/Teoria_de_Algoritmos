# RECUPERATORIO PRIMER PARCIAL - 1C2025

## Ejercicio 1
```py
def buscar_minimo(arr, inicio, fin):
	if len(arr) == 1 and arr[inicio] != 0:
		return inicio - 1
	elif len(arr) == 1 and arr[inicio] == 0:
		return None
	
	medio = (inicio + fin) // 2
	if (len(arr[medio:]) - 1) < medio:
		return buscar_minimo(arr[:medio], inicio, medio)
	return buscar_minimo(arr[medio:], medio, fin)

def minimo_excluido(arr):
	if len(arr) == 1 and arr[0] != 0:
		return arr[0] - 1
	return buscar_minimo(arr, 0, len(arr) - 1, None)
```

La complejidad de este algoritmo se puede encontrar mediante el teorema maestro ya que es del tipo divide y conquista. Entonces dado:
	T(n) = A T(n/B) + O(f(n)) -> A >= 1 y B > 1
donde A es la cantidad de llamadas recursivas, B la cantidad por la que se divide el problema, y f(n) el costo adicional de trabajo realizado. En este algoritmo hay una llamada recursiva, el problema se divide en dos, y todos los trabajos son constantes:
	T(n) = 1 T(n/2) + O(1)
que al realizar el analisis de comparar f(n) con n^(log_B(A)):
	O(1) = n^(log_2(1))
resultan iguales, entonces la complejidad en tiempo es:
	O(log(n))

## Ejercicio 2
```py
def matching_maximo(grafo):
	if len(grafo) == 0:
		return []
	vertices = grafo.obtener_vertices()
	return buscar_matching(grafo, vertices, 0, [])

```

## Ejercicio 3
```py
def path_selection(grafo, caminos)
```

## Ejercicio 4
Para este problema podemos plantear:
	OPT[n] = 1 + min(OPT[m]) -> n + 1 <= m <= len(arr) - 1