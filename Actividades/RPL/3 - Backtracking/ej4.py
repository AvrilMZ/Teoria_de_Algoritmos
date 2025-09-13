'''
Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo.

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

'''
agarro 1 vertice y salteo los adyacentes
por cada vecino del adyacente me fijo si se conecta con algun vertice ya contabilizado 
si se conecta lo descarto y sigo, sino lo agrego
cuando recorri todos vuelvo a probar pero arrancando con el segundo vertice
luego comparo cual de las soluciones es la mayor y la guardo
repito con el que sigue y asi sucesivamente
'''

from grafo import Grafo

def es_vertice_apto(grafo, vertice, i_set):
	for v in i_set:
		for vecino in grafo.adyacentes(v):
			if vecino == vertice:
				return False
	return True

def is_backtracking(grafo, vertices, i_set, indice):
	if len(vertices) == indice:
		return list(i_set)

	vertice = vertices[indice]

	record = []
	if es_vertice_apto(grafo, vertice, i_set):
		i_set.append(vertice)
		agrego = is_backtracking(grafo, vertices, i_set, indice + 1)
		if len(agrego) > len(record):
			record = agrego
		i_set.pop()
		
	salteo = is_backtracking(grafo, vertices, i_set, indice + 1)
	if len(salteo) > len(record):
		record = salteo

	return record
		
def independent_set(grafo):
	vertices = grafo.obtener_vertices()
	i_set = []
	r = is_backtracking(grafo, vertices, i_set, 0)
	if r:
		return r
	return []