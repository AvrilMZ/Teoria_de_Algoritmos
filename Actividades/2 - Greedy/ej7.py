'''
Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. 
Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. 
El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). 
Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. 
Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def precios_inflacion(R):
	precios_descendente = sorted(R, key=None, reverse=True)
	pasada = 0
	precios_actualizados = 0
	for precio in precios_descendente:
		precios_actualizados += (precio**(pasada + 1))
		pasada += 1
	return precios_actualizados

'''
Ordenar el arrgelo descendentemente tiene una complejidad O(n*log(n)).
Luego se recorre el arreglo nuevamente aplicando una operacion constante, por lo que resulta en O(n).
Finalmente la complejidad es de O(n*log(n)).

El algoritmo implementado es Greedy dado a que en cada dia se busca minimizar el costo arrancando por el producto mas caro, ya que la inflacion
realiza un incremento exponencial. El algoritmo es optimo ya que si en algún arreglo existe un par consecutivo P_k < P_(k+1), intercambiarlos 
disminuye la suma:
	P_(k+1)^k + P_k^(k+1) < P_k^k + P_(k+1)^(k+1)
'''