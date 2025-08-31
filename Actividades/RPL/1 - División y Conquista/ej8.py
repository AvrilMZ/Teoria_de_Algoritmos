'''
Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. 
El arreglo A está completamente ordenado de menor a mayor. 
El arreglo B se encuentra desordenado. 
Indicar, por división y conquista, la cantidad de inversioes necesarias al arreglo B para que quede ordenado de menor a mayor, con un orden de complejidad mejor que O(n^2). 
Justificar la complejidad del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "en tiempo mejor que O(n^2)". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

def merge_count(izq, der):
	resultado = []
	i = j = 0
	inv_count = 0

	while i < len(izq) and j < len(der):
		if izq[i] <= der[j]:
			resultado.append(izq[i])
			i += 1
		else:
			resultado.append(der[j])
			j += 1
			inv_count += len(izq) - i

	resultado.extend(izq[i:])
	resultado.extend(der[j:])

	return resultado, inv_count

def merge_sort_count(arr):
	if len(arr) <= 1:
		return arr, 0

	medio = len(arr) // 2

	izq, inv_izq = merge_sort_count(arr[:medio])
	der, inv_der = merge_sort_count(arr[medio:])

	merged, inv_merge = merge_count(izq, der)
	total_inv = inv_izq + inv_der + inv_merge

	return merged, total_inv

def contar_inversiones(A, B):
	ordenados, inv = merge_sort_count(B)
	return inv

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=2T(n/2)+O(n) -> A>=1 y B>1
	O(n) == n^(log_2(2))
Por lo tanto la complejidad resulta en:
	O(n*log(n))
Al igual que al algoritmo tradicional de merge sort.
'''