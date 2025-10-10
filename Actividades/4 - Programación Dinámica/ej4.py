'''
Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. 
Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. 
Hacer una reconstrucción para verificar qué días debe trabajar. Indicar y justificar la complejidad del algoritmo implementado.

Ejemplo:
Para: [100, 5, 50, 1, 1, 200]
Devolver: [0, 2, 5]

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
Si me situo en el dia n de trabajo deberia verficar el monto optimo de los dos dias anteriores y quedarme con el maximo, digamos:
	i. Trabaja el dia n y el dia n - 2 (o el dia cuya ganancia sea la maxima).
	ii. Trabaja el dia n - 1 pero no el dia n.
Por lo tanto, la ecuacion de recurrencia para conseguir la suma maxima de ganancia para el dia n es:
	OPT[n] = max(OPT[n - 2] + ganancia(n), OPT[n - 1])
Suponiendo que el dia n - 2 es el que tiene la suma maxima de ganancia hasta el momento.
'''

def calcular_pagos(trabajos):
	OPT = [0] * len(trabajos)
	OPT[0] = trabajos[0]
	OPT[1] = max(OPT[0], trabajos[1])

	for dia in range(2, len(trabajos)):
		OPT[dia] = max(OPT[dia - 2] + trabajos[dia], OPT[dia - 1])
	
	return OPT

def dias_optimos(OPT, trabajos):
	dias = []
	dia_actual = len(trabajos) - 1

	while dia_actual >= 0:
		if dia_actual > 0:
			opt_ayer = OPT[dia_actual - 1] 
		else:
			opt_ayer = 0

		if dia_actual > 1:
			opt_anteayer = OPT[dia_actual - 2]
		else:
			opt_anteayer = 0

		valor_hoy = trabajos[dia_actual]
		if valor_hoy + opt_anteayer >= opt_ayer:
			dias.append(dia_actual)
			dia_actual -= 2
		else:
			dia_actual -= 1

	dias.reverse()
	return dias

def juan_el_vago(trabajos):
	if len(trabajos) == 0:
		return []
	if len(trabajos) == 1:
		return [0]

	OPT = calcular_pagos(trabajos)
	dias = dias_optimos(OPT, trabajos)
	return dias

'''
Complejidad:
Dado que `calcular_pagos` y `dias_optimos` es O(n) la complejidad resulta en:
	O(n)
ya que `juan_el_vago` solo llama a estas funciones secuencialmente.
'''