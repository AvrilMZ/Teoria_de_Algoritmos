'''
Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver todas las tiradas posibles de n dados cuya suma es s.

Por ejemplo, con n = 2 y s = 7, debe devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. 

¿De qué complejidad es el algoritmo en tiempo? ¿Y en espacio?
'''

def sum_backtracking(combinaciones, posibilidad, cant_dados, s_total, s_actual):
	if len(posibilidad) == cant_dados and s_actual == s_total:
		combinaciones.append(posibilidad.copy()) # O(n) -> n = cant. elementos de posibilidad = cant. dados
		return
	
	cant_faltan = cant_dados - len(posibilidad)
	if s_actual + (cant_faltan * 1) > s_total or s_actual + (cant_faltan * 6) < s_total:
		return

	for num in range(1, 7): # O(m) -> m = cant. de numeros en un dado
		if len(posibilidad) < cant_dados and s_actual + num <= s_total:
			posibilidad.append(num)
			sum_backtracking(combinaciones, posibilidad, cant_dados, s_total, s_actual + num) # O(m ** n) -> n = cant. de dados
			posibilidad.pop()

	return

def sumatoria_dados(n, s):
	if n == 1 and 1 <= s <= 6:
		return [[s]]
	combinaciones = []
	sum_backtracking(combinaciones, [], n, s, 0)
	return combinaciones

'''
Complejidad:
	- En tiempo: O((m ** n) * n) -> m ** n combinaciones probadas * n elementos copiados
	- En espacio: O(n) + O((m ** n) * n) -> n stackframes generados y (m ** n) * n combinaciones guardadas en el peor de los casos.
'''