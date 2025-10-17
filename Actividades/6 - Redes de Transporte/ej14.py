'''
Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más clubes, y de exactamente 1 partido político. Cada grupo de interés debe nombrar a un representante ante la nueva comisión de actividades culturales, con las siguientes restricciones: 
	- cada partido político no puede tener más de n/2 simpatizantes en la comisión;
	- cada persona puede representar a solo un club;
	- cada club debe estar representado por un miembro.

Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a qué partido pertenecen), nos dé una lista de representantes válidos (Para RPL, lo volvemos diccionario para que el orden no afecte los resultados de las pruebas, y poder consultar fácilmente). Indicar y justificar la complejidad del algoritmo implementado.

Considerar que la función flujo(red) que implementa el algoritmo de Ford-Fulkerson (usando BFS, definida por Edmonds y Karp) ya se encuentra implementada, y devuelve un diccionario con la asignación de flujo que pasa por cada arista de la red definida.

Información de los miembros:
Cada miembro tiene los siguientes campos:
	miembro: {
		nombre: string con el nombre del miembro
		clubes: lista con los nombres (strings) de los clubes a los que pertenece
		partido_politico: nombre (string) del partido político al que está afiliado
	}
Se puede asumir que cada club tiene al menos un miembro asociado.

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

La función flujo recibe la red de transporte (debe cumplir con las propiedades de red de transporte), la fuente y el sumidero, en ese orden.
Devuelve un diccionario Arista -> flujo. 
'''

from ff import flujo
from grafo import Grafo

def crear_red(miembros, s, t):
	grafo = Grafo(True)
	t_clubes = []
	t_pp = []

	for miembro in miembros:
		grafo.agregar_vertice(miembro.nombre)

		vertices = grafo.obtener_vertices()
		for club in miembro.clubes:
			if club not in vertices:
				grafo.agregar_vertice(club)
				t_clubes.append(club)
			grafo.agregar_arista(club, miembro.nombre)
		
		if miembro.partido_politico not in vertices:
			grafo.agregar_vertice(miembro.partido_politico)
			t_pp.append(miembro.partido_politico)
		grafo.agregar_arista(miembro.nombre, miembro.partido_politico)

	grafo.agregar_vertice(s)
	grafo.agregar_vertice(t)

	for club in t_clubes:
		grafo.agregar_arista(s, club)

	for pp in t_pp:
		grafo.agregar_arista(pp, t)

	return grafo

# devolver un diccionario NombreRepresentante -> NombreClubRepresentado
# si no se puede resolver dadas las características del problema, devolver None
def representantes(miembros):
	s = "fuente"
	t = "sumidero"
	grafo = crear_red(miembros, s, t)
	flujo_dic = flujo(grafo, s, t)
	rep = {}

	clubes = {club for miembro in miembros for club in miembro.clubes}
	for arista in flujo_dic:
		if arista[0] in clubes and flujo_dic[arista] == 1:
			rep[arista[1]] = arista[0]

	return rep

# FALTAN LAS RESTRINCCIONES (MIRAR TESTS FALLIDOS)