'''
Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto, es la de maximizar la ganancia dada por p[k] - p[j]. 

Implementar un algoritmo de programación dinámica que permita resolver el problema de Osvaldo. Indicar y justificar la complejidad del algoritmo implementado.
'''

'''
En este problema me tengo que forzar a comprar en todos los dias hasta n - 1 y forzar a vender en los subsecuentes, para luego verificar en cual tengo la ganancia maxima:
	OPT[n] = max(0, OPT[n - 1] + P(n) - P(n - 1))
donde P(i) - P(i - 1) calcula la diferencia entre el dia de compra y venta. En otras palabras, compro y vendo el mismo dia o compre antes y verifico cuanto mejoro por no haber vendido ayer. (NO ME ANDUVO)

Otra manera seria pensar ¿vendo o no vendo hoy?:
	- La mejor solución hasta el día i - 1 (no vendo);
	- La mejor ganancia vendiendo exactamente en el día i (vendo).
Por lo que la ecuacion de recurrencia seria:
	OPT[i] = max(OPT[i - 1], p[i] - (min_precio_hasta_i - 1))
'''

def crear_opt(p):
	OPT = [0] * len(p)

	min_precio = p[0]
	min_dia = 0
	dia_compra = 0
	dia_venta = 0

	for i in range(1, len(p)):
		if p[i] - min_precio > OPT[i - 1]:
			OPT[i] = p[i] - min_precio
			if OPT[i] > OPT[dia_venta]:
				dia_compra = min_dia
				dia_venta = i
		else:
			OPT[i] = OPT[i - 1]

		if p[i] < min_precio:
			min_precio = p[i]
			min_dia = i

	return OPT, (dia_compra, dia_venta)

def compra_venta(p):
	if len(p) < 2:
		return (0, 0)
	OPT, res = crear_opt(p)
	return res

'''
Complejidad:
	- O(n), siendo n la cantidad de predicciones del arreglo.
'''