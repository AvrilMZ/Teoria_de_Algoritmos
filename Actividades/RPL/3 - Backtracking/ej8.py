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

def detectar_iso(g1, g2, v1, v2, vertice1, vertice2, visitados, indice):
	if indice == len(v1):
		return True
	
	for vecino in g2.adyacentes(vertice2):
		if vecino not in visitados:
			for new_ver in g1.adyacentes(vertice1):
				if new_ver not in visitados and g1.estan_unidos(vertice1, new_ver) == g2.estan_unidos(vertice2, vecino):
					visitados.append(vecino)
					if detectar_iso(g1, g2, v1, v2, new_ver, vecino, visitados, indice + 1):
						return True
					visitados.pop()

	return False

def hay_isomorfismo(g1, g2):
	ver1 = g1.obtener_vertices()
	ver2 = g2.obtener_vertices()

	if len(ver1) != len(ver2):
		return False
	elif len(ver1) == 0 and len(ver2) == 0:
		return True
	
	for v1 in ver1:
		for v2 in ver2:
			if detectar_iso(g1, g2, ver1, ver2, v1, v2, [], 0):
				return True
	return False

# CORREGIR