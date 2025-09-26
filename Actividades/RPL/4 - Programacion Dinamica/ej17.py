'''
Dado un número n, indicar la cantidad más económica (con menos términos) de escribirlo como suma de cuadrados perfectos, utilizando Programación Dinámica. Indicar y justificar la complejidad del algoritmo implementado.

Aclaración: siempre es posible escribir a n como suma de n términos de 1^2, por lo que siempre existe solución. Sin embargo, la expresión 10 = 3^2 + 1^2 es una manera más económica de escribirlo para n=10

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def terminos(n):
	return 0