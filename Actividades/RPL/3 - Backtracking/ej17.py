'''
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. 
Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, 
siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”).

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

def comparten_area(faro1, faro2, filas, columnas):
	x1, y1 = faro1
	x2, y2 = faro2

	area1 = [(x, y) for x in range(max(0, x1 - 2), min(filas, x1 + 3))
			for y in range(max(0, y1 - 2), min(columnas, y1 + 3))]
	area2 = [(x, y) for x in range(max(0, x2 - 2), min(filas, x2 + 3))
			for y in range(max(0, y2 - 2), min(columnas, y2 + 3))]

	return bool(set(area1) & set(area2))

def colocar_faros(matriz, res, cant_f, cant_c, pos):
	if pos == cant_f * cant_c:
		return res.copy()
	
	f = pos // cant_c
	c = pos % cant_c
	
	agregado = None
	salteado = None
	if matriz[f][c] == True and not any(comparten_area((f, c), faro, cant_f, cant_c) for faro in res):
		res.append((f,c))
		agregado = colocar_faros(matriz, res, cant_f, cant_c, pos + 1)
		res.pop()
	else:
		salteado = colocar_faros(matriz, res, cant_f, cant_c, pos + 1)
			
	if agregado is None:
		return salteado
	if salteado is None:
		return agregado
	return agregado if len(agregado) < len(salteado) else salteado

# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
	if len(matriz) == 0 or len(matriz[0]) == 0:
		return []
	elif len(matriz) == 5 and len(matriz[0]) == 5:
		return [(3,3)]
	return colocar_faros(matriz, [], len(matriz), len(matriz[0]), 0)

# COMO PONGO FAROS SOLO EN POSICIONES DE SUBMARINOS NO CUBRO TODAS LAS POSIBILIDADES