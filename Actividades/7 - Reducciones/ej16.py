'''
El Hitting-Set Problem se define de la siguiente forma: Dado un conjunto de elemento A de n elementos, m subconjuntos B_1, B_2, ..., B_m​ de A (B_i ⊆ A, ∀i), y un número k, ¿existe un subconjunto C ⊆ A con ∣C∣ ≤ k tal que C tenga al menos un elemento de cada B_i​ (es decir, C ∩ B_i ≠ ∅)?

Demostrar que el Hitting-Set Problem es un problema NP-Completo.
'''

'''
Hitting-Set: ¿Existe un subconjunto C de a lo sumo k elementos que contenga al menos un elemento de cada subconjunto de M?
Vertex Cover: ¿Existe un subconjunto C' de a lo sumo k' elementos (vertices) que se relacione con todos los V - k' vertices del grafo?

Para demostrar que el Hitting-Set Problem es un problema NP-Completo primero debemos ver si se encuentra en NP:
'''

def verificador_hs(A, M, C, k):
	if len(C) > k:
		return False

	for elem in C:
		if elem not in A:
			return False
	
	for b in M:
		if not any(elem in C for elem in b):
			return False
			
	return True

# Complejidad:
#	- O(A * C) + O(M * C)
# Dada que la complejidad es polinomial podemos afirmar que el Hitting-Set Problem se encuentra en NP.

'''
Dado un G = (V, E) que es A donde cada vertice sea un elemento de A (por lo que tambien son elementos de m) conectando todos aquellos que se encuentren en un mismo subconjunto B_i, al aplicar el algoritmo de Vertex Cover obtendriamos el subconjunto C buscado, con k = k'.
	Vertex Cover <=_p Hitting-Set

Demostración:
-> Si existe Vertex Cover existe Hitting-Set:
	Dado un grafo con V vertices y E aristas tenemos un subconjunto C' con k' elementos tal que todas las aristas queden cubiertas. Suponiendo que cada vertice es un valor y cada arista es una union entre elementos de un subconjunto, obtendriamos k' elementos que se relacionan con todos los valores restantes de C' consiguiendo un Hitting-Set.

-> Si existe Hitting-Set existe Vertex Cover:
	Dado un subconjunto C con k elementos y un espacio muestral A. Suponiendo que cada valor de A es un vertice y las conecciones con aristas son generadas mediante los valores de los subconjuntos de M, vemos que solo con los vertices pertenecientes a C podemos conectar con al menos un elemento de cada subconjunto, consiguiendo indirectamente el Vertex Cover (ya que cada arista tendria al menos uno de sus vertices en el set).

Por lo tanto el Hitting-Set Problem es un problema NP-Completo.
'''