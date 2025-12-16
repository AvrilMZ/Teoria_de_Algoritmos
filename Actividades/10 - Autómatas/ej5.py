'''
Implementar un Autómata Finito No Determinista que acepte las cadenas que cumplan con la expresión regular:
	((ab)+ba*)?(b*(ab)*)

Notar que la expresión es equivalente a:
	((ab)+ba*)?b*(ab)*

Como recordatorio:
	- El símbolo + indica que el símbolo anterior (o grupo, si está entre paréntesis) aparece al menos una vez (puede aparecer muchas veces, de forma contigua).
	- El símbolo ? indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer una vez, o no estar (es decir, es opcional).
	- El símbolo * indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer tantas veces como sea (puede ser ninguna o muchas) de forma contigua.

Para esto, considerar que existe el TAD/Clase Automata con las siguientes primitivas:
	- `Automata()`: para crear al autómata
	- `estado(nombre, es_inicial=False, es_final=False)`: para agregar un nuevo estado. El parámetro es_inicial determina si el nuevo estado es además el estado inicial (si ya había un estado inicial, lanzará una excepción). El parámetro es_final indica si dicho estado es un estado de finalización (False por defecto).
	- `transicion_estado(nombre1, nombre2, simbolo)`: agrega la transición de estados para el símbolo indicado.

Casos de uso:
	Caso	Cadena	Resultado
	1		Acepta
	2	ba	No acepta
	3	ababababba	Acepta
	4	abababababab	Acepta
	5	abba	Acepta
	6	abbaaaaaaa	Acepta
	7	abb	Acepta
	8	ababab	Acepta
	9	bbbbbab	Acepta
	10	aaaaaaaaa	No acepta
	11	baa	No acepta
	12	aab	No acepta
	13	bab	Acepta
	14	bbbbb	Acepta
'''

from automata import Automata

def expresion():
	a = Automata()
	
	a.estado("Q0", True, True)
	a.estado("Q1")
	a.estado("Q2")
	a.estado("Q3")
	a.estado("Q4")
	a.estado("Q5", False, True)

	a.transicion_estado("Q3", "Q0", '')
	
	# b*
	a.transicion_estado("Q0", "Q0", 'b')

	# (ab)*
	a.transicion_estado("Q0", "Q1", 'a')
	a.transicion_estado("Q1", "Q0", 'b')

    # (ab)+
	a.transicion_estado("Q1", "Q2", 'b')
	a.transicion_estado("Q2", "Q1", 'a')

	# ba*
	a.transicion_estado("Q2", "Q3", 'b')
	a.transicion_estado("Q3", "Q3", 'a')

	return a
