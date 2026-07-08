'''
Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something, que transportaba una importante piedra preciosa de la corona británica. Al parecer, la escondieron en un cofre con muchas piedras preciosas falsas, en caso de un ataque. Barba-ra Verde sabe que los refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. El problema es que no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya verdadera. La única forma de descubrir la joya verdadera es pesando. Se sabe que la joya verdadera va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. Cuenta con una balanza de platillos para poder pesarlas (es el 1700, no esperen una balanza digital).

Indicar la posición de la Joya verdadera e indicar y justificar (adecuadamente) la complejidad de la función implementada.

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