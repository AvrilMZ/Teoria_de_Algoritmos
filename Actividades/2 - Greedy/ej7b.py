'''
En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. 
Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero Wakanda está atravesando una era de deflación y los precios disminuyen todo el tiempo. 
El precio del producto i el día j+1 es exactamente la mitad del precio en el día j. El arreglo R[i] indica todos los precios del primer día. 
Si bien para reducir costos se debería esperar a que los productos sigan bajando, los tiempos de entrega no nos permiten esperar, y cada 
día debemos comprar uno de los productos.

Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. 
Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def precios_deflacion(R):
	precios_ordenados = sorted(R)
	pasada = 0
	suma_precios = 0
	for precio in precios_ordenados:
		suma_precios += precio / (2 ** pasada)
		pasada += 1
	return suma_precios

'''
Ordenar el arrgelo ascendentemente tiene una complejidad O(n*log(n)).
Luego se recorre el arreglo nuevamente aplicando una operacion constante, por lo que resulta en O(n).
Finalmente la complejidad es de O(n*log(n)).

El algoritmo implementado es Greedy dado a que en cada dia se busca minimizar el costo arrancando por el producto mas barato, ya que la deflacion
realiza un decremento exponencial. El algoritmo es optimo ya que si en algún arreglo existe un par consecutivo P_k > P_(k+1), intercambiarlos 
disminuye la suma:
	P_(k+1)^k + P_k^(k+1) > P_k^k + P_(k+1)^(k+1)
'''