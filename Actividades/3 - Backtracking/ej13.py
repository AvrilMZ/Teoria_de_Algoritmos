'''
Un Vertex Cover de un Grafo `G` es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.

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

def cubre_todas_aristas(grafo, visitados):
	for vertice in grafo.obtener_vertices():
		for vecino in grafo.adyacentes(vertice):
			if vertice not in visitados and vecino not in visitados:
				return False
	return True

def buscar_min_vc(grafo, vertices, visitados, indice_actual):
	if len(vertices) == indice_actual:
		if cubre_todas_aristas(grafo, visitados):
			return list(visitados)
		return None
	
	vertice = vertices[indice_actual]

	visitados.append(vertice)
	agrego_v = buscar_min_vc(grafo, vertices, visitados, indice_actual + 1)
	visitados.pop()

	salteo_v = buscar_min_vc(grafo, vertices, visitados, indice_actual + 1)

	mejor = None
	if agrego_v is not None and (mejor is None or len(agrego_v) < len(mejor)):
		mejor = agrego_v
	if salteo_v is not None and (mejor is None or len(salteo_v) < len(mejor)):
		mejor = salteo_v
	return mejor
		
def vertex_cover_min(grafo):
	vertices = grafo.obtener_vertices()
	visitados = []
	r = buscar_min_vc(grafo, vertices, visitados, 0)
	if r: 
		return r 
	else: 
		return []