'''
Hacer un seguimiento de obtener el flujo máximo en la siguiente red de transporte, realizando las modificaciones previas que fueran necesarias. 
Luego, definir cuáles son los dos conjuntos del corte mínimo en dicha red.
'''

def obtener_flujo():
    flujo = {}
    vertices = "super_fuente", "S", "T", "U", "V", "W", "X", "Z"
    flujo[("super_fuente", "S")] = 6 # Segun las pruebas aca iria 7, pero no entiendo ya que la misma cantidad de entrada deberia ser que la de salida.
    flujo[("super_fuente", "X")] = 3
    flujo[("S", "V")] = 3
    flujo[("S", "U")] = 3
    flujo[("V", "T")] = 3
    flujo[("V", "W")] = 0
    flujo[("W", "T")] = 6
    flujo[("U", "W")] = 6
    flujo[("X", "Z")] = 3
    flujo[("Z", "W")] = 0
    flujo[("Z", "U")] = 3
    flujo[("U", "Z")] = 0

    conjunto_super_fuente = ["S", "X", "super_fuente"]
    conjunto_sumidero = ["V", "W", "T"]

    return flujo, conjunto_super_fuente, conjunto_sumidero