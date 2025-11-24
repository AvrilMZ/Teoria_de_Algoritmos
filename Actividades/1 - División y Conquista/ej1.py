'''
Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos y casi ordenado (todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento fuera de lugar. Indicar y justificar la complejidad.
'''

def buscar_elemento_desordenado(arr, ini, fin):
	if ini >= fin:
		return None
	
	medio = (ini + fin) // 2

	if arr[medio] > arr[medio + 1]:
		if medio - 1 >= 0 and arr[medio + 1] < arr[medio - 1]:
			return arr[medio + 1]
		return arr[medio]
	
	izq = buscar_elemento_desordenado(arr, ini, medio)
	if izq:
		return izq
	return buscar_elemento_desordenado(arr, medio + 1, fin)

def elemento_desordenado(arr):
	return buscar_elemento_desordenado(arr, 0, len(arr) - 1)

'''
Por el teorema maestro:
	T(n) = AT(n/B) + O(f(n))
Entonces:
	T(n) = 2T(n/2) + O(1) -> A >= 1 y B > 1
	O(1) == n^(log_2(2))
Por lo tanto la complejidad es:
	O(n)
'''