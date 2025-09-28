'''
Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

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

def son_iso(grafo, parcial, nuevo):
	for v in parcial:
		if grafo.estan_unidos(v, nuevo):
			return True
	return False

def detectar_iso(g1, v1, v2, parcial, indice):
	if indice == min(len(v1), len(v2)) and len(parcial) != 0:
		return True
	
	vertice = v2[indice]
	if son_iso(g1, parcial, vertice): # tengo que meter un for antes
		parcial.append(vertice)
		if detectar_iso(g1, v1, v2, parcial, indice + 1):
			return True
		parcial.pop()
	
	if detectar_iso(g1, v1, v2, parcial, indice + 1):
		return True
	
	return False

def hay_isomorfismo(g1, g2):
	ver1 = g1.obtener_vertices()
	ver2 = g2.obtener_vertices()

	return detectar_iso(g1, ver1, ver2, [], 0)