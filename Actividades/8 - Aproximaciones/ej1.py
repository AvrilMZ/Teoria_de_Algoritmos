'''
Dado un grafo en forma de grilla como el dado a continuación (y también a los del ejercicio 2), donde cada vértice tiene un peso w(v), se desea maximizar la sumatoria de los pesos de un Independent Set sobre dicho grafo.
	a. Dar un algoritmo greedy que sirva de aproximación para la solución al problema.
	b. Demostrar que cualquier vértice es parte de la solución aproximada, o bien tiene peso menor (o igual) a alguno de sus adyacentes, que es en efecto parte de dicha solución.
	c. Analizar qué tan buena es la aproximación.
'''

'''
a. El algoritmo greedy que se puede proponer es: (MAL)
	1. Dado un vertice v, con ninguno de sus vecinos x_i dentro del set y su respectivo perso w(v).
	2. Agrego si ninguno de sus adyacentes esta en el set.
	3. Sigo con el vecino cuyo coeficiente, (\sum{w(x_i)}) / (cant. de vecinos - 1), sea mayor. -> x_i != v
'''