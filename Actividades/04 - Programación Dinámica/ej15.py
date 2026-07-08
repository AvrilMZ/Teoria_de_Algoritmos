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
'''

'''
Para este problema podemos plantear cortar la soga en una posicion i tal que 1 <= i <= n - 1, entonces ahora debemos tomar la decision de:
	i. Cortar más algún segmento de la soga (usar el OPT del segmento);
	ii. No cortar más ninguna parte, usando su optimo actual (usar la longitud tal cual).
Osea, como buscamos el producto maximo:
	max(i, OPT[i]) * max(i - 1, OPT[i - 1]) -> (producto maximo del primer segmento) * (producto maximo del segundo segmento)
Luego debemos forzar todos los cortes de i para luego decidir cual es el que maximiza:
	OPT[n] = max_{1 ≤ i ≤ n - 1}(max(i, OPT[i]) * max(i - 1, OPT[i - 1]))
'''

def crear_opt(n):
	OPT = [0] * (n + 1)
	OPT[1] = 1
	OPT[2] = 1
	for i in range(2, n + 1):
		max_prod = 0
		for j in range(1, i): # Cortes del primer segmento de la soga
			prod = max(j, OPT[j]) * max(i - j, OPT[i - j])
			if prod > max_prod:
				max_prod = prod
		OPT[i] = max_prod
	return OPT

def problema_soga(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	OPT = crear_opt(n)
	return OPT[n]

'''
Complejidad:
	- O(n * m), siendo n la cantidad de metros de la soga y m la cantidad de subcortes que se realizaron. Aunque cuando i = n, m = n.
Por lo que la complejidad final es:
	O(n^2)
'''