'''
Implementar Merge Sort. Justificar la complejidad del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea de ordenamiento "por Merge Sort". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

def merge(izq, der):
	resultado = []
	i = j = 0

	while i < len(izq) and j < len(der):
		if izq[i] <= der[j]:
			resultado.append(izq[i])
			i += 1
		else:
			resultado.append(der[j])
			j += 1

	resultado.extend(izq[i:])
	resultado.extend(der[j:])

	return resultado

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	
	medio = len(arr) // 2
	parte_izq = merge_sort(arr[:medio])
	parte_der = merge_sort(arr[medio:])

	return merge(parte_izq, parte_der)

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=2T(n/2)+O(n) -> A>=1 y B>1
	O(n) == n^(log_2(2))
Por lo que la complejidad resulta en:
	O(n*log(n))
'''