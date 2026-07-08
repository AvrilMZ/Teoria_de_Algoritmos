'''
Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud N empezando por botón del número inicial k. 

Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. 
Implementar el algoritmo por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. 

Ejemplos:
	Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)
	Para N=2, depende de cuál dígito se comienza.
	Empezando por 0, son válidos 00, 08 (cantidad: 2)
	Empezando por 1, son válidos 11, 12, 14 (cantidad: 3)
	Empezando por 2, son válidos 22, 21, 23, 25 (cantidad: 4)
	Empezando por 3, son válidos 33, 32, 36 (cantidad: 3)
	Empezando por 4, son válidos 44, 41, 45, 47 (cantidad: 4)
	Empezando por 5, son válidos 55, 52, 54, 56, 58 (cantidad: 5)
	Empezando por 6, son válidos 66, 63, 65, 69 (cantidad: 4)
	Empezando por 7, son válidos 77, 74, 78 (cantidad: 3)
	Empezando por 8, son válidos 88, 80, 85, 87, 89 (cantidad: 5)
	Empezando por 9, son válidos 99, 96, 98 (cantidad: 3)

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.

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
Dado a que no todos los vertices pueden marcar la misma cantidad de numeros siguientes podemos plantear la ecuacion de
recurrencia como:
	OPT[n][m] = \sum_{v = vecinos de m} OPT[n - 1][v]
siendo n la longitud total de combinaciones y m el valor del teclado seleccionado.
'''

from grafo import Grafo

def crear_teclado():
	grafo = Grafo(False, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

	# fila 1
	grafo.agregar_arista(1, 2, peso = 1)
	grafo.agregar_arista(2, 3, peso = 1)

	# fila 2
	grafo.agregar_arista(4, 5, peso = 1)
	grafo.agregar_arista(5, 6, peso = 1)

	# fila 3
	grafo.agregar_arista(7, 8, peso = 1)
	grafo.agregar_arista(8, 9, peso = 1)

	# verticales
	grafo.agregar_arista(1, 4, peso = 1)
	grafo.agregar_arista(2, 5, peso = 1)
	grafo.agregar_arista(3, 6, peso = 1)
	grafo.agregar_arista(4, 7, peso = 1)
	grafo.agregar_arista(5, 8, peso = 1)
	grafo.agregar_arista(6, 9, peso = 1)
	grafo.agregar_arista(8, 0, peso = 1)

	# bucles
	grafo.agregar_arista(1, 1, peso = 1)
	grafo.agregar_arista(2, 2, peso = 1)
	grafo.agregar_arista(3, 3, peso = 1)
	grafo.agregar_arista(4, 4, peso = 1)
	grafo.agregar_arista(5, 5, peso = 1)
	grafo.agregar_arista(6, 6, peso = 1)
	grafo.agregar_arista(7, 7, peso = 1)
	grafo.agregar_arista(8, 8, peso = 1)
	grafo.agregar_arista(9, 9, peso = 1)
	grafo.agregar_arista(0, 0, peso = 1)

	return grafo

def cant_combinaciones(grafo, teclas, pasos, tecla_inicial):
	cant = [[0] * len(teclas) for _ in range(pasos + 1)]

	for tecla in range(len(teclas)):
		cant[0][tecla] = 0
		cant[1][tecla] = 1

	for i in range(2, pasos + 1):
		for tecla in range(len(teclas)):
			contador = 0
			for vecino in grafo.adyacentes(tecla):
				contador += cant[i - 1][vecino]
			cant[i][tecla] = contador

	return cant[pasos][tecla_inicial]

def numeros_posibles(k, n):
	grafo = crear_teclado()
	teclas = grafo.obtener_vertices()
	return cant_combinaciones(grafo, teclas, n, k)

'''
Complejidad:
- Crear el grafo es O(m + k) siendo m la cantidad de digitos del teclado y k la cantidad de aristas agregadas.
- Crear la matriz de cantidad de combinaciones cuesta O(n * (m * g)), siendo n la cantidad de combinaciones esperadas,
m la cantidad de digitos en el teclado, y g la cantidad de vecinos que se contabilizan por cada m.
Por lo tanto la complejidad final resulta en:
	O(n * (m * g))
'''