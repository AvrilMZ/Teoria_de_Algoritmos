'''
Implementar un Autómata Finito Determinista que describa al Lenguaje que acepta todos las cadenas de 0 y 1s tales que dicho input termine con al menos tres 0s.

Para esto, considerar que existe el TAD/Clase Automata con las siguientes primitivas:
	- `Automata()`: para crear al autómata
	- `estado(nombre, es_inicial=False, es_final=False)`: para agregar un nuevo estado. El parámetro es_inicial determina si el nuevo estado es además el estado inicial (si ya había un estado inicial, lanzará una excepción). El parámetro es_final indica si dicho estado es un estado de finalización (False por defecto).
	- `transicion_estado(nombre1, nombre2, simbolo)`: agrega la transición de estados para el símbolo indicado.
'''

from automata import Automata

def automata_al_menos_3_0s():
	a = Automata()

	a.estado("Q0", True)
	a.estado("Q1")
	a.estado("Q2")
	a.estado("Q3", False, True)

	a.transicion_estado("Q0", "Q0", "1")
	a.transicion_estado("Q0", "Q1", "0")
	a.transicion_estado("Q1", "Q0", "1")
	a.transicion_estado("Q1", "Q2", "0")
	a.transicion_estado("Q2", "Q0", "1")
	a.transicion_estado("Q2", "Q3", "0")
	a.transicion_estado("Q3", "Q0", "1")
	a.transicion_estado("Q3", "Q3", "0")

	return a