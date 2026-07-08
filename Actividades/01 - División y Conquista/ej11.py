'''
Implementar una función (que utilice división y conquista) de complejidad O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de dos tercios de las veces. Justificar la complejidad de la solución.

Aclaración: Este ejercicio puede resolverse, casi trivialmente, utilizando una tabla de hash. 
Para hacer interesante el ejercicio, resolver puramente por división y conquista.
'''

def encontrar_numero(arr, inicio, fin):
	if inicio == fin:
		return [arr[inicio]]

	medio = (inicio + fin) // 2
	num_izq = encontrar_numero(arr, inicio, medio)
	num_der = encontrar_numero(arr, medio + 1, fin)

	numeros = num_izq + num_der

	contadores = {}
	for c in numeros:
		if c in contadores:
			contadores[c] += 1
		elif len(contadores) < 2:
			contadores[c] = 1
		else:
			borrar = []
			for x in contadores:
				contadores[x] -= 1
				if contadores[x] == 0:
					borrar.append(x)
			for x in borrar:
				del contadores[x]
	return list(contadores.keys())

def mas_de_dos_tercios(arr):
	numeros = encontrar_numero(arr, 0, len(arr) - 1)

	for c in numeros:
		if arr.count(c) > (2 * len(arr)) // 3: # .count = O(n)
			return True
	return False

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=2T(n/2)+O(1) -> A>=1 y B>1 (O(f(n)) = O(1) ya que solo se comparan los candidatos y se actualizan sus contadores, sin recorrer los subarreglos nuevamente)
	O(1) < n^(log_2(2))
Por lo que la complejidad resulta en:
	O(n)
'''