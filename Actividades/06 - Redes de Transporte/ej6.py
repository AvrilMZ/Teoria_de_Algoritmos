'''
Hacer un seguimiento de obtener el flujo máximo en la siguiente red de transporte, realizando las modificaciones previas que fueran necesarias. 
Luego, definir cuáles son los dos conjuntos del corte mínimo en dicha red.
'''

def obtener_flujo():
	flujo = {}
	vertices = "super_fuente", "S", "T", "U", "V", "W", "X", "Z"
	flujo[("super_fuente", "S")] = 7
	flujo[("super_fuente", "X")] = 2
	flujo[("S", "V")] = 4
	flujo[("S", "U")] = 3
	flujo[("V", "T")] = 3
	flujo[("V", "W")] = 1
	flujo[("W", "T")] = 6
	flujo[("U", "W")] = 4
	flujo[("X", "Z")] = 2
	flujo[("Z", "W")] = 1
	flujo[("Z", "U")] = 1
	flujo[("U", "Z")] = 0

	conjunto_super_fuente = ["super_fuente", "S", "U", "V", "W", "X", "Z"]
	conjunto_sumidero = ["T"] # Complemento de conjunto super fuente

	return flujo, conjunto_super_fuente, conjunto_sumidero