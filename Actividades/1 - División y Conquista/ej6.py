'''
Implementar un algoritmo de multiplicación de dos números grandes de longitud n, por división y conquista, con un orden de complejidad mejor que O(n^2). 
Justificar la complejidad del algoritmo mediante el teorema maestro.
'''

def multiplicar(a, b):
	if a < 10 or b < 10:
		return a * b

	n = max(len(str(a)), len(str(b)))
	m = n // 2

	x1 = a // 10**m
	x0 = a % 10**m
	y1 = b // 10**m
	y0 = b % 10**m

	p = multiplicar(x1 + x0, y1 + y0)
	x0y0 = multiplicar(x0, y0)
	x1y1 = multiplicar(x1, y1)

	return x1y1 * 10**(2*m) + (p - x1y1 - x0y0) * 10**m + x0y0

'''
Teniendo en cuenta el teorema maestro:
	T(n)=AT(n/B)+O(f(n))
Entonces:
	T(n)=3T(n/2)+O(n) -> A>=1 y B>1 (O(f(n)) = O(n) ya que requiere recorrer los n digitos)
	O(n) < n^(log_2(3))
Por lo que la complejidad resulta en:
	O(n^1,6) aproximadamente
'''