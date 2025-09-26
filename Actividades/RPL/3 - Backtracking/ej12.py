'''
Modificar el algoritmo anterior para que, dada una lista de enteros positivos L y un entero n, 
devuelva un subconjunto de L que sume exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n.
'''

def sub_conj(lista, sub, sum_actual, record, num, i_actual):
	if sum(record) < sum_actual <= num:
		record.clear()
		record.extend(sub)
	if sum_actual == num or i_actual == len(lista):
		return
		
	for i in range(i_actual, len(lista)):
		if sum_actual + lista[i] <= num:
			sub.append(lista[i])
			sub_conj(lista, sub, sum_actual + lista[i], record,  num, i + 1)
			sub.pop()

	return
	
def max_sumatoria_n(lista, n):
	if n == 0 or n > sum(lista):
		return []
	elif n == 1:
		if 1 in lista:
			return [1]

	record = []
	sub_conj(lista, [], 0, record, n, 0)
	return record

# CORREGIR