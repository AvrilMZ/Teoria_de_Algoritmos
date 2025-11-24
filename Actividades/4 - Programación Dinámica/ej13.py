'''
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse.

Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar y justificar la complejidad del algoritmo.
'''

'''
Suponiendo que ya hay m lugares ocupados en la mesa, para el siguiente grupo con i integrantes puedo:
	i. Agregar el grupo a la mesa, achicando la brecha con la cantidad maxima de lugares disponibles.
	ii. No agregar el grupo a la mesa, quedandome con la cantidad previa.
Por lo que podriamos plantear la ecuacion de recurrencia con una matriz de indice_grupo por cantidad_lugares:
	OPT[i][w] = max(OPT[i - 1][w - cant_lugares(OPT[i][w])] + cant_lugares(OPT[i][w]), OPT[i - 1][w])
donde se busca el maximo de lugares ocupados, siempre y cuando no supere W.
'''

def crear_opt(P, W):
	OPT = [[0] * (W + 1) for _ in range(len(P) + 1)]
	for i in range(1, len(P) + 1):
		for j in range(0, W + 1):
			if P[i - 1] <= j:
				OPT[i][j] = max(OPT[i - 1][j - P[i - 1]] + P[i - 1], OPT[i - 1][j])
			else:
				OPT[i][j] = OPT[i - 1][j]
	return OPT

def bodegon_dinamico(P, W):
	OPT = crear_opt(P, W)
	res = []
	w = W
	for grupo in range(len(P), 0, -1):
		if w == 0:
			break
		if OPT[grupo][w] != OPT[grupo - 1][w]:
			res.append(P[grupo - 1])
			w -= P[grupo - 1]
	res.reverse()
	return res

'''
Complejidad:
	- Matriz OPT: O(n * m) siendo n la cantiadad de grupos y m la cantidad maxima de lugares en la mesa.
	- Reconstruir solucion: O(n)
	- Invertir la solucion: O(n)
Por lo tanto la complejidad es:
	O(n * m) + O(n) + O(n) = O(n * m)
'''