'''
Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero `n` menor a |V|, devuelva si es posible obtener un subconjunto de `n` vertices tal que ningun par de vertices sea adyacente entre si.

Métodos del grafo:
	Grafo(dirigido = False, vertices_init= []) para crear (hacer 'from grafo import Grafo')
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

def compatible(grafo, v, sol):
    for vecino in grafo.adyacentes(v):
        if vecino in sol:
            return False
    return True

def _rec_no_adyacentes(grafo, vertices, i_actual, n, sol):
    if len(sol) == n:
        return sol[:]
    
    if i_actual == len(vertices):
        return None
    
    actual = vertices[i_actual]
    if compatible(grafo, actual, sol):
        sol.append(actual)
        resul = _rec_no_adyacentes(grafo, vertices, i_actual + 1, n, sol)
        if resul is not None:
            return resul
        sol.pop()

	return _rec_no_adyacentes(grafo, vertices, i_actual + 1, n, sol)

def no_adyacentes(grafo, n):
	'Devolver una lista con los n vértices, o None de no ser posible'
	vertices = grafo.obtener_vertices()
	return _rec_no_adyacentes(grafo, vertices, 0, n, [])