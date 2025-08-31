'''
Implementar un algoritmo que dados n puntos en un plano, busque la pareja que se encuentre más cercana, por división y conquista, con un orden de complejidad mejor que O(n^2). 
Justificar la complejidad del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en tiempo mejor que O(n^2)". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''
import math

# Eje X (indice = 0) o Eje Y (indice = 1)
def merge_sort(puntos, indice):
	if len(puntos) <= 1:
		return puntos

	mid = len(puntos) // 2
	left = merge_sort(puntos[:mid], indice)
	right = merge_sort(puntos[mid:], indice)

	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i][indice] <= right[j][indice]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	result.extend(left[i:])
	result.extend(right[j:])
	return result

def distancia(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def puntos_mas_cercanos_rec(px, py):
	n = len(px)
	if n <= 3:
		min_dist = float('inf')
		par = None
		for i in range(n):
			for j in range(i + 1, n):
				d = distancia(px[i], px[j])
				if d < min_dist:
					min_dist = d
					par = (px[i], px[j])
		return par

	# Dividir el conjunto de puntos en dos mitades por X
	mid = n // 2
	Qx = px[:mid]
	Rx = px[mid:]
	x_medio = px[mid][0] # línea divisoria

	# Separar los puntos de py en Qy y Ry según la línea divisoria
	Qy, Ry = [], []
	for p in py:
		if p[0] <= x_medio:
			Qy.append(p)
		else:
			Ry.append(p)

	par_q = puntos_mas_cercanos_rec(Qx, Qy)
	par_r = puntos_mas_cercanos_rec(Rx, Ry)

	# Conseguir la pareja más cercana entre las dos mitades
	d_q = distancia(*par_q)
	d_r = distancia(*par_r)
	if d_q <= d_r:
		d = d_q
		min_pair = par_q
	else:
		d = d_r
		min_pair = par_r

	# Franja de puntos cercanos a la línea divisoria
	S = []
	for p in py:
		if abs(p[0] - x_medio) <= d:
			S.append(p)

	# Computar distancia contra los siguientes 15 puntos y quedarse con S[i] y S[j] que minimizan esa distancia
	for i in range(len(S)):
		for j in range(i + 1, min(i + 15, len(S))):
			d_pq = distancia(S[i], S[j])
			if d_pq < d:
				d = d_pq
				min_pair = (S[i], S[j])

	return min_pair

def puntos_mas_cercanos(puntos):
	px = merge_sort(puntos, 0)
	py = merge_sort(puntos, 1)
	return puntos_mas_cercanos_rec(px, py)

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Enotnces:
	T(n)=2T(n/2)+O(n) -> A>=1 y B>1
	O(n) == n^(log_2(2))
Por lo tanto la complejidad resulta en:
	O(n*log(n))
'''