'''
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las 
charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. 
Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def es_charla_apta(charla, anterior):
	return anterior[1] < charla[0]

def charlas(horarios):
	ordenados = sorted(horarios, key=lambda x: x[1])
	a_dar = []
	for charla in ordenados:
		if len(a_dar) == 0 or es_charla_apta(charla, a_dar[-1]):
			a_dar.append(charla)
	return a_dar

'''
Inicialmente tenemos un arreglo de tuplas que se ordena mediante sus horarios de finalizacion, utilizando un `sorted()` de complejidad O(n*log(n)).
Luego se realiza un recorrido por el arreglo de `n` horarios comparando si el horario de finalizacion del anterior es mayor al horario de inicio
del actual, para asi determinar si se superponen, en caso de no ocurrir se agrega a el arreglo de charlas a dar.
Dado a que ordenamos el arreglo y luego se recorre nuevamente realizando una comparacion constante resultamos en una complejidad de:
	O(n*log(n)) + O(n) = O(n*log(n))
'''