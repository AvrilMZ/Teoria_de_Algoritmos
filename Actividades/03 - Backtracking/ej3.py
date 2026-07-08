'''
Dado un tablero de ajedrez `n * n`, implementar un algoritmo por backtracking que ubique (si es posible) a `n` reinas de tal manera que ninguna pueda comerse con ninguna.
'''

def puede_atacar_reina(reina, posicion):
	rx, ry = reina
	x, y = posicion
	if rx == x or ry == y:
		return True
	elif abs(rx - x) == abs(ry - y):
		return True
	return False

def posicion_valida(posiciones, nueva):
	for posicion in posiciones:
		if puede_atacar_reina(posicion, nueva):
			return False
	return True

def ubicar_reinas(n, fila, posiciones):
	if fila == n:
		return posiciones

	for col in range(n):
		if posicion_valida(posiciones, (fila, col)):
			posiciones.append((fila, col))
			r = ubicar_reinas(n, fila + 1, posiciones)
			if r:
				return r
			posiciones.pop()
	return []

def nreinas(n):
	posiciones = []
	return ubicar_reinas(n, 0, posiciones)