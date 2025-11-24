'''
Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci. Indicar y justificar la complejidad del algoritmo implementado.

Definición:
	n = 0 --> Debe devolver 1
	n = 1 --> Debe devolver 1
	n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)
'''

def fibonacci(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	return fibonacci(n - 2) + fibonacci(n - 1)

'''
Complejidad:
	La ecuacion de recurrencia es:
		T(n) = T(n - 1) + T(n - 2) + O(1)
	Por lo que se tienen dos llamadas recursivas por invocacion en el peor de los casos, esto implica:
		O(2**n)
'''