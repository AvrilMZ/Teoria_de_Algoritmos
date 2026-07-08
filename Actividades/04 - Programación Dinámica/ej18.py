'''
Dado un número n, indicar la cantidad más económica (con menos términos) de escribirlo como suma de cuadrados perfectos, utilizando Programación Dinámica. Indicar y justificar la complejidad del algoritmo implementado.

Aclaración: siempre es posible escribir a n como suma de n términos de 1^2, por lo que siempre existe solución. Sin embargo, la expresión 10 = 3^2 + 1^2 es una manera más económica de escribirlo para n = 10.
'''

'''
Para este problema, como buscamos cuadrados perfectos, debemos forzar el resultado para los primeros \sqrt{n} (para que elevado a la dos no supere a n) y seleccionar aquel cuya cantidad de terminos sea la menor. Es asi que se puede plantear la ecuacion de recurrencia:
	OPT[n] = min_{1 <= i <= \sqrt{n}}(1 + OPT[n - i^2])
'''

import math

def crear_opt(n):
	OPT = [0] * (n + 1)
	OPT[1] = 1
	for i in range(1, n + 1):
		minimo = i
		for j in range(1, int(math.sqrt(i)) + 1):
			cuad = 1 + OPT[i - j**2]
			if cuad < minimo:
				minimo = cuad
		OPT[i] = minimo
	return OPT

def terminos(n):
	if n == 0:
		return 0
	OPT = crear_opt(n)
	return OPT[n]

'''
Complejidad:
	- Dado a que por cada indice hasta n se recorren todos los posibles resultados hasta \sqrt{n}, la complejidad es O(n * \sqrt{n}).
'''