'''
Un centro de fotocopiado tiene un conjunto de máquinas para procesar diferentes trabajos. Las mismas las compró en dos momentos diferentes. Teniendo m fotocopiadoras de la primera compra y k fotocopiadoras más modernas de la segunda. Como la tecnología mejoró las más nuevas trabajan el doble de rápido que las viejas. Cada día recibe un conjunto de pedidos con diferentes longitudes. Desea asignar las tareas a las máquinas de tal forma de terminar lo antes posible la jornada de trabajo.

Proponer un algoritmo de aproximación de tal forma que la diferencia con el óptimo sea como mucho 3 veces mayor.
'''

'''
m fotocopiadoras viejas
k fotocopiadoras nuevas
P_i: pedidos recibidos el dia i

n es el tiempo del trabajo mas largo P.
Cotas de nuestro problema:
	- Cota superior: m = 2n
	- Cota inferior: k = n
Proponemos el siguiente algoritmo:
	1. Ordenar los tiempos de forma descendente.
	2. Agregar un trabajo en k si es menor al doble de trabajos que tiene m, en caso contrario agregarselo a m.
'''