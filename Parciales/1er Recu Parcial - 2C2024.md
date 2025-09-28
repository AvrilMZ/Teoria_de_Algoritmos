# PRIMER RECUPERATORIO PARCIAL - 2C2024

## Ejercicio 1
```py
def esta_balanceada(cadena):
	contador = 0
	pila = crear_pila()
	for char in cadena:
		if char == '(':
			pila.apilar(char)
		else:
			if pila.esta_vacia():
				break
			pila.desapilar()
			contador += 1
	return contador * 2
```
Complejidad:
	- Iterar cada caracter de la cadena: O(n), siendo n la cantidad de caracteres.
	- Apilar y desapilar: O(1)
Por lo que la complejidad final es:
	O(n)

El algoritmo implementado es greedy dado a que no se contabliza el par hasta que no se desapile, dando el optimo local de contabilizar los mismos. Es optimo ya que comenzando desde otro lado no se pueden contabilizar mas pares consecutivos y al momento de encontrar el primer ')' que rompa la secuecia de pares se sale.

## Ejercicio 2
OPT[n]
```py

```

## Ejercicio 3
```py
def buscar_elem(arr, elem, inicio, fin):
	if inicio > fin:
		return -1

	medio = (inicio + fin) // 2
	if arr[medio] == elem:
		return medio
	if elem > arr[medio]:
		return buscar_elem(arr, elem, medio + 1, fin)
	return buscar_elem(arr, elem, inicio, medio - 1)

def valores(arr, elemento, k):
	i_elem = buscar_elem(arr, elem, 0, len(arr) - 1)

	res = []
	izquierda = i_elem - 1
	derecha = i_elem

	for _ in range(k):
		if izquierda < 0:
			res.append(arr[derecha])
			derecha += 1
		elif derecha >= n:
			res.append(arr[izquierda])
			izquierda -= 1
		else:
			if abs(arr[izquierda] - elem) <= abs(arr[derecha] - elem):
				res.append(arr[izquierda])
				izquierda -= 1
			else:
				res.append(arr[derecha])
				derecha += 1

	return res
```
Complejidad:
La busqueda del elemento, como se realiza mediante una busqueda binaria que es un problema de divide y conquista, se puede calcular mediante el toerema maestro:
	T(n) = A T(n/B) + O(f(n)) -> A >= 1 y B > 1
donde A es la cantidad de llamadas recursivas, B la cantidad por la que se divide el problema, y f(n) el coste extra de procesamiento.
En este caso quedaria:
	T(n) = 1 T(n/2) + O(1)
que al evaluarlo:
	f(n) == n^(log_B(A))
	O(1) = n^(log_2(1))
Por lo que la complejidad en tiempo resulta:
	O(log(n))
Aunque la busqueda binaria no es lo unico que se realiza, luego se buscan los k elementos mas cercanos, que tiene un costo de O(k).
Finalmente la complejidad en tiempo es:
	O(k) < O(n)

## Ejercicio 4
(SEGUNDO PARCIAL)

## Ejercicio 5
(SEGUNDO PARCIAL)