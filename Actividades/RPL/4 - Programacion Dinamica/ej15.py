'''
Dada una soga de n metros (n mayor o igual a 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El algoritmo debe devolver el valor del producto máximo alcanzable. Tener en cuenta que la soga puede cortarse varias veces, como se muestra en el ejemplo con n = 10. Indicar y justificar la complejidad del algoritmo.

Ejemplos:
	n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
	n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
	n = 4 --> Debe devolver 4 (producto máximo es 2 * 2)
	n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
	n = 6 --> Debe devolver 9 (producto máximo es 3 * 3)
	n = 7 --> Debe devolver 12 (producto máximo es 3 * 4)
	n = 10 --> Debe devolver 36 (producto máximo es 3 * 3 * 4)

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
Para este problema tenemos dos opciones por cada iteracion:
	i. Cortar la soga
	ii. No cortar la soga
Dadas estas opciones podemos plantear la ecuacion de recurrencia como:
	OPT[i] = max(OPT[i - 1] * OPT[i - 1], OPT[i - 1])
'''

def problema_soga(n):
	if n <= 1:
		return 0
	elif n == 2:
		return 1
	
	return 0