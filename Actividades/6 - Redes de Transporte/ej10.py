'''
Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). Dado un grafo dirigido y dos vértices s y t, encontrar el máximo número de caminos disjuntos s-t en G. Dar una metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el máximo número de caminos disjuntos. ¿Cuál es la complejidad temporal de la solución implementada? ¿Cómo resolverías el problema si el grafo fuera no dirigido?

Considerar que la función flujo(red) que implementa el algoritmo de Ford-Fulkerson (usando BFS, definida por Edmonds y Karp) ya se encuentra implementada, y devuelve un diccionario con la asignación de flujo que pasa por cada arista de la red definida.

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

La función flujo recibe la red de transporte (debe cumplir con las propiedades de red de transporte), la fuente y el sumidero, en ese orden.
Devuelve un diccionario Arista -> flujo. 
'''

from ff import flujo
from grafo import Grafo

def copiar_grafo(grafo):
	vertices = grafo.obtener_vertices()
	nuevo = Grafo(True, vertices)

	for vertice in vertices:
		for vecino in grafo.adyacentes(vertice):
			nuevo.agregar_arista(vertice, vecino)
	
	return nuevo

# devolver una lista en la cual cada elemento es una lista, con el camino
# entre s y t. Todos esos caminos deben incluir inicio (s) y fin (t).
def disjuntos(grafo, s, t):
	copia = copiar_grafo(grafo)
	flujo_dic = flujo(copia, s, t)
	caminos = []

	while True:
		actual = [s]
		v_actual = s
		hay_sig = True
		while v_actual != t and hay_sig:
			hay_sig = False
			for arista in flujo_dic:
				if arista[0] == v_actual and flujo_dic[arista] == 1:
					hay_sig = True
					v_actual = arista[1]
					actual.append(v_actual)
					flujo_dic[arista] = 0
					break
		if actual[len(actual) - 1] != t:
			break
		caminos.append(actual)
	
	return caminos

'''
Para resolver este problema se plantea un grafo nuevo, copia del anterior, pero con pesos unitarios en las aristas. Luego se ejecuta el algoritmo Ford-Fulkerson que indirectamente me va a devolver la cantidad maxima de caminos disjuntos posibles, esto se debe a que al devolver el flujo maximo por aristas me estaria devolviendo los caminos posibles desde la fuente al sumidero por tener pesos unitarios. La recontruccion implementada lo que hace es recorrer las aristas, desde vertice de origen a fin, del diccionario devuelto siempre y cuando su flujo sea 1.

Complejidad:
	- Copia del grafo: O(V * E)
	- Algoritmo Ford-Fulkerson: O(V * E^2)
	- Reconstruccion: O(V * E^2), ya que en el peor caso por cada iteración recorro todas las aristas.
Por lo que la complejidad final es O(V * E^2)

En caso de que el grafo fuera no dirigido no se podria usar el algoritmo Ford-Fulkerson por lo que se deberia de resolver como un problema normal, no de flujo. Esto implicaria hacer un recorrido dfs mientras que no se utilice alguna arista que haya sido utilizada en algun camino previo.
'''