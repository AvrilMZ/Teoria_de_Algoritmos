# ==============================================================================================================
# ==============================================================================================================
# PROBLEMAS CONOCIDOS:
# 	- Independent Set
# 	- Camino Hamiltoniano
# 	- Coloreo de grafos
#	- Sudoku
# 	- Caballo de ajedrez
#	- Isomorfismos en Grafos
#	- Subset Sum
#	- Materias Compatibles
#	- Sumatoria de n-dados
#
# RECETA BACKTRACKING:
#	1. Si ya encontre una solucion, la devuelvo y termino.
#	2. Avanzo si puedo
#	3. Pruebo si la solucion parcial es valida:
#		i. Si no lo es, retrocedo (.pop()) y vuelvo a avanzar (punto 2).
#		ii. Si lo es, agrego (.append()) y llamo recursivamente (volver al punto 1).
#	4. Si llegue hasta aca, ya probe con todo y no encontre una solucion.
# ==============================================================================================================
# ==============================================================================================================

# EJ 13
'''
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. 
Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.

Métodos del grafo:
	Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
	agregar_vertice(self, v)
	borrar_vertice(self, v)
	agregar_arista(self, v, w, peso = 1)
		el resultado será v <--> w
	borrar_arista(self, v, w)
	estan_unidos(self, v, w)
	peso_arista(self, v, w)
	obtener_vertices(self)
		Devuelve una lista con todos los vértices del grafo
	vertice_aleatorio(self)
	adyacentes(self, v)
	str
'''

def cubre_todas_aristas(grafo, visitados):
	for vertice in grafo.obtener_vertices():
		for vecino in grafo.adyacentes(vertice):
			if vertice not in visitados and vecino not in visitados:
				return False
	return True

def buscar_min_vc(grafo, vertices, visitados, indice_actual):
	if len(vertices) == indice_actual:
		if cubre_todas_aristas(grafo, visitados):
			return list(visitados)
		return None
	
	vertice = vertices[indice_actual]

	visitados.append(vertice)
	agrego_v = buscar_min_vc(grafo, vertices, visitados, indice_actual + 1)
	visitados.pop()

	salteo_v = buscar_min_vc(grafo, vertices, visitados, indice_actual + 1)

	mejor = None
	if agrego_v is not None and (mejor is None or len(agrego_v) < len(mejor)):
		mejor = agrego_v
	if salteo_v is not None and (mejor is None or len(salteo_v) < len(mejor)):
		mejor = salteo_v
	return mejor
		
def vertex_cover_min(grafo):
	vertices = grafo.obtener_vertices()
	visitados = []
	r = buscar_min_vc(grafo, vertices, visitados, 0)
	if r: 
		return r 
	else: 
		return []

# ============================================================================
# EJ 14
'''
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: 
	o bien (i) pertenece a D;
	o bien (ii) es adyacente a un vértice en D.

Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.

Métodos del grafo:
	Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
	agregar_vertice(self, v)
	borrar_vertice(self, v)
	agregar_arista(self, v, w, peso = 1)
		el resultado será v <--> w
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

def es_adyacente(grafo, subset, vertice):
	adyacentes = grafo.adyacentes(vertice)
	for v in subset:
		if v in adyacentes:
			return True
	return False

def dominante(grafo, subset):
	for v in grafo.obtener_vertices():
		if v not in subset and not es_adyacente(grafo, subset, v):
			return False
	return True

def dsm_backtracking(grafo, vertices, subset, indice):
	if len(vertices) == indice:
		if dominante(grafo, subset):
			return list(subset)
		return None
	
	vertice = vertices[indice]

	subset.append(vertice)
	agrego = dsm_backtracking(grafo, vertices, subset, indice + 1)
	subset.pop()

	salteo = dsm_backtracking(grafo, vertices, subset, indice + 1)

	record = None
	if agrego is not None and (record is None or len(agrego) < len(record)):
		record = agrego
	if salteo is not None and (record is None or len(salteo) < len(record)):
		record = salteo
	return record

def dominating_set_min(grafo):
	subset = []
	vertices = grafo.obtener_vertices()
	r = dsm_backtracking(grafo, vertices, subset, 0)
	if r:
		return r
	else:
		return []
	
# ============================================================================
# EJ 15
'''
Un bodegón tiene una única mesa larga con W lugares. 
Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. 
Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. 
Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. 
Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa 
(o en otras palabras, que dejan la menor cantidad de espacios vacíos).
'''

def grupos_rec(mesa, grupos, conj, indice):
	if indice == len(grupos) or sum(conj) == mesa:
		return conj.copy()

	agrego = []
	if sum(conj) + grupos[indice] <= mesa:
		conj.append(grupos[indice])
		agrego = grupos_rec(mesa, grupos, conj, indice + 1)
		conj.pop()

	salteo = grupos_rec(mesa, grupos, conj, indice + 1)

	if sum(agrego) > sum(salteo):
		return agrego
	else:
		return salteo

def max_grupos_bodegon(P, W):
	if len(P) == 1 and P[0] <= W:
		return [P[0]]
	
	conj = []
	return grupos_rec(W, P, conj, 0)

# ============================================================================
# EJ 16
'''
Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una misma parada de 
colectivo nunca pararán dos colectivos que usen el mismo color. 
El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. 
Por problemas presupuestarios, desean pintar los colectivos con la menor cantidad posible k colores diferentes. 
Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber cuál es ese 
mínimovalor para cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color coincidiendo en la misma parada). 

Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí, modelar el problema utilizando 
grafos e implementar un algoritmo que determine el mínimo valor k para resolver el problema. Indicar la complejidad del algoritmo implementado.

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

# ============================================================================
# EJ 18
'''
Implementar un algoritmo que, por backtracking, obtenga la cantidad total de posibles ordenamientos topológicos de un grafo dirigido y acíclico.

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

def cant_ordenes(grafo, vertices, visitados):
	if len(vertices) == len(visitados):
		return 1
	
	cont = 0
	for vertice in vertices:
		if vertice not in visitados:
			predecesores = []
			for posible_predecesor in vertices:
				if vertice in grafo.adyacentes(posible_predecesor):
					predecesores.append(posible_predecesor)

			todos_predecesores_visitados = True
			for predecesor in predecesores:
				if predecesor not in visitados:
					todos_predecesores_visitados = False
					break

			if todos_predecesores_visitados:
				visitados.append(vertice)
				cont += cant_ordenes(grafo, vertices, visitados)
				visitados.pop()

	return cont

def contar_ordenamientos(grafo):
	vertices = grafo.obtener_vertices()
	return cant_ordenes(grafo, vertices, [])