'''
Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

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

def son_iso(g1, g2, v1, parcial, nuevo_v2):
	for i in range(len(parcial)):
		if g1.estan_unidos(v1[i], v1[len(parcial)]) != g2.estan_unidos(parcial[i], nuevo_v2): # v1[len(parcial)] deberia ser igual a nuevo_v2 y obviamente los incluidos previamente en parcial deberian coincidir con los de v1 (parcial[i] deberia ser igual a v1[i]). Se verifica la union con todos los vertices ya que si el nuevo tendria otra arista a algunos de los vertices ya puestos deberia estar para ambos.
			return False
	return True

def detectar_iso(g1, g2, v1, v2, parcial):
	if len(parcial) == len(v1):
		return True
	
	for v in v2:
		if v not in parcial and son_iso(g1, g2, v1, parcial, v):
			parcial.append(v)
			if detectar_iso(g1, g2, v1, v2, parcial):
				return True
			parcial.pop()
	
	# No se realiza la llamada recursiva donde se saltea el vertice ya que si se lo saltea significa que difiere del otro grafo, por lo que no seria un isomorfismo.

	return False

def hay_isomorfismo(g1, g2):
	if len(g1) != len(g2):
		return False
	ver1 = g1.obtener_vertices()
	ver2 = g2.obtener_vertices()
	return detectar_iso(g1, g2, ver1, ver2, [])