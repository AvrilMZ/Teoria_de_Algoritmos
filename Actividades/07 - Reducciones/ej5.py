'''
Para cada uno de los siguientes problemas, implementar un verificador polinomial y justificar su complejidad.
	a. Dado un número por parámetro, si es la solución al problema de búsqueda del máximo en un arreglo.
	b. Dado un arreglo, si es la solución a tener el arreglo ordenado.
	c. Dadas un arreglo de posiciones de reinas, si es la solución de colocar al menos N-reinas en un tablero NxN.
'''

# a.
def verificador_num_max(arr, max):
	if max not in arr:
		return False
	
	for n in arr:
		if n > max:
			return False
		
	return True

'''
Complejidad:
	- O(n), dado que se recorre verificando si existe un numero mayor al dado.
'''

# b.
def verificador_ordenado(arr):
	for i in range(1, len(arr)):
		if arr[i] < arr[i - 1]:
			return False
	return True

'''
Complejidad:
	- O(n), dado que se recorre una vez sola verificando el si existe un numero menor a un anterior.
'''

# c.
def verificador_nreinas(posiciones, n):
	for i in range(posiciones):
		fil, col = posiciones[i]
		if fil > n or fil < 0:
			return False
		if col > n or col < 0:
			return False
		for j in range(posiciones):
			if j == i:
				continue
			f, c = posiciones[j]
			if f == fil or c == col:
				return False
			# me falta verificar diagonales
	return True

'''
Complejidad:
	- O(n^2), dado que por cada reina puesta se verifica si existe otra que pueda ser eliminada.
'''