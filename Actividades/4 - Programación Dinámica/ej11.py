'''
Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:
	(i) aumentar el valor del operando en 1;
	(ii) duplicar el valor del operando.

Implementar un algoritmo que, por programación dinámica, obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones). 
Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo implementado.
Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'

Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
Dado a que solo se pueden realizar dos operaciones para llegar al número k y se busca minimizar la cantidad de operaciones realizadas:
	OPT[n] = min(OPT[n - 1] + 1, OPT[n // 2] + 1)
Planteando esta ecuacion de recurrencia evaluamos, sobre el vector optimo OPT que almacena la cantidad de operaciones realizadas hasta el numero n, que camino nos conviene tomar con el fin de minimizar las operaciones.
'''

def calcular_OPT(k):
	OPT = [0] * (k + 1)
	prev = [0] * (k + 1)

	for n in range(1, k + 1):
		if n % 2 == 0:
			if OPT[n - 1] + 1 <= OPT[n // 2] + 1:
				OPT[n] = OPT[n - 1] + 1
				prev[n] = n - 1
			else:
				OPT[n] = OPT[n // 2] + 1
				prev[n] = n // 2
		else:
			OPT[n] = OPT[n - 1] + 1
			prev[n] = n - 1

	return OPT, prev

def reconstruir_operaciones(prev, k):
	ops = []
	n = k
	while n != 0:
		if prev[n] == n - 1:
			ops.append("mas1")
		else:
			ops.append("por2")
		n = prev[n]
	ops.reverse()
	return ops

def operaciones(k):
	OPT, prev = calcular_OPT(k)
	return reconstruir_operaciones(prev, k)
	
'''
Complejidad:
	- Se recorren los numeros hasta k para crear el arreglo OPT y para reconstruir las operaciones, ambas resultan en O(k).
Por lo que la complejidad es:
	O(k) + O(k) = O(k)
'''