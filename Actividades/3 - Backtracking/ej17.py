'''
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.

Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”).
'''

def comparten_area(submarino, faro):
	x1, y1 = submarino
	x2, y2 = faro
	return (x2 - 2 <= x1 <= x2 + 2) and (y2 - 2 <= y1 <= y2 + 2)

def buscar_submarinos(matriz):
	submarinos = set()
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if matriz[i][j]:
				submarinos.add((i, j))
	return submarinos

def buscar_cobertura(fil, col, submarinos):
	cobertura = set()
	for i in range(fil - 2, fil + 3):
		for j in range(col - 2, col + 3):
			if (i, j) in submarinos:
				cobertura.add((i, j))
	return cobertura

def colocar_faros(matriz, submarinos, parcial, indice, minima):
	if len(submarinos) == 0:
		return parcial.copy()
	elif indice == len(matriz) * len(matriz[0]):
		return None
	elif minima and len(parcial) >= len(minima):
		return minima

	f = indice // len(matriz[0])
	c = indice % len(matriz[0])

	cobertura = buscar_cobertura(f, c, submarinos)

	agregado = None
	if len(cobertura) != 0:
		parcial.append((f, c))
		submarinos.difference_update(cobertura)
		agregado = colocar_faros(matriz, submarinos, parcial, indice + 1, minima)
		submarinos.update(cobertura)
		parcial.pop()
		if agregado and (not minima or len(agregado) < len(minima)):
			minima = agregado

	salteado = colocar_faros(matriz, submarinos, parcial, indice + 1, minima)
	if salteado and (not minima or len(salteado) < len(minima)):
		minima = salteado

	if agregado and (not salteado or len(agregado) < len(salteado)):
		return agregado
	elif salteado:
		return salteado
	else:
		return None

def submarinos(matriz):
	subs = buscar_submarinos(matriz)
	resultado = colocar_faros(matriz, subs, [], 0, None)
	if resultado:
		return resultado
	return []

'''
Complejidad:
	- 'colocar_faros()' por cada submarino pendiente verifica cobertura en O(s), donde s es el número de submarinos restantes, y la función se llama recursivamente O(2^(n*m)).
Por lo que la complejidad final es:
	O(2^(n * m) * s)
'''