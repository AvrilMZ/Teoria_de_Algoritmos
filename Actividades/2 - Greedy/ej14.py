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

def comparten_area(submarino, faro):
	x1, y1 = submarino
	x2, y2 = faro
	return (x2 - 2 <= x1 <= x2 + 2) and (y2 - 2 <= y1 <= y2 + 2)

def esta_iluminado(submarino, faros):
	if len(faros) == 0:
		return False
	
	for faro in faros:
		if comparten_area(submarino, faro):
			return True
	
	return False

def buscar_cobertura(fil, col, submarinos_pendientes):
	cobertura = set()
	for submarino in submarinos_pendientes:
		if comparten_area(submarino, (fil, col)):
			cobertura.add(submarino)
	return cobertura

def buscar_submarinos(matriz):
	submarinos = set()
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if matriz[i][j]:
				submarinos.add((i, j))
	return submarinos

# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
	if len(matriz) == 0:
		return []

	faros = []
	while True:
		max_cobertura = 0
		mejor_pos = None
		for i in range(0, len(matriz)):
			for j in range(0, len(matriz[0])):
				cobertura = 0
				for x in range(0, len(matriz)):
					for y in range(0, len(matriz[0])):
						if (matriz[x][y] and not esta_iluminado((x, y), faros) and comparten_area((x, y), (i, j))):
							cobertura += 1
				if cobertura > max_cobertura:
					max_cobertura = cobertura
					mejor_pos = (i, j)
		if max_cobertura == 0:
			break
		faros.append(mejor_pos)
	
	return faros

'''
Complejidad:
	- El algoritmo itera k veces (una por cada faro colocado), siendo k la cantidad de faros necesarios;
	- En cada iteración, recorre toda la matriz para encontrar la mejor posición: O(n * m);
	- Por cada posición candidata (i,j), recorre nuevamente la matriz para contar submarinos no iluminados que cubriría: O(n * m);
	- Por lo que cada iteración es O(n * m * n * m) = O(n^2 * m^2);
	- Complejidad final: O(k * n^2 * m^2)
'''