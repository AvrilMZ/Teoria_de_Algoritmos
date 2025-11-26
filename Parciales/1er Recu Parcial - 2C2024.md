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
**Complejidad**

- Iterar cada caracter de la cadena: $O(n)$, siendo $n$ la cantidad de caracteres.
- Apilar y desapilar: $O(1)$

Por lo que la complejidad final es:
- $O(n)$

El algoritmo implementado es greedy dado a que no se contabliza el par hasta que no se desapile, dando el óptimo local de contabilizar los mismos. Es **óptimo** ya que comenzando desde otro lado no se pueden contabilizar mas pares consecutivos y al momento de encontrar el primer ')' que rompa la secuecia de pares se sale.


## Ejercicio 2
Para este problema tenemos las opciones de:
- Quedarme con la subsecuencia actual (siguiendo contando)
- Quedarme con la subsecuencia anterior

Dado a que hay que detectar pares balanceados y, si hay anidamiento, sumar la mejor solución previa, podemos plantear la siguiente ecuacion de recurrencia:
- $OPT[n] = OPT[n - 1] + 2 + OPT[n - OPT[n - 1] - 2]$

Donde:
- $OPT[n - 1]$ = largo de la subsecuencia balanceada anterior.
- $+ 2$ = nuevo par, '(' y ')'.
- $+ OPT[n - OPT[n - 1] - 2]$ = largo de la subsecuencia balanceada que termina justo antes del '(' que abre el nuevo par (si existe).
	- $n$ = posición actual, donde termina el nuevo par con ')'.
	- $- OPT[n - 1]$ = retrocedo la cantidad de caracteres que ocupa la última subsecuencia balanceada antes de este ')'.
	- $- 1$ = llego a la posición del '(' que abre el nuevo par.
	- $- 1$ = me paro justo antes de ese '(', para sumar la subsecuencia balanceada previa (si existe).

Donde definimos $OPT[n]$ como el largo de la subsecuencia balanceada más larga que termina en la posición $n$. 

```py
def max_sec(secuencia):
	OPT = [0] * (len(secuencia) + 1)
	max_len = 0
	for i in range(1, len(secuencia) + 1):
		if secuencia[i] == ')':
			j = i - OPT[i - 1] - 1
			if j >= 0 and secuencia[j] == '(':
				OPT[i] = OPT[i - 1] + 2
				if j - 1 >= 0:
					OPT[i] += OPT[j - 1]
			max_len = max(max_len, OPT[i])
	return max_len
```
**Complejidad**

Dado a que se recorre la secuencia entera una vez sola:
- $O(n)$, siendo $n$ la cantidad de caracteres de la secuencia.


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
**Complejidad**

La busqueda del elemento, como se realiza mediante una busqueda binaria que es un problema de divide y conquista, se puede calcular mediante el toerema maestro:
- $T(n) = A \cdot T(n/B) + O(f(n)) \rightarrow A \ge 1, B \gt 1$

donde $A$ es la cantidad de llamadas recursivas, $B$ la cantidad por la que se divide el problema, y $f(n)$ el coste extra de procesamiento.

En este caso quedaria:
- $T(n) = 1 \cdot T(n/2) + O(1)$
- $f(n) = n^{log_B(A)}$
- $O(1) = n^{log_2(1)}$

Por lo que la complejidad en tiempo resulta:
- $O(\log(n))$

Aunque la busqueda binaria no es lo unico que se realiza, luego se buscan los k elementos mas cercanos, que tiene un costo de O(k).  
Finalmente la complejidad en tiempo es:
- $O(k) < O(n)$


## Ejercicio 4
(SEGUNDO PARCIAL)


## Ejercicio 5
(SEGUNDO PARCIAL)