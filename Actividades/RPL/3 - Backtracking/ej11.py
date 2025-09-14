'''
Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L y un entero n devuelva todos los subconjuntos de L que suman exactamente n.
'''

def sub_conj(lista, combinaciones, posibilidad, num, sum_actual, i_actual):
	if sum_actual == num:
		combinaciones.append(posibilidad.copy())
		return

	for i in range(i_actual, len(lista)):
		if sum_actual + lista[i] <= num:
			posibilidad.append(lista[i])
			sub_conj(lista, combinaciones, posibilidad, num, sum_actual + lista[i], i + 1)
			posibilidad.pop()
	
	return

def sumatorias_n(lista, n):
	if n == 0 or n > sum(lista):
		return []
	elif n == 1:
		if 1 in lista:
			return [1]

	combinaciones = []
	sub_conj(lista, combinaciones, [], n, 0, 0)
	return combinaciones