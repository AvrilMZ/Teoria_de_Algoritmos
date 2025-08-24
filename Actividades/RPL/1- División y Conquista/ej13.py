'''
Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista. 
Indicar y justificar la complejidad del algoritmo. 

Ejemplos:
	[5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
	[5, 3, -5, 4, -1] ->  [5, 3]
	[5, -4, 2, 4, -1] -> [5, -4, 2, 4]
	[5, -4, 2, 4] -> [5, -4, 2, 4]
	[-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def max_ambos(arr, inicio, mitad, fin):
	suma = 0
	mejor_izq = float("-inf")
	idx_izq = mitad
	for i in range(mitad, inicio - 1, -1):
		suma += arr[i]
		if suma > mejor_izq:
			mejor_izq = suma
			idx_izq = i

	suma = 0
	mejor_der = float("-inf")
	idx_der = mitad + 1
	for i in range(mitad + 1, fin + 1):
		suma += arr[i]
		if suma > mejor_der:
			mejor_der = suma
			idx_der = i

	return mejor_izq + mejor_der, idx_izq, idx_der

def max_subarray_rec(arr, inicio, fin):
	if inicio == fin:
		return arr[inicio], inicio, fin
	
	mitad = (inicio + fin) // 2

	max_izq, start_izq, end_izq = max_subarray_rec(arr, inicio, mitad)
	max_der, start_der, end_der = max_subarray_rec(arr, mitad + 1, fin)
	max_cruz, start_cruz, end_cruz = max_ambos(arr, inicio, mitad, fin)

	if max_izq >= max_der and max_izq >= max_cruz:
		return max_izq, start_izq, end_izq
	elif max_der >= max_izq and max_der >= max_cruz:
		return max_der, start_der, end_der
	else:
		return max_cruz, start_cruz, end_cruz


def max_subarray(arr):
	suma, inicio, fin = max_subarray_rec(arr, 0, len(arr) - 1)
	return arr[inicio:fin + 1]

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=2T(n/2)+O(n) -> A>=1 y B>1
	O(n) == n^(log_2(2))
Por lo tanto la complejidad resulta en:
	O(n*log(n))
'''