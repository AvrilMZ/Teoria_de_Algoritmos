'''
Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. 
Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los 
productos en la menor cantidad posible de bolsas. 
Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. 
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def bolsas(capacidad, productos):
	if len(productos) == 0:
		return []

	distribucion = []
	for producto in productos:
		for bolsa in distribucion:
			if sum(bolsa) + producto <= capacidad:
				bolsa.append(producto)
				break
		else:
			distribucion.append([producto])
	return distribucion

'''
Ordenar el arrgelo tiene una complejidad de O(n*log(n)).
Luego se recorren todos los productos y bolsas para agregar los productos correspondientes en O(n*m), siendo n la cantidad de productos y
m la cantidad de bolsas.
Finalmente la complejidad resulta en O(n * log(n) + m)

No es un algoritmo optimo ya que puede que colocando los productos en un orden distinto minimice todavia mas la cantidad. Por ejemplo:
- Si se tienen los productos [2,4,6,3,1] y cada bolsa tiene un peso maximo de 8.
- El algoritmo devolveria:
	[[2,4,1],[6],[3]] -> 3 bolsas
cuando el optimo seria:
	[[2,6],[4,3,1]] -> 2 bolsas
'''