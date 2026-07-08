'''
El problema del Independent Set se define como: dado un grafo no dirigido, obtener el máximo subconjunto de vértices del grafo tal que ningun par de vértices del subconjunto sea adyacente entre si. Dicho conjunto es un Independet Set. Definir el problema de decisión del Independent Set. Luego, implementar un verificador polinomial para este problema. ¿Cuál es la complejidad del verificador implementado? Justificar
'''

'''
El problema de decision del Independent Set es si existe al menos un set de tamaño k que sea independiente.
'''

def verificador_is(grafo, set, k):
	if len(set) >= k:
		return False
	
	for v in set:
		for vecino in grafo.adyacentes(v):
			if vecino in set:
				return False
	
	return True

'''
Complejidad:
	- Por cada vertice del set (O(n)) recorro todos sus vecinos (O(m)) y verifico si se encuentra tambien en el set, en caso de ser asi devuelvo falso.
Por lo tanto la complejidad resulta en:
	- O(n * m)

El verificador no debe comprobar que el conjunto es máximo. Solo verifica que es independiente y que su tamaño es al menos k.
Comprobar maximalidad o optimalidad es tan difícil como resolver el problema de optimización, por lo cual no es verificable en tiempo polinomial conocido.
'''