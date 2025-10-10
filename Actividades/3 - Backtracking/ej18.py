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

def predecesores_visitados(grafo, v, visitados):
	for ver in grafo.obtener_vertices():
		if v in grafo.adyacentes(ver) and ver not in visitados:
			return False
	return True

def contar_ordenamientos_bt(grafo, visitados, parcial, resultado):
	if len(parcial) == len(grafo):
		resultado.append(parcial.copy())
		return
	
	for v in grafo.obtener_vertices():
		if v not in visitados and predecesores_visitados(grafo, v, visitados):
			visitados.add(v)
			parcial.append(v)
			contar_ordenamientos_bt(grafo, visitados, parcial, resultado)
			parcial.pop()
			visitados.remove(v)

def contar_ordenamientos(grafo):
	visitados = set()
	resultado = []
	contar_ordenamientos_bt(grafo, visitados, [], resultado)
	return len(resultado)