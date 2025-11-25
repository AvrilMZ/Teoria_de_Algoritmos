'''
Se sabe que existe la equivalencia e = \sum_{i=0}^{\inf} \frac{1}{n!}​, siendo e el número de Euler. Sabiendo esto, podemos aproximar el valor de e sumando los primeros n términos de dicha serie. Un algoritmo trivial puede obtener esto en O(n^2). Implementar un algoritmo que, utilizando programación dinámica, permita obtener dicha aproximación en tiempo lineal.
'''

'''
Podemos plantear el calculo del termino n como el resultado de todos los calculados anteriormente mas el actual:
	OPT[n] = OPT[n - 1] + \frac{1}{n!}
'''

def crear_opt(n):
	OPT = [0] * (n + 1)
	OPT[0] = 1
	factorial = 1
	for i in range(1, n + 1):
		factorial *= i
		OPT[i] = OPT[i - 1] + (1 / factorial)
	return OPT

def aprox_e(n):
	OPT = crear_opt(n)
	return OPT[-1]