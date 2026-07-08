'''
Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar, utilizando programación dinámica, cuántas formas diferentes hay de subir la escalera hasta el paso n. Indicar y justificar la complejidad del algoritmo implementado.

Ejemplos:
	n = 0 --> Debe devolver 1 (no moverse)
	n = 1 --> Debe devolver 1 (paso de 1)
	n = 2 --> Debe devolver 2 (dos pasos de 1, o un paso de 2)
	n = 3 --> Debe devolver 4 (un paso de 3, o tres pasos de 1, o un paso de 2 y uno de 1, o un paso de 1 y un paso de 2)
	n = 4 --> Debe devolver 7
	n = 5 --> Debe devolver 13
'''

'''
Podemos plantear desde un escalon n:
	i. Subo por (n - 1)
	ii. Subo por (n - 2)
	iii. Subo por (n - 3)
En cualquiera de los 3 casos debo contabilizar la cantidad de formas que habia hasta llegar al escalon anterior, por lo que:
	OPT[n] = OPT[n - 1] + OPT[n - 2] + OPT[n - 3]
'''

def contar_formas(OPT, n):
	return OPT[n - 1] + OPT[n - 2] + OPT[n - 3]

def escalones(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	
	OPT = [1,1,2]
	for escalon in range(3, n + 1):
		cant_n = contar_formas(OPT, escalon)
		OPT.append(cant_n)

	return OPT[n]

'''
Complejidad:
Dado a que secuencialmente por escalon se cuentan las formas la complejidad resulta:
	O(n)
donde n es la cantidad de escalones.
'''