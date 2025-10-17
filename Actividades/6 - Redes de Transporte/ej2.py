'''
Implementar el algoritmo de Ford-Fulkerson, asumiendo que ya está implementada una función 'actualizar_grafo_residual', definida como 'actualizar_grafo_residual(grafo_residual, u, v, valor)', que recibe el grafo residual, una arista dirigida dada por los vértices u y v, y el nuevo valor del flujo a través de la arista (u,v) y actualiza el grafo residual ya teniendo en cuenta el peso anterior de la arista, y su antiparalela. 
Devolver un diccionario con los valores de los flujos para todas las aristas del grafo original.
'''

def ford_fulkerson(grafo, s, f):
	