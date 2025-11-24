'''
Sea una matriz A de tamaño `n * n`, con todos valores distintos. Un índice (i,j) es un máximo local si A[i,j] es estrictamente mayor que todos su vecinos que existan (arriba, abajo, izquierda, derecha). 

Implementar un algoritmo de División y Conquista que permita encontrar algún máximo local en tiempo O(n). Justificar adecuadamente la complejidad del algoritmo. Prestar mucha atención a la ecuación de recurrencia escrita, ya que esto puede develar un error en el algoritmo planteado.
'''

def es_max(matriz, pos):
	f, c = pos
	if matriz[f - 1][c] > matriz[f][c]: # arriba
		return matriz[f - 1][c]
	if matriz[f + 1][c] > matriz[f][c]: # abajo
		return matriz[f + 1][c]
	if matriz[f][c - 1] > matriz[f][c]: # izquiera
		return matriz[f][c - 1]
	if matriz[f][c + 1] > matriz[f][c]: # derecha
		return matriz[f][c + 1]
	return pos

def buscar_max(matriz, inicio_c, fin_c):
	medio = (inicio_c + fin_c) // 2

	val_max = float('-inf')
	i_max = 0
	for i in range(len(matriz)):
		if matriz[i][medio] > val_max:
			i_max = i
			val_max = matriz[i][medio]
			
	x_max, y_max = es_max(matriz, (i_max, medio))
	if (x_max, y_max) == (i_max, medio):
		return (i_max, medio)
	if y_max > medio:
		return buscar_max(matriz, medio + 1, fin_c)
	return buscar_max(matriz, inicio_c, medio - 1)

def max_local(matriz):
	if len(matriz) == 1:
		return (0, 0)
	return buscar_max(matriz, 0, len(matriz))

'''
Teniendo en cuenta el teorema maestro:
	T(n) = A T(n/B) + O(f(n)) -> A >= 0, B > 0
Donde en este caso tenemos:
	- A (cantidad de llamadas recursivas) = 1
	- B (por cuanto se divide el problema) = 2
	- O(f(n)) (costo de procesamiento) = O(n) -> recorrer la columna buscando el máximo
Por lo tanto:
	T(n) = 1 T(n/2) + O(n)
	O(n) > n^{log_2(1)}
Resultando en una complejidad de:
	O(n)
''' 