'''
Suponer que queremos schedulear cómo los aviones van de un aeropuerto a otro para cumplir sus horarios. Podemos decir que podemos usar un avión para un segmento/vuelo i y luego para otro j si se cumple alguna de las siguientes condiciones: 
    a. El destino de i y el origen de j son el mismo.
    b. Podemos agregar un vuelo desde el destino de i al origen de j con tiempo suficiente.

Decimos que el vuelo j es alcanzable desde el vuelo i si es posible usar el avión del vuelo i y después para el vuelo j.
Dados todos los vuelos con origen y destino, y el tiempo que tarda un avión entre cada par de ciudades queremos decidir: ¿Podemos cumplir con los m vuelos usando a lo sumo k aviones? 
Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se decide si es posible cumplir con la premisa. ¿Cuál es el orden temporal de la solución implementada?

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
Se modela similar a una red de flujo bipartita, creando una copia de todos los vuelos y realizando una union con el original si es que se cumplen los requisitos para que sea el siguiente en despegar.
'''

from ff import flujo
from grafo import Grafo

def crear_red(vuelos, f, s):
    grafo = Grafo(True, vuelos)
    grafo.agregar_vertice(f)
    grafo.agregar_vertice(s)

    for v1 in vuelos:
        origen1, destino1, tiempo1 = v1
        for v2 in vuelos:
            origen2, destino2, tiempo2 = v2
            if v1 != v2 and destino1 == origen2 and tiempo1 < tiempo2:
                grafo.agregar_vertice(v2.copy())
                grafo.agregar_arista(v1, v2)
                grafo.agregar_arista(v2, s)

    return grafo

def compatibles(vuelos, k):
    f = "fuente"
    s = "sumidero"
    red = crear_red(vuelos, f, s)
    flujo_dic = flujo(red, f, s)

    sum = 0
    for arista in flujo_dic:
        inicio, fin = arista
        if fin == s:
            sum += flujo_dic[arista]

    return True if len(vuelos) - sum <= k else False

'''
Complejidad:
    - O(n^2), siendo n la cantidad de vuelos.
'''