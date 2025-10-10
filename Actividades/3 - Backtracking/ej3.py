'''
Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique 
(si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, 
está disponible como se describe.

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

def puede_atacar_reina(reina, posicion):
	rx, ry = reina
	x, y = posicion
	if rx == x or ry == y:
		return True
	elif abs(rx - x) == abs(ry - y):
		return True
	return False

def posicion_valida(posiciones, nueva):
	for posicion in posiciones:
		if puede_atacar_reina(posicion, nueva):
			return False
	return True

def ubicar_reinas(n, fila, posiciones):
	if fila == n:
		return posiciones

	for col in range(n):
		if posicion_valida(posiciones, (fila, col)):
			posiciones.append((fila, col))
			r = ubicar_reinas(n, fila + 1, posiciones)
			if r:
				return r
			posiciones.pop()
	return []

def nreinas(n):
	posiciones = []
	return ubicar_reinas(n, 0, posiciones)