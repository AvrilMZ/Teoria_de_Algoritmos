'''
Implementar un modelo de programación lineal que permita determinar el clique de tamaño máximo dentro de un grafo. Indicar la cantidad de restricciones generadas en función de la cantidad de vértices y aristas (podés usar notación O para esto, no es importante el número exacto).

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

Recordar que aquí estamos usando PuLP para resolver el problema porque es la forma programática de poder evaluarlo en RPL. A la hora del parcial lo que nos es relevante es el modelo.
'''

'''
V: "Vertice"
X: "Variable binaria, está o no en el clique"

\max{\sum_{i = 0}^{n} V_i}

X_i + X_j <= 1 -> Esto implica que el vecino esta pero él no, o directamente no esta ninguno

dado que i NO es vecino de j y n la cantidad maxima de vertices.
'''

import pulp

def clique_maximo(grafo):
	vertices = grafo.obtener_vertices()
	
	prob = pulp.LpProblem("Clique Maximo", pulp.LpMaximize)
	X = {i: pulp.LpVariable(f"X_{i}", cat="Binary") for i in vertices}
	
	prob += pulp.lpSum([X[i] for i in vertices])

	for i in vertices:
		for j in vertices:
			if i < j and not grafo.estan_unidos(i, j): # ningún par de vértices NO conectados puede estar juntos
				prob += X[i] + X[j] <= 1

	prob.solve()

	return [i for i in vertices if X[i].varValue == 1]