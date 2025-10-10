'''
Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar 
cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.

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

def colorear_rec(grafo, vertices, indice_actual, n, visitados):
	if len(visitados) == len(vertices):
		return True
	
	vertice = vertices[indice_actual]

	for color in range(n):
		if all(visitado_color != color for v, visitado_color in visitados if v in grafo.adyacentes(vertice)): # Por cada vertice en visitados, si el vertice es vecino y el color asignado es distinto al actual
			visitados.append((vertice, color))
			if colorear_rec(grafo, vertices, indice_actual + 1, n, visitados):
				return True
			visitados.pop()

	return False

def colorear(grafo, n):
	visitados = []
	vertices = grafo.obtener_vertices()
	return colorear_rec(grafo, vertices, 0, n, visitados)