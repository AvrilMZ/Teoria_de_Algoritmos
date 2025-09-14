'''
Dada una matriz de 9x9, implementar un algoritmo por backtracking que llene la matriz con números del 1 al 9, dadas las condiciones del Sudoku (si es posible). 
Las condiciones son:
	(i) Las celdas están dispuestas en 9 subgrupos de 3x3.
	(ii) Cada columna y cada fila no puede repetir número.
	(iii) Cada subgrupo de 3x3 no puede repetir número.

Las posiciones de la matriz con valor 0 se espera que se completen, las posiciones con valores entr 1 y 9 no deben modificarse.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.

Métodos del grafo:
	Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
	agregar_vertice(self, v)
	borrar_vertice(self, v)
	agregar_arista(self, v, w, peso = 1)
		el resultado será v <--> w
	borrar_arista(self, v, w)
	estan_unidos(self, v, w)
	peso_arista(self, v, w)
	obtener_vertices(self)
		Devuelve una lista con todos los vértices del grafo
	vertice_aleatorio(self)
	adyacentes(self, v)
	str
'''

def submatriz(matriz, fila, columna):
	fila_inicio = (fila // 3) * 3
	col_inicio = (columna // 3) * 3

	sub_m = []
	for i in range(3):
		fila_sub = []
		for j in range(3):
			fila_sub.append(matriz[fila_inicio + i][col_inicio + j])
		sub_m.append(fila_sub)
	
	return sub_m

def no_repite_numero(matriz, fila, columna, num):
	for n in range(9):
		if n != columna and matriz[fila][n] == num:
			return False
		if n != fila and matriz[n][columna] == num:
			return False
		
	sub = submatriz(matriz, fila, columna)
	for i in range(3):
		for j in range(3):
			if sub[i][j] == num:
				return False
			
	return True

def sudo_backtracking(matriz, res, fila, col):
	if fila == 9:
		return True
	
	if col == 9:
		return sudo_backtracking(matriz, res, fila + 1, 0)

	if matriz[fila][col] != 0:
		return sudo_backtracking(matriz, res, fila, col + 1)
	else:
		for num in range(1, 10):
			if no_repite_numero(res, fila, col, num):
				res[fila][col] = num
				if sudo_backtracking(matriz, res, fila, col + 1):
					return True
				res[fila][col] = 0
	return False

def resolver_sudoku(matriz):
	res = [row[:] for row in matriz]
	if sudo_backtracking(matriz, res, 0, 0):
		return res
	return None