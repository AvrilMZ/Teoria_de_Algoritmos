'''
El 2-Partition Problem como problema de optimización se describe tal que: Dado un conjunto de nn números positivos T = {T1, T2, …, Tn}, se particionan los números en dos subconjuntos S1​ y S2​ (con intersección vacía y unión = T) de forma de minimizar la sumatoria de cualquiera de los subconjuntos (min ⁡max⁡(S1, S2)).

Para este problema, podemos plantear el siguiente algoritmo aproximado: Inicializar la solución como dos subconjuntos vacíos recorriendo los elementos de T, para cada elemento se lo coloca en el subconjunto con menor sumatoria hasta el momento.

Demostrar que el algoritmo propuesto es una 3/2​-Aproximación.
'''

'''
En este problema nuestro peor caso seria que el ultimo elemento que pongamos sea el mayor de todos, desbalanceando la sumatoria de uno de ellos. Suponiendo que, dados los dos conjuntos, se van agregando elementos siempre a aquel conjunto cuya sumatoria sea la menor y el elemento mas grande queda para el final (con tamaño n). El elemento mas grande que se podria poner es n - 1, entonces tenemos las restincciones:
	- S_i - S_j <= n (siendo S_i el subconjunto mayor que S_j) -> Cota Superior
	- S_j >= n (Siendo S_j el subconjunto menor) -> Cota Inferior
'''