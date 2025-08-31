'''
Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: 
estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1). 
Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2. 

Se pide:
Implementar un algoritmo de división y conquista de complejidad O(log n) que encuentre la posición p del pico: 
	func PosicionPico(v []int, ini, fin int) int. 
La función será invocada inicialmente como: PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que el arreglo tenga forma de pico.

Justificar la complejidad del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

def posicion_pico(v, ini, fin):
	if ini == fin:
		return ini
	
	medio = (ini + fin) // 2
	if medio > 0 and medio < fin and v[medio] > v[medio - 1] and v[medio] > v[medio + 1]:
		return medio
	elif v[medio] < v[medio + 1]:
		return posicion_pico(v, medio + 1, fin)
	else:
		return posicion_pico(v, ini, medio - 1)
	
'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=1T(n/2)+O(1) -> A>=1 y B>1
	O(1) == n^(log_2(1))
Por lo tanto la complejidad resulta en:
	O(log(n))
'''