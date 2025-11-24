'''
Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. Por problemas presupuestarios, desean pintar los colectivos con la menor cantidad posible `k` colores diferentes. Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber cuál es ese mínimovalor para cumplir con lo pedido (pintar cada línea con alguno de los `k` colores, de tal forma que no hayan dos de mismo color coincidiendo en la misma parada). 

Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí, modelar el problema utilizando 
grafos e implementar un algoritmo que determine el mínimo valor `k` para resolver el problema. Indicar la complejidad del algoritmo implementado.

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

from grafo import Grafo

def crear_grafo(colectivos, paradas):
	grafo = Grafo()

	vertices_agregados = []
	for colectivo in colectivos:
		grafo.agregar_vertice(colectivo)
		vertices_agregados.append(colectivo)

	for parada in paradas:
		for vecino in parada:
			if vecino not in vertices_agregados:
				grafo.agregar_vertice(vecino)
				vertices_agregados.append(vecino)

	for parada in paradas:
		for i in range(len(parada)):
			for j in range(i + 1, len(parada)):
				if not grafo.estan_unidos(parada[i], parada[j]):
					grafo.agregar_arista(parada[i], parada[j])
				
	return grafo

def es_valido(grafo, colores, vertice, color):
	for vecino in grafo.adyacentes(vertice):
		if vecino in colores and colores[vecino] == color:
			return False
	return True

def colorear_bt(grafo, vertices, indice, colores, record_min):
	if indice == len(vertices):
		usado = len(set(colores.values()))
		return min(record_min, usado)

	vertice = vertices[indice]
	for color in range(record_min):
		if es_valido(grafo, colores, vertice, color):
			colores[vertice] = color
			record_min = colorear_bt(grafo, vertices, indice + 1, colores, record_min)
			del colores[vertice]

	return record_min

def pintar_colectivos(colectivos, paradas):
	if len(colectivos) == 0:
		return 0
	elif len(paradas) == 0:
		return 1
	grafo = crear_grafo(colectivos, paradas)
	vertices = grafo.obtener_vertices()
	return colorear_bt(grafo, vertices, 0, {}, len(vertices))

'''
Complejidad:
	- Crear el grafo: O(n * m²), siendo n la cantidad de paradas todales y m la cantidad de lineas de la parada. Se recorre por cada parada todas las lineas y por cada linea se recorren las siguientes para agregar las conexiones.
	- Recorrido backtracking: O(m^m * k), siendo m la cantidad de lineas de colectivo (maximo total de colores posibles) y k los vertices adyacentes, que en el peor de los casos es igual a m. Entonces O(m^m * m) ya que por cada vertice se recorren todos los colores y por cada vecino de ese vertice tambien.
Por lo tanto la complejidad en tiempo resulta en:
	O(m^m * m)
'''