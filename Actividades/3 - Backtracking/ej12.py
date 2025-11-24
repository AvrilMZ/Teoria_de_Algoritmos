'''
Modificar el algoritmo anterior para que, dada una lista de enteros positivos `L` y un entero `n`, devuelva un subconjunto de `L` que sume exactamente `n`, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de `n`.
'''

def sub_conj(lista, n, i, actual):
	sum_actual, sol_actual = actual
	if i == len(lista) or sum_actual == n:
		return (sum_actual, sol_actual.copy())
	
	num = lista[i]
	agrego = (0, [])
	if sum_actual + num <= n:
		sol_actual.append(num)
		sum_actual += num
		agrego = sub_conj(lista, n, i + 1, (sum_actual, sol_actual))
		sol_actual.pop()
		sum_actual -= num
	
	salteo = sub_conj(lista, n, i + 1, (sum_actual, sol_actual))

	sum_agrego, sol_agrego = agrego
	sum_salteo, sol_salteo = salteo
	if sum_agrego > sum_salteo:
		return (sum_agrego, sol_agrego)
	return (sum_salteo, sol_salteo)

def max_sumatoria_n(lista, n):
	if n <= 0:
		return []

	_, sol = sub_conj(lista, n, 0, (0, []))
	return sol