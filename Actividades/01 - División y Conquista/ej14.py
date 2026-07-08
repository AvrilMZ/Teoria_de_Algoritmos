'''
Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva y en el punto b es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo. 

Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una).

La complejidad de dicha función debe ser logarítmica del largo del intervalo [a, b]. Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: Se puede trabajar con floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones con la complejidad. Justificar la complejidad de la función implementada.
'''

def raiz(funcion, a, b):
	if funcion(a) == 0:
		return a
	elif funcion(b) == 0:
		return b
	
	mitad = (a + b) // 2
	if funcion(mitad) == 0:
		return mitad
	
	if funcion(a) * funcion(mitad) < 0:
		return raiz(funcion, a, mitad)
	else:
		return raiz(funcion, mitad, b)
	
'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=1T(n/2)+O(1) -> A>=1 y B>1
	O(1) == n^(log_2(1))
Por lo tanto la complejidad resulta en:
	O(log(n))
'''