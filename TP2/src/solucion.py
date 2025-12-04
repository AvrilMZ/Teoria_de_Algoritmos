ATACAR = "Atacar"
CARGAR = "Cargar"


def crear_m(enemigos: list[int], calcular_muertos: list[int]):
	M = [0] * (len(enemigos) + 1)
	for ultima_oleada in range(1, len(enemigos) + 1):
		# Puedo no haber atacado nunca
		maximo = min(calcular_muertos[ultima_oleada - 1], enemigos[ultima_oleada - 1])
		# O, habiendo atacado antes, atacar
		for ultimo_ataque in range(1, ultima_oleada):
			muertos = M[ultimo_ataque] + min(calcular_muertos[ultima_oleada-ultimo_ataque - 1], enemigos[ultima_oleada - 1])
			if muertos > maximo:
				maximo = muertos 
		M[ultima_oleada] = maximo
	return M

def rec(enemigos: list[int], calcular_muertos: list[int]):
	M = crear_m(enemigos, calcular_muertos)
	
	oleada_actual = len(enemigos)
	acciones = []
	while oleada_actual > 0:
		valor_no_atacar = min(calcular_muertos[oleada_actual - 1], enemigos[oleada_actual - 1])
		ultimo_ataque = 0
		
		for posible_ultimo_ataque in range(1, oleada_actual):
			valor_atacar = M[posible_ultimo_ataque] + min(calcular_muertos[oleada_actual - posible_ultimo_ataque - 1], enemigos[oleada_actual - 1])
			if valor_atacar > valor_no_atacar:
				valor_no_atacar = valor_atacar
				ultimo_ataque = posible_ultimo_ataque

		num_cargas = oleada_actual - ultimo_ataque - 1 # Cantidad de cargas necesarias antes de atacar
		if num_cargas < 0:
			num_cargas = 0
			
		acciones.append(ATACAR)
		for _ in range(num_cargas):
			acciones.append(CARGAR)

		oleada_actual = ultimo_ataque
	
	acciones.reverse()
	return acciones, M[len(enemigos)]


def crear_m_oleada(enemigos: list[int], calcular_muertos: list[int]):
	M = [0] * (len(enemigos) + 1)
	prev = [0] * (len(enemigos) + 1)
	for ultima_oleada in range(1, len(enemigos) + 1):
		maximo = min(calcular_muertos[ultima_oleada - 1], enemigos[ultima_oleada - 1])
		prev[ultima_oleada] = 0
		for ultimo_ataque in range(1, ultima_oleada):
			muertos = M[ultimo_ataque] + min(calcular_muertos[(ultima_oleada - ultimo_ataque) - 1], enemigos[ultima_oleada - 1])
			if muertos > maximo:
				maximo = muertos
				prev[ultima_oleada] = ultimo_ataque # Guardo cuando ataque
		M[ultima_oleada] = maximo
	return M, prev

def rec_oleada(enemigos: list[int], calcular_muertos: list[int]):
	M, prev = crear_m_oleada(enemigos, calcular_muertos)

	oleada_actual = len(enemigos)
	acciones = []

	while oleada_actual > 0:
		ultimo_ataque = prev[oleada_actual]

		num_cargas = oleada_actual - ultimo_ataque - 1 # Cantidad de cargas necesarias antes de atacar
		if num_cargas < 0:
			num_cargas = 0
			
		acciones.append(ATACAR)
		for _ in range(num_cargas):
			acciones.append(CARGAR)

		oleada_actual = ultimo_ataque

	acciones.reverse()
	return acciones, M[len(enemigos)]
