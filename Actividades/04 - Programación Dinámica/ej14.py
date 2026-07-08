'''
Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g_0, la casa a su derecha es la 1, que nos daría g_1, y así hasta llegar a la casa n-1, que nos daría g_{n-1}. Toda casa se considera adyacente a las casas i-1 e i+1.

Además, como la calle es circular, la casas 0 y n-1 también son vecinas. El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema.

Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.
'''

'''
Dado a que no podemos robar dos casas consecutivas podriamos plantear:
	OPT[n] = max(OPT[n - 2] + g_n, OPT[n - 1])
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