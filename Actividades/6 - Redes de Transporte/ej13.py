'''
Carlos tiene un problema: sus 5 hijos no se soportan. Esto es a tal punto, que ni siquiera están dispuestos a caminar juntos para ir a la escuela. Incluso más: ¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus hermanos! Sólo aceptan pasar por las esquinas, si es que algún otro pasó por allí. Por suerte, tanto la casa como la escuela quedan en esquinas, pero no está seguro si es posible enviar a sus 5 hijos a la misma escuela. No se puede asumir que la ciudad tenga alguna forma en específico, por ejemplo, no hay que asumir que todas las calles sean cuadradas. Utilizando lo visto en la materia, formular este problema y resolverlo. Indicar y justificar la complejidad del algoritmo.
'''

'''
Tomamos a la casa como la fuente de la red de flujo y la escuela como el sumidero, cada esquina un vertice (siendo las calles las aristas). Nos encontramos con el problema de aristas no dirigidas entre esquinas, entonces para solucionarlo creamos un nuevo vertice ficticio intermedio para evitar antiparalelas, aunque puede pasar que dos hijos pasen por ahi tambien entonces luego de obtener el flujo maximo, anulamos el flujo que pueda haber en esas aristas (forzando a que no pasen por ahi).
'''

from ff import flujo
from grafo import Grafo

def crear_red(grafo_ciudad, casa, escuela):
    esquinas = grafo_ciudad.obtener_vertices()
    red = Grafo(True, esquinas)
    visitados = set()
    ficticios = {}

    for esquina in grafo_ciudad.adyacentes(casa):
        red.agregar_arista(casa, esquina)

    for esquina in grafo_ciudad.adyacentes(escuela):
        red.agregar_arista(esquina, escuela)

    for esquina in esquinas:
        if esquina is casa or esquina is escuela:
            continue
        for vecino in grafo_ciudad.adyacentes(esquina):
            if vecino in visitados:
                continue
            nuevo = esquina + vecino # para ponerle un nombre único
            red.agregar_vertice(nuevo)
            red.agregar_arista(esquina, nuevo)
            red.agregar_arista(nuevo, vecino)
            red.agregar_arista(vecino, esquina)
            ficticios[nuevo] = (esquina, vecino)
        visitados.add(esquina)
    
    return red, ficticios

def carlos(grafo_ciudad, casa, escuela, cant_hijos):
    red, ficticios = crear_red(grafo_ciudad, casa, escuela)
    flujo_max = flujo(red, casa, escuela)

    sum_salida = 0
    for vecino in red.adyacentes(casa):
        sum_salida += flujo_max[(casa, vecino)]
    if sum_salida < cant_hijos: # no hay suficientes calles para que salgan todos los hijos
        return None
    
    for ficticio in ficticios:
        esquina, otra = ficticios[ficticio]
        if flujo_max[(esquina, otra)] > 0 and flujo_max[(esquina, ficticio)] > 0: # para evitar que pasen por una misma calle, fuerzo a que directamente no puedan pasar
            flujo_max[(esquina, otra)] = 0
            flujo_max[(esquina, ficticio)] = 0
            flujo_max[(ficticio, otra)] = 0

    caminos = []
    for _ in range(cant_hijos): # busco un camino para cada hijo
        camino_i = [casa]
        v = casa
        while v is not escuela:
            for vecino in red.adyacentes(v):
                if flujo_max[(v, vecino)] == 0:
                    continue
                flujo_max[(v, vecino)] = 0
                v = vecino
                if v not in ficticios:
                    camino_i.append(v)
                break
        caminos.append(camino_i)

    return caminos

'''
Complejidad:
    - O(V * E^2), por el algoritmo de Ford-Fulkerson.
'''