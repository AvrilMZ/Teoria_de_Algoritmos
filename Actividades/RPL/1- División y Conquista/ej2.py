'''
Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). 
Se pide una función de complejidad O(log(n)) que encuentre el índice del primer 0. 
Si no hay ningún 0 (solo hay unos), debe devolver -1.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "en O(log(n))". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se 
busca que se implemente con dicha restricción (se hacen pruebas de volumen que deben ejecutar correctamente)
'''
def buscar_indice(arr, izq, der):
	if izq > der:
		return -1
	
	medio = (izq + der) // 2
	if arr[medio] == 0:
		if medio == 0 or arr[medio - 1] == 1:
			return medio
		else:
			return buscar_indice(arr, izq, medio - 1)
	else:
		return buscar_indice(arr, medio + 1, der)

def indice_primer_cero(arr):
	return buscar_indice(arr, 0, len(arr) - 1)