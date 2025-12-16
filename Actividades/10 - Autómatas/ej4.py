'''
Implementar un Autómata Finito No Determinista que acepte las cadenas que cumplan con la expresión regular:
	(aab)*(a, aba)*

Como recordatorio:
	- El símbolo * indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer tantas veces como sea (puede ser ninguna o muchas) de forma contigua.

Esta expresión acepta todas las cadenas que tengan una cantidad indefinida de aab como inicio, luego puedan tener una cantidad indefinida de a o aba (que pueden estar intercaladas). 

Para esto, considerar que existe el TAD/Clase Automata con las siguientes primitivas:
	- `Automata()`: para crear al autómata
	- `estado(nombre, es_inicial=False, es_final=False)`: para agregar un nuevo estado. El parámetro es_inicial determina si el nuevo estado es además el estado inicial (si ya había un estado inicial, lanzará una excepción). El parámetro es_final indica si dicho estado es un estado de finalización (False por defecto).
	- `transicion_estado(nombre1, nombre2, simbolo)`: agrega la transición de estados para el símbolo indicado.
'''

from automata import Automata

def expresion():
	a = Automata()
	
	a.estado("Q0", True, True)
	a.estado("Q1")
	a.estado("Q2")
	a.estado("Q3", False, True)
	a.estado("Q4", False, True)
	a.estado("Q5")
	
	# (aab)*
	a.transicion_estado("Q0", "Q1", 'a')
	a.transicion_estado("Q1", "Q2", 'a')
	a.transicion_estado("Q2", "Q4", 'b')
	a.transicion_estado("Q2", "Q4", '')

	# (a, aba)*
	a.transicion_estado("Q0", "Q3", 'a')
	a.transicion_estado("Q4", "Q1", 'a')
	a.transicion_estado("Q4", "Q3", 'a')
	a.transicion_estado("Q3", "Q3", 'a')
	a.transicion_estado("Q3", "Q5", 'b')
	a.transicion_estado("Q5", "Q3", 'a')

	return a
