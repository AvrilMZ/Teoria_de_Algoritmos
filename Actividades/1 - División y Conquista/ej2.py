'''
Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). Se pide:

a. Una función de orden O(log(⁡n)) que, por división y conquista, encuentre el índice del primer 0, de forma que se pueda reconocer rápidamente en qué modificación del código se dejó de pasar los tests. Si no hay ningún 0 (solo hay unos), debe devolver -1. 
b. Demostrar con el Teorema Maestro que la función es, en efecto, O(log(⁡n)).

Ejemplos:
	[1, 1, 0, 0, 0] → 2
	[0, 0, 0, 0, 0] → 0
	[1, 1, 1, 1, 1] → -1
'''
def buscar_indice(arr, izq, der):
	if izq > der:
		return -1
	
	medio = (izq + der) // 2
	if arr[medio] == 0:
		if medio == 0 or arr[medio - 1] == 1:
			return medio
		else:
			return buscar_indice(arr, izq, medio - 1)
	else:
		return buscar_indice(arr, medio + 1, der)

def indice_primer_cero(arr):
	return buscar_indice(arr, 0, len(arr) - 1)

'''
Teniendo en cuenta el teorema maestro:
	T(n) = A T(n/B) + O(f(n)) -> A >= 0, B > 0
Sabemos que:
	- A = 1
	- B = 2
	- O(f(n)) = O(1)
Por lo que:
	T(n) = 1 T(n/2) + O(1)
	O(1) = n^{log_2(1)}
Resultando en una complejidad:
	O(log(n))
'''