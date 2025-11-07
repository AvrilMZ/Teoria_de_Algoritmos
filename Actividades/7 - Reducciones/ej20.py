'''
El problema de elección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P1, P2, ⋯, Pc​ de caminos dentro de dicho grafo y un número k, ¿es posible seleccionar al menos k de esos caminos tales que ningún par de caminos seleccionados comparta ningún nodo? Demostrar que Path Selection es un problema NP-Completo. 
Ayuda: este problema tiene mucha semejanza con Independent Set.
'''

'''
Path Selection: ¿Existen al menos k caminos tales que ningun par de caminos seleccionados comparta ningun nodo en un grafo dirigido?
Independent Set: ¿?

Para que el problema Path Selection sea NP-Completo debe estar primero en NP:
'''

def verificador_ps(pedidos, k, seleccion):
	if len(seleccion) < k:
		return False

	for c in seleccion:
		if c not in pedidos:
			return False
	
	for i in range(len(seleccion)):
		c_1 = seleccion[i]
		for j in range(i + 1, len(seleccion)):
			c_2 = seleccion[j]
			if any(v in c_2 for v in c_1):
				return False
	
	return True

# Complejidad:
#	O(k^2 * V), siendo V la cantidad de vertices que puede tener el camino.
# Por lo que el problema Path Selection pertenece a NP.

'''

	Independent Set <=_p Path Selection

Demostración:
-> Si existe Independent Set entonces existe Path Selection:


-> Si existe Path Selection entonces existe Independent Set:

'''