"""
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
"""


def cubre_todas_aristas(grafo, visitados):
    for vertice in grafo.obtener_vertices():
        for vecino in grafo.adyacentes(vertice):
            if vertice not in visitados and vecino not in visitados:
                return False
    return True


def buscar_min_vc(grafo, vertices, visitados, indice, mejor):
    if len(vertices) == indice:
        if cubre_todas_aristas(grafo, visitados):
            mejor = visitados[:]
        return mejor

    vertice = vertices[indice]

    visitados.append(vertice)
    agrego = buscar_min_vc(grafo, vertices, visitados, indice + 1, mejor)
    visitados.pop()

    salteo = buscar_min_vc(grafo, vertices, visitados, indice + 1, mejor)

    if len(agrego) < len(salteo):
        return agrego
    return salteo


def vertex_cover_min(grafo):
    vertices = grafo.obtener_vertices()
    return buscar_min_vc(grafo, vertices, [], 0, vertices)
