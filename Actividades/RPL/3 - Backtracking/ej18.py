'''
Implementar un algoritmo que, por backtracking, obtenga la cantidad total de posibles ordenamientos topológicos de un grafo dirigido y acíclico.

Métodos del grafo:
	Grafo(dirigido = False, vertices_init = []) para crear un grafo no dirigido (hacer 'from grafo import Grafo')
	Grafo(dirigido = True, vertices_init = []) para crear un grafo dirigido (hacer 'from grafo import Grafo')
	agregar_vertice(self, v)
	borrar_vertice(self, v)
	agregar_arista(self, v, w, peso = 1)
	borrar_arista(self, v, w)
	estan_unidos(self, v, w)
	peso_arista(self, v, w)
	obtener_vertices(self)
		Devuelve una lista con todos los vértices del grafo
	vertice_aleatorio(self)
	adyacentes(self, v)
	str
'''

def cant_ordenes(grafo, vertices, visitados):
	if len(vertices) == len(visitados):
		return 1
	
	cont = 0
	for vertice in vertices:
		if vertice not in visitados:
			predecesores = []
			for posible_predecesor in vertices:
				if vertice in grafo.adyacentes(posible_predecesor):
					predecesores.append(posible_predecesor)

			todos_predecesores_visitados = True
			for predecesor in predecesores:
				if predecesor not in visitados:
					todos_predecesores_visitados = False
					break

			if todos_predecesores_visitados:
				visitados.append(vertice)
				cont += cant_ordenes(grafo, vertices, visitados)
				visitados.pop()

	return cont

def contar_ordenamientos(grafo):
	vertices = grafo.obtener_vertices()
	return cant_ordenes(grafo, vertices, [])