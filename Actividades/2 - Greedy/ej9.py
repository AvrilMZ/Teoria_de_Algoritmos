'''
Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse en cualquier momento, intentando que se hagan antes del deadline. 
Una tarea puede completarse luego de su deadline, pero ello tendra una penalización de latencia. 
Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten. 
Es decir, dados los arreglos de: T tiempo de duraciones de las tareas y L representando al deadline de cada tarea, 
si definimos que una tarea i empieza en S_i, entonces termina en F_i = S_i + T_i, y su latencia es L_i = F_i - D_i (si F_i > D_i, sino 0).
Nuestra latencia máxima será aquella i que maximice el valor L_i.

Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo que al terminar una tarea se puede empezar la siguiente. 
Indicar y justificar la complejidad del algoritmo implementado.
Devolver un arreglo de tuplas, una tupla por tarea, en el orden en que deben ser realizadas, y que cada tupla indique: 
(el tiempo de la tarea i T_tareas[i] y la latencia resultante L_i de esa tarea).

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def latencia(finalizacion, deadline):
	return max(0, finalizacion - deadline)

def minimizar_latencia(L_deadline, T_tareas):
	tareas = list(zip(L_deadline, T_tareas))
	tareas.sort(key=lambda x: x[0])

	orden = []
	tiempo_acumulado = 0
	for deadline, duracion in tareas:
		tiempo_acumulado += duracion
		latencia_tarea = latencia(tiempo_acumulado, deadline)
		orden.append((duracion, latencia_tarea))

	return orden

'''
La complejidad de utilizar zip es O(n).
Luego ordenar por deadlines cuesta O(n*log(n)).
Por utlimo se recorre nuevamente el arreglo ordenado realizando operaciones constantes, resultando en O(n).
Finalmente la complejidad es O(n*log(n)).

El algoritmo es Greedy dado que en cada iteracion, sobre el arreglo ordenado por deadlines, se toma el mas proximo como nuestro optimo local,
minimizando la latencia. Es la solucion optima ya que si se tomara P_(k+1), con un deadline mas lejano, en vez de P_k, luego P_k tendria mayor 
latencia, resultando en el mismo output sin importar la inversion.
'''