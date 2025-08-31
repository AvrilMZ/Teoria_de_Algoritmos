'''
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. 
Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. 
El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y debe devolver qué 
monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada. Indicar y justificar la complejidad del algoritmo implementado.
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo. 
¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def cambio(monedas, monto):
	monedas_ordenadas = sorted(monedas, key=None, reverse=True)
	cambio = []
	for moneda in monedas_ordenadas:
		while monto >= moneda:
			cambio.append(moneda)
			monto -= moneda
	return cambio

'''
Ordenar las monedas de mayor a menor tiene un costo de O(n*log(n)).
Recorrer el arreglo de monedas para conseguir la cantidad necesaria para el monto cuesta O(n + monto).
Finalmente la complejidad es de O(n * log(n) + monto).

El algoritmo propuesto es Greedy dado que en cada iteracion elije el monto mas acertado del cambio, es decir el billete mayor posible para
minimizar la cantidad entregada. No es optimo dado a que puede existir un caso donde la menor combinacion no incluya los billetes de mayor
denominacion, por ejemplo:
	monedas: [4, 3, 1], monto = 6
El algoritmo eligiria 3 moneadas a entregar [4, 1, 1], mientras que la solucion optima serian 2, [3, 3].
'''