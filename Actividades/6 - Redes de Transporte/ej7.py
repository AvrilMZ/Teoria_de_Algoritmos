'''
Hacer un seguimiento de obtener el flujo máximo en la siguiente red de transporte, realizando las modificaciones previas que fueran necesarias. Luego, definir cuáles son los dos conjuntos del corte mínimo en dicha red.

Nota sobre RPL: no hay forma de evaluar un seguimiento por esta plataforma, así que se propone rellenar los valores de flujo para las aristas existentes, y dar los dos conjuntos del corte mínimo.
'''

def obtener_flujo():
    flujo = {}
    vertices = "S", "T", "U", "V", "W", "X", "Z", "super_sumidero"
    flujo[("S", "V")] = 4
    flujo[("V", "T")] = 3
    flujo[("V", "W")] = 1
    flujo[("S", "W")] = 3
    flujo[("W", "T")] = 5
    flujo[("S", "U")] = 3
    flujo[("U", "W")] = 1
    flujo[("U", "Z")] = 2
    flujo[("Z", "X")] = 2
    flujo[("Z", "W")] = 0
    flujo[("W", "Z")] = 0
    flujo[("Z", "T")] = 0
    flujo[("T", "super_sumidero")] = 8
    flujo[("X", "super_sumidero")] = 2

    conjunto_fuente = ["S", "U", "V"]
    conjunto_super_sumidero = ["T", "X", "super_sumidero"]

    return flujo, conjunto_fuente, conjunto_super_sumidero