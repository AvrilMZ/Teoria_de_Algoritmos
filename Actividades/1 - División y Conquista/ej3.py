'''
Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(log n). 
Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

Aclaración: no se requiere el uso de ninguna librería de matemática que calcule la raíz cuadrada, ni de forma exacta ni aproximada.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def raiz_entera(n, min, max):
	if min > max:
		return max
	
	medio = (min + max) // 2
	if medio * medio == n:
		return medio
	elif medio * medio < n:
		return raiz_entera(n, medio + 1, max)
	else:
		return raiz_entera(n, min, medio - 1)

def parte_entera_raiz(n):
	return raiz_entera(n, 1, n)

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=1T(n/2)+O(1) -> A>=1 y B>1
	O(1) == n^(log_2(1))
Por lo tanto el orden final es:
	O(log(n))
'''