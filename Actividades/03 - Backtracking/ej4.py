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

def es_vertice_apto(grafo, vertice, i_set):
	for v in i_set:
		for vecino in grafo.adyacentes(v):
			if vecino == vertice:
				return False
	return True
		
def is_bt(grafo, vertices, indice, sol_actual, sol_mejor):
	if indice == len(vertices):
		if sol_mejor is None or len(sol_actual) > len(sol_mejor):
			sol_mejor = sol_actual[:]
		return sol_mejor
	
	v = vertices[indice]
	agrego = []
	if es_vertice_apto(grafo, v, sol_actual):
		sol_actual.append(vertices[indice])
		agrego = is_bt(grafo, vertices, indice + 1, sol_actual, sol_mejor)
		sol_actual.pop()

	salteo = is_bt(grafo, vertices, indice + 1, sol_actual, sol_mejor)

	if len(agrego) > len(salteo):
		return agrego
	return salteo

def independent_set(grafo):
	vertices = grafo.obtener_vertices()
	return is_bt(grafo, vertices, 0, [], None)