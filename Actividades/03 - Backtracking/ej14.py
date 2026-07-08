"""
Un set dominante (Dominating Set) de un grafo `G` es un subconjunto `D` de vértices de `G`, tal que para todo vértice de `G`:
        o bien (i) pertenece a `D`;
        o bien (ii) es adyacente a un vértice en `D`.

Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.

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


def es_adyacente(grafo, subset, vertice):
    adyacentes = grafo.adyacentes(vertice)
    for v in subset:
        if v in adyacentes:
            return True
    return False


def dominante(grafo, subset):
    for v in grafo.obtener_vertices():
        if v not in subset and not es_adyacente(grafo, subset, v):
            return False
    return True


def dsm_backtracking(grafo, vertices, subset, indice, mejor):
    if indice == len(vertices):
        if dominante(grafo, subset):
            mejor = subset[:]
        return mejor

    vertice = vertices[indice]

    subset.append(vertice)
    agrego = dsm_backtracking(grafo, vertices, subset, indice + 1, mejor)
    subset.pop()

    salteo = dsm_backtracking(grafo, vertices, subset, indice + 1, mejor)

    if len(agrego) < len(salteo):
        return agrego
    return salteo


def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    return dsm_backtracking(grafo, vertices, [], 0, vertices)
