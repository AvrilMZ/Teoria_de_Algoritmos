'''
Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez. Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado.

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

from grafo import Grafo

def ch_dfs(grafo, cam_ham, vertice):
	cam_ham.append(vertice)

	if len(cam_ham) == len(grafo.obtener_vertices()):
		return list(cam_ham)

	for vecino in grafo.adyacentes(vertice):
		if vecino not in cam_ham:
			if ch_dfs(grafo, cam_ham, vecino):
				return True
	
	cam_ham.pop()
	return False

def camino_hamiltoniano(grafo):
	cam_ham = []
	for vertice in grafo.obtener_vertices():
		if ch_dfs(grafo, cam_ham, vertice):
			return cam_ham
	return None