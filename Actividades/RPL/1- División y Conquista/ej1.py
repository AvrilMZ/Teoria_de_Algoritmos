'''
Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos y casi ordenado 
(todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento fuera de lugar. Indicar y justificar la complejidad.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista". Por las características de la herramienta,
no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

def buscar_elemento_desordenado(arr, izq, der):
	if izq == der:
		return arr[izq]

	medio = (izq + der) // 2
	if medio > 0 and arr[medio] < arr[medio - 1]:
		return arr[medio]
	elif medio < len(arr) - 1 and arr[medio] > arr[medio + 1]:
		return arr[medio]
	
	if arr[medio] >= arr[izq]:
		return buscar_elemento_desordenado(arr, medio + 1, der)
	else:
		return buscar_elemento_desordenado(arr, izq, medio - 1)

def elemento_desordenado(arr):
	return buscar_elemento_desordenado(arr, 0, len(arr) - 1)

'''
Por el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=1T(n/2)+O(1) -> A>=1 y B>1
	O(1) == n^(log_2(1))
Por lo tanto la complejidad es:
	O(log(n))
'''