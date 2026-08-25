"""
El problema de elección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P1, P2, ⋯, Pc​ de caminos dentro de dicho grafo y un número k, ¿es posible seleccionar al menos k de esos caminos tales que ningún par de caminos seleccionados comparta ningún nodo? Demostrar que Path Selection es un problema NP-Completo.
Ayuda: este problema tiene mucha semejanza con Independent Set.
"""

"""
Path Selection: ¿Existen al menos k caminos tales que ningun par de caminos seleccionados comparta ningun nodo en un grafo dirigido?
Independent Set: ¿Existen al menos k' vertices tales que ninguno sea adyacente con el otro?

Para que el problema Path Selection sea NP-Completo debe estar primero en NP:
"""


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
# 	O(k^2 * V), siendo V la cantidad de vertices que puede tener el camino.
# Por lo que el problema Path Selection pertenece a NP.

"""
Dado un grafo G=(V, E), donde cada vertice representa un pedido P_i, y k = k', buscamos realizar la reduccion:
	Independent Set <=_p Path Selection

Demostración:
-> Si existe Independent Set entonces existe Path Selection:
	Al aplicar el algoritmo de independent set sobre el grafo G planteado obtendriamos los caminos buscados del problema de path selection.

<- Si existe Path Selection entonces existe Independent Set:
	Dado que los caminos no deben compartir ningun nodo, un nodo A perteneciente a la solucion S no tendra niguno de sus adyacentes dento de S, por lo que tendriamos un independent set.

Por lo tanto el problema Path Selection es un problema NP-Completo.
"""
