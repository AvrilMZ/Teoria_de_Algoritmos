'''
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. 

Implementar un algoritmo Greedy que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). 

Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.

Métodos del grafo:
	Grafo(dirigido = False, vertices_init = []) para crear un grafo no dirigido (hacer 'from grafo import Grafo')
	Grafo(dirigido = True, vertices_init = []) para crear un grafo dirigido (hacer 'from grafo import Grafo')
	agregar_vertice(self, v)
	borrar_vertice(self, v)
	agregar_arista(self, v, w, peso = 1)
	borrar_arista(self, v, w)
	estan_unidos(self, v, w)
	peso_arista(self, v, w)
	obtener_vertices(self)
		Devuelve una lista con todos los vértices del grafo
	vertice_aleatorio(self)
	adyacentes(self, v)
	str
'''

def comparten_area(submarino, faro, filas, columnas):
	x2, y2 = faro

	area = [(x, y) for x in range(max(0, x2 - 2), min(filas, x2 + 3))
			for y in range(max(0, y2 - 2), min(columnas, y2 + 3))]

	return submarino in area

def esta_iluminado(submarino, faros, filas, columnas):
	if len(faros) == 0:
		return False
	
	for faro in faros:
		if comparten_area(submarino, faro, filas, columnas):
			return True
	
	return False

# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
	if len(matriz) == 0:
		return []

	filas = len(matriz)
	columnas = len(matriz[0])
	faros = []

	for i in range(0, filas):
		for j in range(0, columnas):
			submarino = matriz[i][j]
			if submarino and not esta_iluminado((i,j), faros, filas, columnas):
				if i + 2 < filas and j + 2 < columnas:
					faros.append((i+2,j+2))
				else:
					faros.append((i,j))

	return faros

# FALLAN 2 TESTS

'''
Complejidad:
	- Recorrer la matriz: O(n * m), siendo n la cantidad de filas y m la cantidad de columnas;
	- Recorrer por cada submarino todos los faros para verficar si alguno lo ilumina: O(s * k), siendo s la cantidad de submarinos y k la cantidad de faros colocados. Dado que k en el peor de los casos es igual a s podemos escribir la complejidad como O(s^2).
Por lo que la complejidad final resulta en:
	O(n * m + s^2)
'''