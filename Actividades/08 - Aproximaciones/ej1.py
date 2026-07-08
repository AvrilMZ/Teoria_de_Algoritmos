'''
Dado un grafo en forma de grilla como el dado a continuación (y también a los del ejercicio 2), donde cada vértice tiene un peso w(v), se desea maximizar la sumatoria de los pesos de un Independent Set sobre dicho grafo.
	a. Dar un algoritmo greedy que sirva de aproximación para la solución al problema.
	b. Demostrar que cualquier vértice es parte de la solución aproximada, o bien tiene peso menor (o igual) a alguno de sus adyacentes, que es en efecto parte de dicha solución.
	c. Analizar qué tan buena es la aproximación.
	d. Analizar qué tan buena es la aproximación en el caso de un grafo que no necesariamente tenga esta forma de grilla.
'''

'''
a. Un algoritmo greedy seria elegir el siguiente en base a un coeficiente, este podria conseguirse haciendo $w(v) / (cant. de adyacentes)$ -> incluyendo al actual, siendo v el vecino del vertice actual. Eligiriamos al vecino cuyo coeficiente sea mayor ya que nos garantizaria una mayor ganancia en cuanto a peso obtenido segun la cantidad de adyacentes que "bloquee".

b. Supongamos que u no pertenece al conjunto solucion, si u no pertence entonces existe un vecino v que si pertence con un coeficiente $w(v) / (grado(v) + 1)$ mayor, por lo que nos asegura que u fue considerado al momento de conseguir la solucion como asi tambien todos los vecinos de v. Por lo tanto, todo vertice no contenido en la solucion tiene un adyacente con coeficiente mayor o igual a él.

c. Dado que disponemos de una grilla $nxn$ donde cada celda tiene como máximo 4 adyacentes y como mínimo 2 (según corresponda), en el peor de los casos tendremos a un grupo vertices con pesos muy grandes juntos, con el vertice central con al menos 1 numero mas de peso, donde el vertice incluido en la solucion es el central. Podemos considerar que seria peor cuanto mas cantidad de adyacentes haya, ya que realizando la sumatoria resultariamos en una mayor cantidad de peso perdida, es asi que podemos aproximar un 4-aproximacion, siendo 4 los vecinos con pesos enormes los que se estan "perdiendo" por no estar incluidos, resultando en una perdida de 4 veces el peso del vertice incluido en la solucion.

d. En el caso de que el grafo no tenga forma de grilla la situacion es la misma, supongamos que disponemos de un vertice con e+1 de peso y todos sus adyacentes de peso e, el vertice "central" seria aquel que se incluye en la solucion y se estaria perdiendo la cantidad de adyacentes maxima por el peso del vertice incluido, resultando en una (cant. de adyacentes maxima)-aproximación.
'''