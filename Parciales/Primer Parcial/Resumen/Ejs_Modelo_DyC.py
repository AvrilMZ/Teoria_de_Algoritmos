# ==============================================================================================================
# ==============================================================================================================
# ALGORITMOS USADOS:
# 	- Merge Sort
# 	- Busqueda Binaria
#
# TEOREMA MAESTRO:
# 	T(n) = A T(n/B) + O(f(n)), donde A >= 1 y B > 1
# 	Si:
#		- f(n) = n^(log_B(A)) -> O(f(n)*log(n))
#		- f(n) > n^(log_B(A)) -> O(f(n))
#		- f(n) < n^(log_B(A)) -> O(n^(log_B(A)))
# ==============================================================================================================
# ==============================================================================================================

# EJ 11
'''
Implementar una función (que utilice división y conquista) de complejidad O(n) que dado un arreglo de n números enteros devuelva true o 
false según si existe algún elemento que aparezca más de dos tercios de las veces. 
Justificar la complejidad de la solución.

Aclaración: Este ejercicio puede resolverse, casi trivialmente, utilizando una tabla de hash. 
Para hacer interesante el ejercicio, resolver puramente por división y conquista.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(n)". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
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

# ============================================================================
# EJ 9
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

# ============================================================================
# EJ 12
'''
Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del 
arreglo es potencia de 2 (por ende, n también lo es). 
Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, 
sin utilizar espacio adicional (obviando el utilizado por la recursividad y variables de tipos simples). 
¿Cual es la complejidad del algoritmo?

Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). 
Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

def mezclar(arr, inicio, fin):
	cantidad = fin - inicio + 1
	if cantidad <= 2:
		return

	mitad = (inicio + fin) // 2
	bloque = (mitad - inicio + 1) // 2

	for k in range(bloque):
		i = mitad - bloque + 1 + k
		j = mitad + 1 + k
		arr[i], arr[j] = arr[j], arr[i]
		
	mezclar(arr, inicio, mitad)
	mezclar(arr, mitad + 1, fin)

def alternar(arr):
	mezclar(arr, 0, len(arr) - 1)
	return arr

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=2T(n/2)+O(n) -> A>=1 y B>1
	O(n) == n^(log_2(2))
Por lo tanto la complejidad resulta en:
	O(n*log(n))
'''

# ============================================================================
# EJ 8
'''
Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. 
El arreglo A está completamente ordenado de menor a mayor. 
El arreglo B se encuentra desordenado. 
Indicar, por división y conquista, la cantidad de inversioes necesarias al arreglo B para que quede ordenado de menor a mayor, con un orden de complejidad mejor que O(n^2). 
Justificar la complejidad del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "en tiempo mejor que O(n^2)". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

def merge_count(izq, der):
	resultado = []
	i = j = 0
	inv_count = 0

	while i < len(izq) and j < len(der):
		if izq[i] <= der[j]:
			resultado.append(izq[i])
			i += 1
		else:
			resultado.append(der[j])
			j += 1
			inv_count += len(izq) - i

	resultado.extend(izq[i:])
	resultado.extend(der[j:])

	return resultado, inv_count

def merge_sort_count(arr):
	if len(arr) <= 1:
		return arr, 0

	medio = len(arr) // 2

	izq, inv_izq = merge_sort_count(arr[:medio])
	der, inv_der = merge_sort_count(arr[medio:])

	merged, inv_merge = merge_count(izq, der)
	total_inv = inv_izq + inv_der + inv_merge

	return merged, total_inv

def contar_inversiones(A, B):
	ordenados, inv = merge_sort_count(B)
	return inv

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=2T(n/2)+O(n) -> A>=1 y B>1
	O(n) == n^(log_2(2))
Por lo tanto la complejidad resulta en:
	O(n*log(n))
Al igual que al algoritmo tradicional de merge sort.
'''

# ============================================================================
# EJ 16
'''
Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something, que transportaba una importante piedra preciosa de la corona británica. 
Al parecer, la escondieron en un cofre con muchas piedras preciosas falsas, en caso de un ataque. 
Barba-ra Verde sabe que los refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. 
El problema es que no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya verdadera. 
La única forma de descubrir la joya verdadera es pesando. Se sabe que la joya verdadera va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. 
Cuenta con una balanza de platillos para poder pesarlas (es el 1700, no esperen una balanza digital).

Indicar la posición de la Joya verdadera.

En el ejemplo de código inicial de la actividad mostramos un llamado de ejemplo a la función balanza, a la que se le deben pasar los dos conjuntos de joyas a verificar. 
La cantidad de joyas en cada conjunto debe ser la misma, para que el resultado de la balanza de platillos nos dé información.
	Si los dos platillos pesan lo mismo, balanza devuelve 0.
	Si el primer platillo es más pesado, balanza devuelve 1.
	Si el segundo platillo es más pesado, balanza devuelve -1.
'''

from balanza import *

def buscar_joya(joyas, inicio, fin):
	if fin - inicio == 1:
		return inicio
	
	n = fin - inicio
	mitad = n // 2
	
	platillo1 = [joyas[inicio + i] for i in range(mitad)]
	platillo2 = [joyas[inicio + mitad + i] for i in range(mitad)]
	
	resultado = balanza(platillo1, platillo2)
	if resultado == 1:
		return buscar_joya(joyas, inicio, inicio + mitad)
	elif resultado == -1:
		return buscar_joya(joyas, inicio + mitad, inicio + 2*mitad)
	else:
		return buscar_joya(joyas, inicio + 2*mitad, fin)

def encontrar_joya(joyas):
	return buscar_joya(joyas, 0, len(joyas))

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=1T(n/2)+O(n) -> A>=1 y B>1
	O(n) > n^(log_2(1))
Por lo tanto la complejidad resulta en:
	O(n)
'''