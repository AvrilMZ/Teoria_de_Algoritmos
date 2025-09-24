'''
Tenemos un conjunto de números v_1, v_2, …, v_n, y queremos obtener un subconjunto de todos esos números tal que su suma sea igual o menor a un valor V, tratando de aproximarse lo más posible a V. 

Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores, y la suma objetivo V, y devuelva qué elementos deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
Para este problema tenemos dos posibilidades por iteracion:
	i. Agregar el valor y achicar la brecha con V.
	ii. Saltear el valor y quedarme con el valor previo.
Teniendo en cuenta esto se puede plantear la ecuacion de recurrencia sobre una matriz:
	OPT[i][v] = max(OPT[i - 1][v - valor(OPT[i][v])] + valor(OPT[i][v]), OPT[i - 1][v])
Siendo i el indice del valor y v el valor. Esto es siempre y cuando no se supere el valor de V.
'''

def crear_opt(elementos, v):
	OPT = [[0] * (v + 1) for _ in range(len(elementos) + 1)]
	for i in range(1, len(elementos) + 1):
		for j in range(1, v + 1):
			if elementos[i - 1] <= j:
				OPT[i][j] = max(OPT[i - 1][j - elementos[i - 1]] + elementos[i - 1], OPT[i - 1][j])
			else:
				OPT[i][j] = OPT[i - 1][j]
	return OPT

def subset_sum(elementos, v):
	if len(elementos) == 0:
		return []
	OPT = crear_opt(elementos, v)
	res = []
	actual = v
	for i in range(len(elementos), 0, -1):
		if OPT[i][actual] != OPT[i - 1][actual]:
			res.append(elementos[i - 1])
			actual -= elementos[i - 1]
	res.reverse()
	return res

'''
Complejidad:
	- Crear la matriz optima es O(n * V) donde n es la cantidad de elementos y V el valor maximo.
	- Recostruir la solucion es O(n) dado que se recorre el arreglo de elementos obteniendo su elemento correspondiente en OPT.
	- Dar vuelta el arreglo: O(n)
Por lo que la complejidad final es:
	O(n * W) + O(n) + O(n) = O(n * W)
'''