'''
Implementar una función (que utilice división y conquista) de complejidad O(n logn) que dado un arreglo de n números enteros devuelva true 
o false según si existe algún elemento que aparezca más de la mitad de las veces. 
Justificar el orden de la solución. 

Ejemplos:
	[1, 2, 1, 2, 3] -> false
	[1, 1, 2, 3] -> false
	[1, 2, 3, 1, 1, 1] -> true
	[1] -> true

Aclaración: Este ejercicio puede resolverse, casi trivialmente, ordenando el arreglo con un algoritmo eficiente, 
o incluso se puede realizar más rápido utilizando una tabla de hash. 
Para hacer interesante el ejercicio, resolver sin ordenar el arreglo, sino puramente división y conquista.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(n log(n))". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def encontrar_numero(arr, left, right):
	if left == right:
		return arr[left]
	
	mid = (left + right) // 2
	num_left = encontrar_numero(arr, left, mid)
	num_right = encontrar_numero(arr, mid + 1, right)
	
	if num_left == num_right:
		return num_left
	
	count_left = arr[left:right + 1].count(num_left)
	count_right = arr[left:right + 1].count(num_right)
	
	if count_left > count_right:
		return num_left
	else:
		return num_right

def mas_de_la_mitad(arr):
	cand = encontrar_numero(arr, 0, len(arr) - 1)
	return arr.count(cand) > len(arr) // 2

'''
Se utiliza la misma logica para subdividir el arreglo que merge sort, por lo que la complejidad es la misma.
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=2T(n/2)+O(n) -> A>=1 y B>1
	O(n) == n^(log_2(2))
Por lo que la complejidad resulta en:
	O(n*log(n))
'''