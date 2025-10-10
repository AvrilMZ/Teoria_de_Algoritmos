'''
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.

Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados 
para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado. 
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def coeficiente(valor, peso):
	return valor / peso

# Cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
	elementos_ordenados = sorted(elementos, key=lambda x: coeficiente(x[0], x[1]), reverse=True)
	mochila = []
	peso_acumulado = 0
	for elemento in elementos_ordenados:
		if peso_acumulado + elemento[1] <= W:
			mochila.append(elemento)
			peso_acumulado += elemento[1]
	return mochila

'''
Se ordena el arreglo con una complejidad O(n*log(n)).
Luego se iteran los elementos ordenados mientras haya espacio en la mochila en O(n).
Finalmente la complejidad resulta en O(n*log(n)).

El algoritmo es Greedy ya que se busca una solucion local al problema buscando un balance entre el valor y peso de los elementos,
consiguiendo guardar el mejor promedio. Aunque este algoritmo no es optimo debido a que existe la posibilidad de el valor como el peso sean
bajos y que su coeficiente le "gane" a un elemento con peso y valor mas altos, dejando fuera elementos que sumandolos le aporten un mayor 
valor a la mochila. Por ejemplo:
	[(60,10), (100,20), (120,30)], W=50
El algoritmo elegiria [(60,10), (100,20)] con valor total = 160
Mientras que la solucion optima seria [(100,20), (120,30)] con valor total = 220
'''