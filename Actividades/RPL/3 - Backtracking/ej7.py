'''
Implementar un algoritmo de backtracking que, dado una pieza de caballo en un tablero de ajedrez de n x n, 
determine si existen los movimientos a realizar para que el caballo logre pasar por todos los casilleros del tablero una única vez.
Recordar que el caballo mueve en forma de L (dos casilleros en una dirección, y un casillero en forma perpendicular).

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

def mov_caballo(caballo, n):
	fil, col = caballo
	nueva_pos = []
	if fil + 2 <= n - 1 and col - 1 >= 0:
		nueva_pos.append((fil + 2, col - 1))
	elif fil - 2 >= 0 and col - 1 >= 0:
		nueva_pos.append((fil - 2, col - 1))
	elif fil + 2 <= n - 1 and col + 1 <= n - 1:
		nueva_pos.append((fil + 2, col + 1))
	elif fil - 2 >= 0 and col + 1 <= n - 1:
		nueva_pos.append((fil + 2, col - 1))
	elif fil + 1 <= n - 1 and col + 2 <= n - 1:
		nueva_pos.append((fil + 1, col + 2))
	elif fil - 1 >= 0 and col + 2 <= n - 1:
		nueva_pos.append((fil - 1, col + 2))
	elif fil + 1 <= n - 1 and col - 2 >= 0:
		nueva_pos.append((fil + 1, col - 2))
	elif fil - 1 >= 0 and col - 2 >= 0:
		nueva_pos.append((fil - 1, col - 2))

	return nueva_pos
	
def recorrer_todo(visitados, caballo, n):
	if len(visitados) == (n * n):
		return True
	
	nueva_pos = mov_caballo(caballo, n)
	for pos in nueva_pos:
		if pos not in visitados:
			visitados.append(pos)
			if recorrer_todo(visitados, pos, n):
				return True
			visitados.pop()

	return False

def knight_tour(n):
	visitados = [(0, 0)]
	caballo = (0, 0)
	return recorrer_todo(visitados, caballo, n)