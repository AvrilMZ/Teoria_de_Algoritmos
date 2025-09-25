# ==============================================================================================================
# ==============================================================================================================
# PROBLEMAS CONOCIDOS:
# 	- Scheduling:
# 		OPT[n] = max(OPT[n - 2] + ganancia(OPT[n]), OPT[n - 1])
# 	- Juan el vago: 
# 		OPT[n] = max(OPT[n - 2] + ganancia(n), OPT[n - 1])
#	- Laberinto: 
# 		OPT[i][j] = matriz[i - 1][j - 1] + max(OPT[i - 1][j], OPT[i][j - 1])
# 	- Teclado del telefono: 
# 		OPT[n][m] = \sum_{v = vecinos de m} OPT[n - 1][v]
#	- Mochila: 
# 		OPT[n][W] = max(OPT[n - 1][W - peso(OPT[n][W])] + valor(OPT[n][W]), OPT[n - 1][W])
#	- Subset-sum: 
# 		OPT[i][v] = max(OPT[i - 1][v - valor(OPT[i][v])] + valor(OPT[i][v]), OPT[i - 1][v])
# 	- Londres-California:
#		California:
#			OPT_C[n] = min(OPT_L[n - 1] + M, OPT_C[n - 1]) + C[n]
#		Londres:
#			OPT_L[n] = min(OPT_C[n - 1] + M, OPT_L[n - 1]) + L[n]
# ==============================================================================================================
# ==============================================================================================================

# EJ 2
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

'''
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.

Implementar un algoritmo que, por programación dinámica, reciba los valores y pesos de los elementos, y devuelva qué elementos deben 
ser guardados para maximizar la ganancia total.

Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

# ============================================================================
# EJ 7
'''
Para este problema tenemos dos posibilidades:
	i. Agregar el elemento a la mochila, achicando la brecha con el peso maximo e incrementando el valor.
	ii. No agregar el elemento y seguir con el siguiente.
Dados estos casos podemos plantear la ecuacion de recurrencia con una matriz:
	OPT[n][W] = max(OPT[n - 1][W - peso(OPT[n][W])] + valor(OPT[n][W]), OPT[n - 1][W])
Donde se elije siempre el valor maximo entre agregar el elemento o no, siempre y cuando, al agregar el elemento, no nos estemos pasando de la capacidad W de la mochila.
'''

def crear_opt(elementos, W):
	OPT = [[0] * (W + 1) for _ in range(len(elementos) + 1)]

	for i in range(1, len(elementos) + 1):
		valor, peso = elementos[i - 1]
		for w in range(W + 1):
			if peso <= w:
				OPT[i][w] = max(OPT[i - 1][w], OPT[i - 1][w - peso] + valor)
			else:
				OPT[i][w] = OPT[i - 1][w]
				
	return OPT

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
	OPT = crear_opt(elementos, W)
	res = []
	w = W
	for i in range(len(elementos), 0, -1):
		if OPT[i][w] != OPT[i - 1][w]:
			res.append(elementos[i - 1])
			w -= elementos[i - 1][1]
	res.reverse()
	return res

'''
Complejidad:
	- Crear la matriz optima es O(n * W) donde n es la cantidad de elementos y W el peso maximo de la mochila.
	- Recostruir la solucion es O(n) dado que se recorre el arreglo de elementos obteniendo su elemento correspondiente en OPT.
	- Dar vuelta el arreglo: O(n)
Por lo que la complejidad final es:
	O(n * W) + O(n) + O(n) = O(n * W)
'''

# ============================================================================
# EJ 9
'''
Tenemos un conjunto de números v_1, v_2, …, v_n, y queremos obtener un subconjunto de todos esos números tal que su suma sea igual o menor a un valor V, tratando de aproximarse lo más posible a V. 

Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores, y la suma objetivo V, y devuelva qué elementos deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
Para este problema tenemos dos posibilidades por iteracion:
	i. Agregar el valor y achicar la brecha con V.
	ii. Saltear el valor y quedarme con el valor previo.
Teniendo en cuenta esto se puede plantear la ecuacion de recurrencia sobre una matriz:
	OPT[i][v] = max(OPT[i - 1][v - valor(OPT[i][v])] + valor(OPT[i][v]), OPT[i - 1][v])
Siendo i el indice del valor y v el valor. Esto es siempre y cuando no se supere el valor de V.
'''

def crear_opt(elementos, v):
	OPT = [[0] * (v + 1) for _ in range(len(elementos) + 1)]
	for i in range(1, len(elementos) + 1):
		for j in range(1, v + 1):
			if elementos[i - 1] <= j:
				OPT[i][j] = max(OPT[i - 1][j - elementos[i - 1]] + elementos[i - 1], OPT[i - 1][j])
			else:
				OPT[i][j] = OPT[i - 1][j]
	return OPT

def subset_sum(elementos, v):
	if len(elementos) == 0:
		return []
	OPT = crear_opt(elementos, v)
	res = []
	actual = v
	for i in range(len(elementos), 0, -1):
		if OPT[i][actual] != OPT[i - 1][actual]:
			res.append(elementos[i - 1])
			actual -= elementos[i - 1]
	res.reverse()
	return res

'''
Complejidad:
	- Crear la matriz optima es O(n * V) donde n es la cantidad de elementos y V el valor maximo.
	- Recostruir la solucion es O(n) dado que se recorre el arreglo de elementos obteniendo su elemento correspondiente en OPT.
	- Dar vuelta el arreglo: O(n)
Por lo que la complejidad final es:
	O(n * W) + O(n) + O(n) = O(n * W)
'''

# ============================================================================
# EJ 10
'''
Manejamos un negocio que atiende clientes en Londres y en California. Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: L y C, con valores para todos los meses hasta n. Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo M por la mudanza. 

Dados los arreglos de costos de operación en Londres (L) y California (C), indicar la secuencia de las n localizaciones en las que operar durante los n meses, sabiendo que queremos minimizar el total de los costos de operación. Se puede empezar en cualquier ciudad. Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
Dado el problema tenemos las siguiente opciones por cada iteracion:
	California:
		i. Estoy en California y me mudo a Londres, gastando el costo fijo M.
		ii. Me quedo en California.
	Londres:
		i. Estoy en Londres y me mudo a California, gastando el costo fijo M.
		ii. Me quedo en Londres.
Para este problema, dado a que al mudarnos estariamos "apostando" a las ganancias futuras de la ciudad, nos conviene plantear dos ecuaciones de recurrencia que dependan mutuamente de la otra, y al final elegir cual de ambas nos convenia para minimizar el total de los costos de operacion. Las ecuaciones seria:
	California:
		OPT_C[n] = min(OPT_L[n - 1] + M, OPT_C[n - 1]) + C[n]
	Londres:
		OPT_L[n] = min(OPT_C[n - 1] + M, OPT_L[n - 1]) + L[n]
donde en ambos casos n es la cantidad de meses. En ambos se decide si conviene mudarse o quedarse en la ciudad mediante el costo que conlleve ese mes en ambas ciudades.
'''

def crear_opt(arreglo_L, arreglo_C, costo_M):
	OPT_L = [0] * len(arreglo_L)
	OPT_C = [0] * len(arreglo_C)
	prev_L = [None] * len(arreglo_L)
	prev_C = [None] * len(arreglo_C)

	OPT_L[0] = arreglo_L[0]
	OPT_C[0] = arreglo_C[0]
	prev_L[0] = ['londres']
	prev_C[0] = ['california']

	for i in range(1, len(arreglo_L)):
		if OPT_L[i - 1] + costo_M <= OPT_C[i-1]:
			OPT_C[i] = OPT_L[i - 1] + costo_M + arreglo_C[i]
			prev_C[i] = "londres"
		else:
			OPT_C[i] = OPT_C[i - 1] + arreglo_C[i]
			prev_C[i] = "california"

		if OPT_C[i - 1] + costo_M <= OPT_L[i - 1]:
			OPT_L[i] = OPT_C[i - 1] + costo_M + arreglo_L[i]
			prev_L[i] = "california"
		else:
			OPT_L[i] = OPT_L[i - 1] + arreglo_L[i]
			prev_L[i] = "londres"
	
	return OPT_C, prev_C, OPT_L, prev_L

def reconstruccion(OPT_C, prev_C, OPT_L, prev_L):
	ruta = []
	if OPT_C[len(OPT_C) - 1] <= OPT_L[len(OPT_L) - 1]:
		ciudad = "california"
	else:
		ciudad = "londres"

	for i in range(len(OPT_C), 0, -1):
		ruta.append(ciudad)
		if ciudad == "california":
			ciudad = prev_C[i - 1]
		else:
			ciudad = prev_L[i - 1]

	ruta.reverse()
	return ruta

def plan_operativo(arreglo_L, arreglo_C, costo_M):
	if len(arreglo_L) == 0 or len(arreglo_C) == 0:
		return []

	OPT_C, prev_C, OPT_L, prev_L = crear_opt(arreglo_L, arreglo_C, costo_M)
	return reconstruccion(OPT_C, prev_C, OPT_L, prev_L)

'''
Complejidad:
	- Crear los arreglos optimos: O(n), siendo n la cantidad de meses dados.
	- Reconstruccion: O(n)
Por lo que la complejidad en tiempo resulta en:
	O(n)
'''

# ============================================================================
# EJ 12
'''
Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta Ci. También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos Gi. 

Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos. Indicar y justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda? Por ejemplo, si una campaña cuesta 100 dólares, para pasar a pesos se debe hacer la conversión de divisa.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

'''
Para el problema presentado tenemos las opciones:
	i. Elegir la campaña, achicando la brecha con el presupuesto total. (esta opcion implica que el costo (C) no debe ser mayor a la ganancia (G) ni superar el presupuesto (P))
	ii. No elegirla y mantener el presupuesto igual pasando a evaluar la siguiente.
Dado esto, podemos plantear la ecuacion de recurrencia:
	OPT[i][p] = max(OPT[i - 1][p - gasto(campañas[i])] + ganancia(campañas[i]), OPT[i - 1][p])
donde se busca maximizar la ganancia de las camapañas elegidas.
'''

def crear_opt(c_publicitaria, P):
	OPT = [[0] * (P + 1) for _ in range(len(c_publicitaria) + 1)]
	for i in range(1, len(c_publicitaria) + 1):
		for j in range(1, P + 1):
			if c_publicitaria[i - 1][1] <= j:
				OPT[i][j] = max(OPT[i - 1][j - c_publicitaria[i - 1][1]] + c_publicitaria[i - 1][0], OPT[i - 1][j])
			else:
				OPT[i][j] = OPT[i - 1][j]
	return OPT

def reconstruccion(OPT, c_publicitaria, P):
	res = []
	p = P
	for i in range(len(c_publicitaria), 0, -1):
		if OPT[i][p] != OPT[i - 1][p]:
			res.append(c_publicitaria[i - 1])
			p -= c_publicitaria[i - 1][1]
	res.reverse()
	return res

# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
	if len(c_publicitaria) == 0:
		return []
	
	OPT = crear_opt(c_publicitaria, P)
	return reconstruccion(OPT, c_publicitaria, P)

'''
Complejidad:
	- Crear OPT: O(n * m), donde n es la cantidad de campañas y m la cantidad de presupuesto.
	- Reconstruccion: O(n) + O(n) = O(n), por recorrer el largo de las campañas y luego dar vuelta la solucion.
Por lo que la complejidad en tiempo es:
	O(n * m)
'''

# ============================================================================
# EJ 13
'''
Un bodegón tiene una única mesa larga con W lugares. 
Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. 
Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. 
Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse.

Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa 
(o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar y justificar la complejidad del algoritmo.

Para esta resolución en RPL, devolver una lista con los valores de los grupos a ubicar, en el orden original en el que se encontraban en el vector P.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

'''
Suponiendo que ya hay m lugares ocupados en la mesa, para el siguiente grupo con i integrantes puedo:
	i. Agregar el grupo a la mesa, achicando la brecha con la cantidad maxima de lugares disponibles.
	ii. No agregar el grupo a la mesa, quedandome con la cantidad previa.
Por lo que podriamos plantear la ecuacion de recurrencia con una matriz de indice_grupo por cantidad_lugares:
	OPT[i][w] = max(OPT[i - 1][w - cant_lugares(OPT[i][w])] + cant_lugares(OPT[i][w]), OPT[i - 1][w])
donde se busca el maximo de lugares ocupados, siempre y cuando no supere W.
'''

def crear_opt(P, W):
	OPT = [[0] * (W + 1) for _ in range(len(P) + 1)]
	for i in range(1, len(P) + 1):
		for j in range(0, W + 1):
			if P[i - 1] <= j:
				OPT[i][j] = max(OPT[i - 1][j - P[i - 1]] + P[i - 1], OPT[i - 1][j])
			else:
				OPT[i][j] = OPT[i - 1][j]
	return OPT

def bodegon_dinamico(P, W):
	OPT = crear_opt(P, W)
	res = []
	w = W
	for grupo in range(len(P), 0, -1):
		if w == 0:
			break
		if OPT[grupo][w] != OPT[grupo - 1][w]:
			res.append(P[grupo - 1])
			w -= P[grupo - 1]
	res.reverse()
	return res

'''
Complejidad:
	- Matriz OPT: O(n * m) siendo n la cantiadad de grupos y m la cantidad maxima de lugares en la mesa.
	- Reconstruir solucion: O(n)
	- Invertir la solucion: O(n)
Por lo tanto la complejidad es:
	O(n * m) + O(n) + O(n) = O(n * m)
'''

# ============================================================================
# EJ 14
'''
Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. 
Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. 
Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. 
Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, 
y así hasta llegar a la casa n-1, que nos daría gn-1. 
Toda casa se considera adyacente a las casas i-1 e i+1.

Además, como la calle es circular, la casas 0 y n-1 también son vecinas. 
El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. 
No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. 
El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. 
Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema.

Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a 
partir de recibir un arreglo de las ganancias obtenibles. 
Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.

Para esta resolución en RPL, devolver una lista con las posiciones de las casas a robar.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica".
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

'''
Dado a que no podemos robar dos casas consecutivas podriamos plantear:
	OPT[n] = max(OPT[n - 2] + gn, OPT[n - 1])
Pero dado a que la casa 0 y n son consecutivas debemos crear dos casos:
	i- Esta incluida la casa 0 pero no la n
	ii- Esta incluida la casa n pero no la 0
Finalmente devolveriamos aquella cuya ganancia sea la mayor.
'''

def calcular_ganancias(ganancias):
	if len(ganancias) == 0:
		return []
	if len(ganancias) == 1:
		return [ganancias[0]]

	OPT = [0] * len(ganancias)
	OPT[0] = ganancias[0]
	OPT[1] = max(ganancias[0], ganancias[1])

	for i in range(2, len(ganancias)):
		OPT[i] = max(OPT[i - 2] + ganancias[i], OPT[i - 1])

	return OPT

def dias_optimos(OPT, ganancias):
	casas = []
	casa_actual = len(ganancias) - 1

	while casa_actual >= 0:
		if casa_actual > 0:
			opt_anterior = OPT[casa_actual - 1] 
		else:
			opt_anterior = 0

		if casa_actual > 1:
			opt_antes_anterior = OPT[casa_actual - 2]
		else:
			opt_antes_anterior = 0

		valor_hoy = ganancias[casa_actual]
		if valor_hoy + opt_antes_anterior >= opt_anterior:
			casas.append(casa_actual)
			casa_actual -= 2
		else:
			casa_actual -= 1

	casas.reverse()
	return casas

def lunatico(ganancias):
	if len(ganancias) == 0:
		return []
	if len(ganancias) == 1:
		return [0]

	OPT_0 = calcular_ganancias(ganancias[:-1])
	dias_0 = dias_optimos(OPT_0, ganancias[:-1])

	OPT_1 = calcular_ganancias(ganancias[1:])
	dias_1 = dias_optimos(OPT_1, ganancias[1:])
	dias_1_ajustados = []
	for dia in dias_1:
		dias_1_ajustados.append(dia + 1)

	return dias_0 if OPT_0[len(OPT_0) - 1] > OPT_1[len(OPT_1) - 1] else dias_1_ajustados

'''
Complejidad:
Dado que `calcular_ganancias` y `dias_optimos` es O(n) la complejidad resulta en:
	O(n)
ya que `lunatico` solo llama a estas funciones secuencialmente.
'''

# ============================================================================
# EJ 11
'''
Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:
	(i) aumentar el valor del operando en 1;
	(ii) duplicar el valor del operando.

Implementar un algoritmo que, por programación dinámica, obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones). 
Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo implementado.
Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'

Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

'''
Dado a que solo se pueden realizar dos operaciones para llegar al número k y se busca minimizar la cantidad de operaciones realizadas:
	OPT[n] = min(OPT[n - 1] + 1, OPT[n // 2] + 1)
Planteando esta ecuacion de recurrencia evaluamos, sobre el vector optimo OPT que almacena la cantidad de operaciones realizadas hasta el numero n, que camino nos conviene tomar con el fin de minimizar las operaciones.
'''

def calcular_OPT(k):
	OPT = [0] * (k + 1)
	prev = [0] * (k + 1)

	for n in range(1, k + 1):
		if n % 2 == 0:
			if OPT[n - 1] + 1 <= OPT[n // 2] + 1:
				OPT[n] = OPT[n - 1] + 1
				prev[n] = n - 1
			else:
				OPT[n] = OPT[n // 2] + 1
				prev[n] = n // 2
		else:
			OPT[n] = OPT[n - 1] + 1
			prev[n] = n - 1

	return OPT, prev

def reconstruir_operaciones(prev, k):
	ops = []
	n = k
	while n != 0:
		if prev[n] == n - 1:
			ops.append("mas1")
		else:
			ops.append("por2")
		n = prev[n]
	ops.reverse()
	return ops

def operaciones(k):
	OPT, prev = calcular_OPT(k)
	return reconstruir_operaciones(prev, k)
	
'''
Complejidad:
	- Se recorren los numeros hasta k para crear el arreglo OPT y para reconstruir las operaciones, ambas resultan en O(k).
Por lo que la complejidad es:
	O(k) + O(k) = O(k)
'''