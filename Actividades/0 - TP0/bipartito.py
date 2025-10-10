'''
Implementar un algoritmo que reciba un grafo y determine si el mismo es un grafo bipartito, o no. 
Es decir, la función es_bipartito debe devolver True si el grafo recibido por parámetro es efectivamente bipartito, False en caso contrario. 
Que un grafo sea Bipartito implica que puede separarse los vértices en dos grupos S y T, tal que para cada par de vértices de S no exista 
arista entre sí (lo mismo para T), que la intersección entre S y T sea vacía y que la unión sea igual al conjunto de todos los vértices del grafo.

A fines del ejercicio, considerar que se pueden ver todos los vértices del grafo en un orden aleatorio con for v in grafo, y el grafo cuenta con 
la primitivas hay_arista(origen, destino) (devuelve bool), adyacentes(vertice) que devuelve una lista de vértices adyacentes al indicado, y vertices() 
que nos devuelve todos los vértices (lista).

El grafo internamente se encuentra implementado con listas de adyacencia (en su versión de diccionario de diccionarios), a considerar para la complejidad.
'''

import sys
sys.setrecursionlimit(10000)

def dfs_bipartito(grafo, vertice, color_actual, colores):
	colores[vertice] = color_actual
	for vecino in grafo.adyacentes(vertice):
		if vecino not in colores:
			if not dfs_bipartito(grafo, vecino, not color_actual, colores):
				return False
		elif colores[vecino] == color_actual:
			return False
	return True

def es_bipartito(grafo):
	colores = {}
	for vertice in grafo.vertices():
		if vertice not in colores:
			if not dfs_bipartito(grafo, vertice, True, colores):
				return False
	return True