'''
El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima cantidad de sus n socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas. 
Dada un lista de tuplas (duplas) de personas que se conocen:
	a. Nos solicitan seleccionar el mayor número posible de invitados. Proponer una estrategia greedy óptima para resolver el problema.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.

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

def definir_conexiones(conocidos):
	conexiones = {}
	for a, b in conocidos:
		if a not in conexiones:
			conexiones[a] = set()
		if b not in conexiones:
			conexiones[b] = set()
		conexiones[a].add(b)
		conexiones[b].add(a)
	return conexiones
			
# conocidos: lista de pares de personas que se conocen, cada elemento es un (a,b)
def obtener_invitados(conocidos):
	if len(conocidos) == 0:
		return []
	
	conexiones = definir_conexiones(conocidos)
	seguir = True
	while seguir:
		eliminados = False
		for persona in list(conexiones.keys()):
			if len(conexiones[persona]) < 4:
				for otros in conexiones.values():
					otros.discard(persona)
				conexiones.pop(persona)
				eliminados = True
				break
		if not eliminados:
			seguir = False

	return list(conexiones.keys())