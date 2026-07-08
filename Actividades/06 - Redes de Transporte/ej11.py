'''
Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca. La biblioteca tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes. Implementar un algoritmo que nos permita obtener la forma de asignar libros a alumnos de tal forma que la cantidad de préstamos sea máxima. Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue la máxima cantidad de préstamos. ¿Cuál es el orden temporal de la solución implementada?

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

'''
Este problema se puede modelar creando una red de flujo de modo tal que la fuente se comunique con los libros, mediante una arista de flujo 3 (ya que son 3 las copias maximas por cada libro), luego los libros a los alumnos (si es que el alumno quiere ese libro) mediante una arista de flujo 1 (ya que cada alumno puede pedir una copia sola de cada libro), y cada alumno tiene una arista de flujo 10 al sumidero (siendo la cantidad maxima de libros que puede solicitar).
'''

from ff import flujo
from grafo import Grafo

def crear_grafo(alumnos, libros, f, s):
	grafo = Grafo(True, alumnos.keys())
	grafo.agregar_vertice(f)
	for l in libros:
		grafo.agregar_vertice(l)
		grafo.agregar_arista(f, l, 3)
		for a in alumnos:
			if l in alumnos[a]:
				grafo.agregar_arista(l, a)

	grafo.agregar_vertice(s)
	for a in alumnos:
		grafo.agregar_arista(a, s, 10)
	
	return grafo
    
def asig_libros(alumnos, libros):
	f = "fuente"
	s = "sumidero"
	red = crear_grafo(alumnos, libros, f, s)
	flujo_dic = flujo(red, f, s)
	alum = {}

	for (origen, destino), flujo_val in flujo_dic.items():
		if destino in alumnos and flujo_val > 0:
			if destino not in alum:
				alum[destino] = []
			alum[destino].append(origen)
	
	return alum

'''
Complejidad:
	- O(l * a), siendo l la cantidad de libros y a la cantidad de alumnos.
	- O(E * F) -> Ford-Fulkerson
Por lo que resulta en:
	O(E * F)
'''