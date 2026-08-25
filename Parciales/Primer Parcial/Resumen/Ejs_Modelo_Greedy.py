# ==============================================================================================================
# ==============================================================================================================
# PROBLEMAS CONOCIDOS:
# 	- Scheduling
#	- Árboles de Huffman
#	- Problema del cambio
#	- Compras con inflación
#	- Carga de combustible
#	- Mochila
#	- Optimal Caching
#	- Coloreo de intervalos
#
# JUSTIFICACION GREEDY:
#	- Explicar la regla sencilla.
#	- Explicar cual es el optimo local que se obtiene en el estado actual.
# ==============================================================================================================
# ==============================================================================================================

# EJ 11
'''
Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. 
Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los 
productos en la menor cantidad posible de bolsas. 
Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. 
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def bolsas(capacidad, productos):
	if len(productos) == 0:
		return []

	distribucion = []
	for producto in productos:
		for bolsa in distribucion:
			if sum(bolsa) + producto <= capacidad:
				bolsa.append(producto)
				break
		else:
			distribucion.append([producto])
	return distribucion

'''
Ordenar el arrgelo tiene una complejidad de O(n*log(n)).
Luego se recorren todos los productos y bolsas para agregar los productos correspondientes en O(n*m), siendo n la cantidad de productos y
m la cantidad de bolsas.
Finalmente la complejidad resulta en O(n * log(n) + m)

No es un algoritmo optimo ya que puede que colocando los productos en un orden distinto minimice todavia mas la cantidad. Por ejemplo:
- Si se tienen los libros [2,4,6,3,1] y cada caja tiene un peso maximo de 8.
- El algoritmo devolveria:
	[[2,4,1],[6],[3]] -> 3 bolsas
cuando el optimo seria:
	[[2,6],[4,3,1]] -> 2 bolsas
'''

# ============================================================================
# EJ 12
'''
Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad República. 
Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales no es otro sino Arnook. 
En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos por el control de diferentes kilómetros de la ruta costera. 
Cada pequeña mafia le pide a Arnook control sobre un rango de kilómetros 
(por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ). 
Si hay una mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden solaparse). 
Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”, indistintamente de los kilómetros pedidos. 
Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie, así lo único que es de interés es maximizar la cantidad de permisos otorgados 
(asegurándose de no otorgarle algún lugar a dos mafias diferentes). 

Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine a cuáles se les otorgará control, de forma que no hayan 
dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados. Indicar y justificar la complejidad del algoritmo implementado. 
Justificar por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

def hay_interseccion(fin_anterior, inicio_nueva):
	return fin_anterior > inicio_nueva

# Pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
	pedidos_ordenados = sorted(pedidos, key=lambda x: x[1])
	control = []
	km_fin_anterior = None
	for inicio, fin in pedidos_ordenados:
		if len(control) == 0 or not hay_interseccion(km_fin_anterior, inicio):
			control.append((inicio, fin))
			km_fin_anterior = fin
	return control

'''
Ordenar el arreglo por km de finalizacion tiene un costo de O(n*log(n)).
Recorrer cada pedido del arreglo ordenado realizando acciones constantes resulta en O(n).
Finalmente concluimos en una complejidad de O(n*log(n)).

El algoritmo es Greedy dado que al ordenar el arraglo por km de finalizacion siempre se busca siempre el rango mas proximo al fin del pedido anterior
para maximizar la cantidad de pedidos otorgados. El algoritmo es optimo, ya que en caso de existir un k+1 cuya finalizacion sea luego de la de k invertir los
pedidos resulta en el mismo resultado o peor ya que le puede quitar la posibilidad de otorgar otro pedido.
'''

# ============================================================================
# EJ 16
'''
El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima cantidad de sus n socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas. 
Dada un lista de tuplas (duplas) de personas que se conocen:
	a. Nos solicitan seleccionar el mayor número posible de invitados. Proponer una estrategia greedy óptima para resolver el problema.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.
Métodos del grafo:
	Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
	agregar_vertice(self, v)
	borrar_vertice(self, v)
	agregar_arista(self, v, w, peso = 1)
		el resultado será v <--> w
	borrar_arista(self, v, w)
	estan_unidos(self, v, w)
	peso_arista(self, v, w)
	obtener_vertices(self)
		Devuelve una lista con todos los vértices del grafo
	vertice_aleatorio(self)
	adyacentes(self, v)
	str
'''

def definir_conexiones(conocidos):
	conexiones = {}
	for a, b in conocidos:
		if a not in conexiones:
			conexiones[a] = set()
		if b not in conexiones:
			conexiones[b] = set()
		conexiones[a].add(b)
		conexiones[b].add(a)
	return conexiones
			
# conocidos: lista de pares de personas que se conocen, cada elemento es un (a,b)
def obtener_invitados(conocidos):
	if len(conocidos) == 0:
		return []
	
	conexiones = definir_conexiones(conocidos)
	seguir = True
	while seguir:
		eliminados = False
		for persona in list(conexiones.keys()):
			if len(conexiones[persona]) < 4:
				for otros in conexiones.values():
					otros.discard(persona)
				conexiones.pop(persona)
				eliminados = True
				break
		if not eliminados:
			seguir = False

	return list(conexiones.keys())

# ============================================================================
# EJ 9
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

# ============================================================================
# EJ 13
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

# ============================================================================
# EJ 15
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