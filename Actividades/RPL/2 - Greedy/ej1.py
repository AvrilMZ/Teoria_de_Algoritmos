'''
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las 
charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. 
Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def charlas_superpuestas(anterior, nueva):
	return anterior[1] > nueva[0]

def charlas(horarios):
	horarios_ordenados = sorted(horarios, key=lambda rango: rango[1])
	charlas = []
	for horario in horarios_ordenados:
		if len(charlas) == 0 or not charlas_superpuestas(charlas[-1], horario):
			charlas.append(horario)
	return charlas

'''
Inicialmente tenemos un arreglo de tuplas que se ordena mediante sus horarios de finalizacion, utilizando un `sorted()` de complejidad O(n*log(n)).
Luego se realiza un recorrido por el arreglo de `n` horarios comparando si el horario de finalizacion del anterior es mayor al horario de inicio
del actual, para asi determinar si se superponen, en caso de no ocurrir se agrega a el arreglo de charlas a dar.
Dado a que ordenamos el arreglo y luego se recorre nuevamente realizando una comparacion constante resultamos en una complejidad de:
	O(n*log(n)) + O(n) = O(n*log(n))
'''