'''
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
Además, cada charla tiene asociado un valor de ganancia. 
Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por 
una tripla de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. 
Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
charlas = [[inicio, fin, ganancia], [inicio, fin, ganancia], ..., [inicio, fin, ganancia]]
Situandome en una charla n debo de considerar la ganancia acumulada de al menos las dos charlas anteriores:
	indice = (n - 1) y (n - 2)
Luego debo decidir:
	i. Me quedo con la anterior, descartando la actual (osea indice n)
	ii. Me quedo con la anteultima sumando la ganancia actual (dado que son compatibles)
Esto se decide comparando ambas opciones y elegiendo cuya ganancia sea mayor.
Finalmente podemos llegar a la conclusion de que la ecuacion de recurrencia es del tipo:
	OPT[n] = max(OPT[n - 2] + ganancia(OPT[n]), OPT[n - 1])
'''

def ultima_compatible(charlas, actual):
	for i in range(actual - 1, -1, -1):
		if charlas[i][1] <= charlas[actual][0]:
			return i
	return -1

def crear_opt(charlas):
	OPT = [0] * len(charlas)
	OPT[0] = charlas[0][2]
	for i in range(1, len(charlas)):
		i_compatible = ultima_compatible(charlas, i)
		if i_compatible != -1:
			OPT[i] = max(OPT[i_compatible] + charlas[i][2], OPT[i - 1])
		else:
			OPT[i] = max(charlas[i][2], OPT[i - 1])
	return OPT

def reconstruir(OPT, charlas):
	a_dar = []
	ganancia_con_actual = 0
	i = len(charlas) - 1
	while i >= 0:
		i_compatible = ultima_compatible(charlas, i)
		if i_compatible != -1:
			ganancia_con_actual = charlas[i][2] + OPT[i_compatible]
		else:
			ganancia_con_actual = charlas[i][2]
		if i > 0:
			if ganancia_con_actual > OPT[i - 1]:
				a_dar.append(charlas[i])
				i = i_compatible
			else:
				i -= 1
		else:
			if ganancia_con_actual > 0:
				a_dar.append(charlas[i])
			break
	a_dar.reverse()
	return a_dar

def scheduling(charlas):
	if len(charlas) == 0:
		return []
	elif len(charlas) == 1:
		return [charlas[0]]
	
	charlas_ord = sorted(charlas, key=lambda x: x[1])
	OPT = crear_opt(charlas_ord)
	return reconstruir(OPT, charlas_ord)

'''
Complejidad:
	- Crear OPT: O(n^2), siendo n la cantidad de charlas. Esto es debido a que por cada charla se busca la ultima compatible, y en el peor de los casos recorreria todas las charlas nuevamente desde la actual hacia atras.
Por lo que la complejidad en tiempo resulta en:
	O(n^2)
'''