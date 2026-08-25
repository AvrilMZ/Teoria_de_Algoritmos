"""
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
"""


def anteriores_visitados(grafo, visitados, v):
    for u in visitados:
        if (
            u in grafo.adyacentes(v) and v not in visitados
        ):  # si v -> u, v no visitado pero u si => falso
            return False
    return True


def contar_ordenamientos_bt(grafo, vertices, visitados):
    if len(visitados) == len(vertices):
        return 1

    total = 0
    for v in vertices:
        if v not in visitados and anteriores_visitados(
            grafo, visitados, v
        ):  # Solo agrego el vertice solo si todos sus anteriores fueron visitados.
            visitados.add(v)
            total += contar_ordenamientos_bt(grafo, vertices, visitados)
            visitados.remove(v)

    # No pruebo salteando ya que todos los vertices deben estar incluidos en el orden

    return total


def contar_ordenamientos(grafo):
    vertices = grafo.obtener_vertices()
    return contar_ordenamientos_bt(grafo, vertices, set())
