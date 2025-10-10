'''
Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. 
Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. 
Pasar por un casillero determinado (i, j) nos da una ganancia de V_{i,j}.

Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. 
Hacer una reconstrucción del camino que se debe transitar. 
Indicar y justificar la complejidad del algoritmo implementado. 
Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?

Aclaración: solamente por simplicidad de las pruebas automáticas, devolver en este caso la ganancia máxima obtenible. 
Tener en cuenta que en un examen se pediría la reconstrucción de cómo se obtiene la ganancia.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
Dado a que solo nos podemos mover hacia abajo y la derecha:
	i. Me muevo hacia abajo.
	ii. Me muevo hacia la derecha
Por lo que la ecuacion de recurrencia seria:
	OPT[i][j] = matriz[i - 1][j - 1] + max(OPT[i - 1][j], OPT[i][j - 1])
'''

def crear_opt(matriz):
	OPT = [[0] * (len(matriz[0]) + 1) for _ in range(len(matriz) + 1)]
	for i in range(1, len(matriz) + 1):
		for j in range(1, len(matriz[0]) + 1):
			OPT[i][j] = matriz[i - 1][j - 1] + max(OPT[i - 1][j], OPT[i][j - 1])
	return OPT

def laberinto(matriz):
	if len(matriz) == 0:
		return 0
	OPT = crear_opt(matriz)
	return OPT[len(matriz)][len(matriz[0])]

'''
Complejidad:
	- Crear OPT: O(n * m), siendo n la cantidad de filas de la matriz dada y m la cantidad de columnas.
Por lo que la complejidad en tiempo es:
	O(n * m)
'''