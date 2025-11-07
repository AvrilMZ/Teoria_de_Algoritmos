'''
Dados los problemas de decisiones de Independent Set y Vertex Cover, realizar dos reducciones.
	a. Reducir Independent Set a Vertex Cover.
	b. Reducir Vertex Cover a Independent Set.
'''

'''
Independent Set: ¿Existe un conjunto k de vertices en el problema Vertex Cover tal que sea Independent Set?
Vertex Cover: ¿Exisite un conjunto k de vertices en el problema Independent Set tal que sea Vertex Cover?

a. 
Para este problema buscamos un subconjunto S de vertices tal que ninguno de ellos tenga una arista que los una.
Consideramos el subconjunto C aquel con los vertices que resuelvan el problema de vertex cover.
El principal inconveniente que surge al comparar ambos algoritmos es que:
	- Dos vertices pueden no estar en un Independent Set pero al menos uno de ellos deberia estarlo para pertenecer a un Vertex Cover.
Notamos que si el vertice no pertenece al Vertex Cover podria pertenecer al Independent Set. Consideramos V_i y V_j a dos vertices pertenecientes al grafo y unidos por una arista, donde al menos ambos de ellos tienen un vecino mas que no es ninguno de ellos, si:
	- V_i pertenece a la solucion del Vertex Cover y V_j no, entonces tambien pertenece a la solucion de Independent Set.
	- Si ambos estan en la solucion de Vertex Cover entonces no pertenece a la solucion de Independent Set.
Es asi donde vemos la relacion de que si G es el grafo con el que se trabaja: G - C = S -> Complemento de Vertex Cover = Independent Set

b.
Ahora buscamos un subconjunto C de vertices tal que todas las aristas tengan al menos uno de sus vertices en el conjunto.
Sea S la solucion al problema de Independent Set. Note que surge el problema:
	- Dos vertices pueden no estar incluidos en S y ser una solucion valida para Independent Set, aunque no valida para Vertex Cover.
Consideremos V_i y V_j a vertices pertenenicentes al grafo y unidos por una arista, sonde al menos ambos de ellos tienen un vecino mas que no es ninguno de ellos, si:
	- V_i pertenece a la solucion del Independent Set y V_j no, entonces tambien pertenece a la solucion de Vertex Cover.
	- Si V_i y V_j no estan en la solucion de Independent Set entonces no pertenecen a la solucion de Vertex Cover.
Es asi donde vemos la relacion de que si G es el grafo con el que se trabaja: G - S = C -> Complemento de Independent Set = Vertex Cover
'''