'''
Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta Ci. También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos Gi. 

Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos. Indicar y justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda? Por ejemplo, si una campaña cuesta 100 dólares, para pasar a pesos se debe hacer la conversión de divisa.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

'''
Para el problema presentado tenemos las opciones:
	i. Elegir la campaña, achicando la brecha con el presupuesto total. (esta opcion implica que el costo (C) no debe ser mayor a la ganancia (G) ni superar el presupuesto (P))
	ii. No elegirla y mantener el presupuesto igual pasando a evaluar la siguiente.
Dado esto, podemos plantear la ecuacion de recurrencia:
	OPT[i][p] = max(OPT[i - 1][p - gasto(campañas[i])] + ganancia(campañas[i]), OPT[i - 1][p])
donde se busca maximizar la ganancia de las camapañas elegidas.
'''

def crear_opt(c_publicitaria, P):
	OPT = [[0] * (P + 1) for _ in range(len(c_publicitaria) + 1)]
	for i in range(1, len(c_publicitaria) + 1):
		for j in range(1, P + 1):
			if c_publicitaria[i - 1][1] <= j:
				OPT[i][j] = max(OPT[i - 1][j - c_publicitaria[i - 1][1]] + c_publicitaria[i - 1][0], OPT[i - 1][j])
			else:
				OPT[i][j] = OPT[i - 1][j]
	return OPT

def reconstruccion(OPT, c_publicitaria, P):
	res = []
	p = P
	for i in range(len(c_publicitaria), 0, -1):
		if OPT[i][p] != OPT[i - 1][p]:
			res.append(c_publicitaria[i - 1])
			p -= c_publicitaria[i - 1][1]
	res.reverse()
	return res

# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
	if len(c_publicitaria) == 0:
		return []
	
	OPT = crear_opt(c_publicitaria, P)
	return reconstruccion(OPT, c_publicitaria, P)

'''
Complejidad:
	- Crear OPT: O(n * m), donde n es la cantidad de campañas y m la cantidad de presupuesto.
	- Reconstruccion: O(n) + O(n) = O(n), por recorrer el largo de las campañas y luego dar vuelta la solucion.
Por lo que la complejidad en tiempo es:
	O(n * m)
'''