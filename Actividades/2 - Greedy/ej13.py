'''
Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante conocido).

Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta (números reales positivos) desordenadas, y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, y se construya para esto la menor cantidad de antenas posibles. 

Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo da la solución óptima siempre?

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def existe_cobertura(casa, antenas, R):
	if len(antenas) == 0:
		return False
	
	ultima_antena = antenas[len(antenas) - 1]
	if ultima_antena - casa >= 0 and ultima_antena - casa <= R:
		return True
	elif casa - ultima_antena >= 0 and casa - ultima_antena <= R:
		return True
	
	return False

def cobertura(casas, R, K):
	if len(casas) == 1:
		return [casas[0]]
	
	casas_ord = sorted(casas)
	antenas = []

	for i in range(0, len(casas_ord)):
		casa = casas_ord[i]
		if existe_cobertura(casa, antenas, R):
			continue
		elif not existe_cobertura(casa, antenas, R):
			if casa + R <= K:
				antenas.append(casa + R)
			else:
				antenas.append(K)
				break

	return antenas

'''
Complejidad:
	- Sorted: O(n*log(n))
	- Se recorren todas las casas una vez: O(n)
	- Se evalua si existe cobertura con la utlima antena: O(1)
Por lo que la complejidad final resulta en:
	O(n*log(n))

Es un algoritmo greedy dado a que por cada iteracion sobre las casas se busca abarcar la mayor cantidad de kilometros con una antena, verificando asi mismo si ya exisita otra cubriendo su radio para minimizar la cantidad. Se obtiene la solución óptima porque, inductivamente:
	1. Ordeno todas las casas ascendentemente y busco la primera sin covertura
	2. Coloco la antena lo mas lejos posible, dentro del radio, para abarcar la mayor cantidad de casas posibles.
	3. Repito los pasos consiguiendo la minima cantidad de antenas posibles a colocar.
'''