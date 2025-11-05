'''
Definir el problema de decisión de las N-Reinas. Usar que N-Reinas es un problema NP-Completo para demostrar que Demostrar que Independent Set es un problema NP-Completo.
'''

'''
N-Reinas: ¿Existe un subonjunto de n reinas que se puedan poner en un tablero NxN para que no se ataquen entre sí?
Independent Set: ¿Existe al menos un subonjunto n de vertices del grafo tal que ninguno de ellos se relacione entre sí?

Para demostrar que Independent Set es un problema es NP-Completo primero debemos demostrar que se encuentra en NP:
'''

def verificador_is(grafo, i_set, n):
	if len(i_set) < n:
		return False
	
	for v in i_set:
		for vecino in grafo.adyacentes(v):
			if vecino in i_set:
				return False
	return True

# Complejidad:
#	- O(n * m), dado que por cada vertice (n) de la solucion dada se verifica que ninguno de sus adyacentes (m) se encuentre tambien en la solucion.
# Se puede realizar un verificador en tiempo polinomial por lo que el problema de Independent Set se encuentra en NP.

'''
Por cada casilla del tablero creamos un vertice V en el grafo G, cada vertice va a tener una arista con todos los vertices de sus diagonales y sus rectas (construccion en tiempo polinomial O(n^2)). En caso de querer ver las posiciones posibles para colocar reinas ejecutamos el algoritmo de Independent Set y obtendriamos los vertices adecuados.

Demostración:
-> Si hay N-Reinas hay Independent Set:
	Dadas las n reinas colocadas, por la naturaleza del problema conocemos que esas posiciones no pueden relacionarse con ninguna de las otras n (esto implica que no se encuentren ni en sus diagonales o rectas), notemos como ese subconjunto de n posiciones es un Independent Set.

-> Si hay Independent Set hay N-Reinas:
	Dados los V vertices de un grafo y los n' vertices pertenencientes al Independent Set sabemos que ninguno de ellos va a tener una arista con otro vertice tambien perteneciente al subconjunto solucion. Podemos definir un vertice V_i y sus adyacentes como una instancia de un tablero, sabiendo que sus adyacentes van a ser las celdas vecinas (o las que esten habilitadas para un movimiento), es asi como notamos que obtendriamos las n posiciones de reinas, resultando en que n' = n.

Concluimos que Independent Set es un problema NP-Completo.
'''