'''
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. 
Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes.

Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores del sistema monetario, y la cantidad de cambio 
objetivo a dar, y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. 
Indicar y justificar la complejidad del algoritmo implementado.
'''

'''
En este problema podemos tomar dos decisiones sobre cada iteracion:
	i. Uso la moneda y achico la brecha con el monto maximo.
	ii. Descarto la moneda y sigo con el monto anterior.
Por lo que podemos plantear la ecuacion de recurrencia con una matriz OPT de modo tal que:
	OPT[i][M] = min(OPT[i - 1][M - monto(OPT[i][M])] + 1), OPT[i - 1][M])
donde i define la cantidad de monedas y M el monto.

Tambien podemos plantear una ecuacion de recurrencia en forma de arreglo:
	OPT[M] = min(OPT[M - monto(OPT[M])] + 1, OPT[M])
donde M es el monto.

En ambos casos, si se usa la moneda se suma uno para incrementar la cantidad total utilizada.
'''

def crear_opt(monedas, monto):
	OPT = [0] * (monto + 1)
	monedas_usadas = [0] * (monto + 1)
	for i in range(1, monto + 1):
		minimo = i
		moneda_usada = 1
		for moneda in monedas:
			if moneda <= i:
				cantidad = 1 + OPT[i - moneda]
				if cantidad < minimo:
					minimo = cantidad
					moneda_usada = moneda
		OPT[i] = minimo
		monedas_usadas[i] = moneda_usada
	return OPT, monedas_usadas

def reconstruccion(monedas_usadas, monto):
	res = []
	i = monto
	while i > 0:
		moneda = monedas_usadas[i]
		if moneda == 0:
			return []
		res.append(moneda)
		i -= moneda
	return res

def cambio(monedas, monto):
	if monto == 0 or len(monedas) == 0:
		return []
	
	OPT, monedas_usadas = crear_opt(monedas, monto)
	return reconstruccion(monedas_usadas, monto)

'''
Complejidad:
	- Por cada valor de OPT (de logitud monto) se recorren todas las monedas minimizando la cantidad de monedas hasta el monto: O(n * m), siendo n los valores del arreglo y m las monedas del sistema monetario.
	- Reconstruccion: O(n), dado que como maximo recorre todos los valores desde monto hasta cero.
Por lo que la complejidad en tiempo resulta en:
	O(n * m)
'''