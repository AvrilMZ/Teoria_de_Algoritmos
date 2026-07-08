'''
Manejamos un negocio que atiende clientes en Londres y en California. Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: L y C, con valores para todos los meses hasta n. Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo M por la mudanza. 

Dados los arreglos de costos de operación en Londres (L) y California (C), indicar la secuencia de las n localizaciones en las que operar durante los n meses, sabiendo que queremos minimizar el total de los costos de operación. Se puede empezar en cualquier ciudad. Indicar y justificar la complejidad del algoritmo implementado.
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