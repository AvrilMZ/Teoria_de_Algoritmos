'''
El problema de Separación en R Cliques (SRC) se enuncia como: Dado un grafo, y un valor entero R, ¿se pueden separar todos los vértices del gráfo en a lo sumo R cliques? (cada clique puede tener una cantidad diferente de vértices). De una manera más formal, se puede enunciar: ¿existen S_1, S_2, ..., S_k subconjuntos disjuntos del conjunto de vértices V tal que ⋃_i S_i = V, k ≤ R, y que que cada subgrafo correspondiente a los S_i sea un clique (subgrafo completo)?
'''

'''
R Cliques: ¿Existen a lo sumo k subconjuntos disjuntos del conjunto de vértices V, tal que la union de esos subconjuntos sea igual al conjunto V, y que que cada subgrafo correspondiente a los S_i sea un clique?
?: ¿?

Para que el problema R Cliques sea NP-Completo primero debemos verificar si esta en NP:
'''

def verificador_rc(grafo, solucion, R):
	if len(solucion) > R:
		return False