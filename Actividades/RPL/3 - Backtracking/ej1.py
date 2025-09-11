'''
Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, 
devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

Métodos del grafo:
	Grafo(dirigido = False, vertices_init= []) para crear (hacer 'from grafo import Grafo')
	agregar_vertice(self, v)
	borrar_vertice(self, v)
	agregar_arista(self, v, w, peso = 1)
		- el resultado será v <--> w
	borrar_arista(self, v, w)
	estan_unidos(self, v, w)
	peso_arista(self, v, w)
	obtener_vertices(self)
		- Devuelve una lista con todos los vértices del grafo
	vertice_aleatorio(self)
	adyacentes(self, v)
	str
'''

from grafo import Grafo

def no_adyacentes_dfs(grafo, vertices, indice_actual, visitados, n):
	if len(visitados) == n:
		return visitados
	
	if indice_actual == len(vertices): # Se recorrieron todos y no se consiguio el subconjunto
		return None
	
	vertice = vertices[indice_actual]
	
	if all(vecino not in visitados for vecino in grafo.adyacentes(vertice)):
		visitados.append(vertice)
		v = no_adyacentes_dfs(grafo, vertices, indice_actual + 1, visitados, n)
		if v:
			return v
		visitados.pop() # Deshago para probar otra posibilidad

	return no_adyacentes_dfs(grafo, vertices, indice_actual + 1, visitados, n) # El vertice anterior no cumple entonces sigo

def no_adyacentes(grafo, n):
	visitados = []
	vertices = grafo.obtener_vertices()
	return no_adyacentes_dfs(grafo, vertices, 0, visitados, n)