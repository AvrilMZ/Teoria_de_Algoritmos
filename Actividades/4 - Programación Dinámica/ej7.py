'''
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.

Implementar un algoritmo que, por programación dinámica, reciba los valores y pesos de los elementos, y devuelva qué elementos deben 
ser guardados para maximizar la ganancia total.

Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
Para este problema tenemos dos posibilidades:
	i. Agregar el elemento a la mochila, achicando la brecha con el peso maximo e incrementando el valor.
	ii. No agregar el elemento y seguir con el siguiente.
Dados estos casos podemos plantear la ecuacion de recurrencia con una matriz:
	OPT[n][W] = max(OPT[n - 1][W - peso(OPT[n][W])] + valor(OPT[n][W]), OPT[n - 1][W])
Donde se elije siempre el valor maximo entre agregar el elemento o no, siempre y cuando, al agregar el elemento, no nos estemos pasando de la capacidad W de la mochila.
'''

def crear_opt(elementos, W):
	OPT = [[0] * (W + 1) for _ in range(len(elementos) + 1)]

	for i in range(1, len(elementos) + 1):
		valor, peso = elementos[i - 1]
		for w in range(W + 1):
			if peso <= w:
				OPT[i][w] = max(OPT[i - 1][w], OPT[i - 1][w - peso] + valor)
			else:
				OPT[i][w] = OPT[i - 1][w]
				
	return OPT

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
	OPT = crear_opt(elementos, W)
	res = []
	w = W
	for i in range(len(elementos), 0, -1):
		if OPT[i][w] != OPT[i - 1][w]:
			res.append(elementos[i - 1])
			w -= elementos[i - 1][1]
	res.reverse()
	return res

'''
Complejidad:
	- Crear la matriz optima es O(n * W) donde n es la cantidad de elementos y W el peso maximo de la mochila.
	- Recostruir la solucion es O(n) dado que se recorre el arreglo de elementos obteniendo su elemento correspondiente en OPT.
	- Dar vuelta el arreglo: O(n)
Por lo que la complejidad final es:
	O(n * W) + O(n) + O(n) = O(n * W)
'''