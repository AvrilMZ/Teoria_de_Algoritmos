'''
Se tiene una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente enteros). Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas disponibles son de la misma capacidad L (se asegura que L >= n). Obviamente, no podés partir un libro para que vaya en múltiples cajas, pero sí podés poner múltiples libros en una misma caja, siempre y cuando los espesores no superen esa capacidad L. 

Implementar un algoritmo Greedy que obtenga las cajas, tal que se minimicen la cantidad de cajas a utilizar. 

Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar.

¿Qué cambios aplicarías si supieras que los espesores sólo fueran números enteros? Describir cómo afecta a la complejidad y a su optimalidad.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

def cajas(capacidad, libros):
	if len(libros) == 0:
		return []
	
	c = []
	for libro in libros:
		for caja in c:
			if sum(caja) + libro <= capacidad:
				caja.append(libro)
				break
		else:
			c.append([libro])
	
	return c

'''
Complejidad:
	- Por cada libro (n) se recorren todas las cajas creadas (m) buscando alguna cuya peso no supere el maximo al agregar el nuevo libro.
Por lo que la complejidad total resulta en:
	O(n^2), dado que m en el peor caso es igual a n.

Es un algoritmo greedy dado que por cada libro se busca siempre una caja empezada antes de comenzar una nueva, minimizando la cantidad de cajas totales a usar.
No es un algoritmo optimo ya que puede que coloclando los libros en un orden distinto minimice todavia mas la cantidad. Por ejemplo:
	- Si se tienen los libros [2,4,6,3,1] y cada caja tiene un peso maximo de 8.
	- El algoritmo devolveria:
		[[2,4,1],[6],[3]] -> 3 bolsas
	cuando el optimo seria:
		[[2,6],[4,3,1]] -> 2 bolsas

Si los espesores fueran solo enteros el algoritmo no se ve afectado y quedaria igual.
'''