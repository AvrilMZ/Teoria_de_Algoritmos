'''
El problema del Vertex Cover se define como: dado un grafo no dirigido, obtener el mínimo subconjunto de vértices del grafo tal que toda arista del grafo tenga al menos uno de sus vértices perteneciendo al subconjunto. Dicho conjunto es un Vertex Cover. Definir el problema de decisión del Vertex Cover. Luego, implementar un verificador polinomial para este problema. ¿Cuál es la complejidad del verificador implementado? Justificar
'''

'''
El problema de decision de Vertex Cover es si existe un subconjunto de al menos k vertices tal que toda arista del grafo tenga al menos uno de sus vértices perteneciendo al subconjunto.
'''

def verificador_vc(grafo, set, k):
	if len(set) >= k:
		return False
	
	for v in grafo.obtener_vertices():
		for vecino in grafo.adyacentes(v):
			if v not in set or vecino not in set:
				return False
			
	return True

'''
Complejidad:
	- Recorro todos los verices del grafo (O(n)) y por cada vertice recorro todos sus vecinos O(m).
Por lo que la complejidad resulta en:
	- O(n * m)
'''