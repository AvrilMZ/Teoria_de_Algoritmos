'''
Implementar una función (que utilice división y conquista) de complejidad O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución.

Aclaración: Este ejercicio puede resolverse, casi trivialmente, utilizando una tabla de hash. 
Para hacer interesante el ejercicio, resolver puramente por división y conquista.
'''

def encontrar_numero(arr, inicio, fin):
	if inicio == fin:
		return arr[inicio], 1

	medio = (inicio + fin) // 2
	num_izq, cant_izq = encontrar_numero(arr, inicio, medio)
	num_der, cant_der = encontrar_numero(arr, medio + 1, fin)

	if num_izq == num_der:
		return num_izq, cant_izq + cant_der
	
	if cant_izq > cant_der:
		return num_izq, cant_izq - cant_der
	elif cant_der > cant_izq:
		return num_der, cant_der - cant_izq
	else:
		return None, 0

def mas_de_la_mitad(arr):
	num, cant = encontrar_numero(arr, 0, len(arr) - 1)
	if num is None:
		return False

	total = 0
	for i in arr:
		if i == num:
			total += 1
	return total > len(arr) // 2

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=2T(n/2)+O(1) -> A>=1 y B>1 (O(f(n)) = O(1) ya que solo se comparan los candidatos y se actualizan sus contadores, sin recorrer los subarreglos nuevamente)
	O(1) < n^(log_2(2))
Por lo que la complejidad resulta en:
	O(n)
'''