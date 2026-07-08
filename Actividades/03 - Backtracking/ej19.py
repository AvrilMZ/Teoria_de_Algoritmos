'''
Implementar un algoritmo que, utilizando backtracking, resuelva el problema del cambio (obtener la forma de dar cambio en la mínima cantidad de monedas) con una nueva restricción: no se tiene una cantidad indefinida de cada moneda, sino una cantidad específica (y esto hace que pueda no haber solución). Suponer que la función a invocar es `cambio(n, monedas, cantidad_x_monedas)`, donde `n` sea el valor a devolver en cambio, `monedas` sea una lista ordenada de los valores de las monedas, y `cantidad_x_monedas` un diccionario.
'''

def obtener_cambio(n, monedas, cantidad_x_monedas, suma_restante, cambio_actual, i_moneda, mejor_sol):
	billetes, suma = cambio_actual
	if suma == n:
		if mejor_sol[0] is None or len(billetes) < len(mejor_sol[0]):
			mejor_sol[0] = billetes.copy()
		return
	
	if suma + suma_restante < n or suma + monedas[i_moneda] > n: # Poda
		return

	for i in range(cantidad_x_monedas[monedas[i_moneda]] + 1): # + 1 para contar el caso 0 (que no se agrega ninguna moneda) y el ultimo
		monto = monedas[i_moneda] * i

		if suma + monto > n: # Poda
			break
		
		for _ in range(i):
			suma_restante -= monedas[i_moneda]
			billetes.append(monedas[i_moneda])
			suma += monedas[i_moneda]

		obtener_cambio(n, monedas, cantidad_x_monedas, suma_restante, (billetes, suma), i_moneda + 1, mejor_sol)

		for _ in range(i):
			suma_restante += monedas[i_moneda]
			billetes.pop()
			suma -= monedas[i_moneda]

def cambio(n, monedas, cantidad_x_monedas):
	suma_total = 0
	total_billetes = []
	for m in cantidad_x_monedas:
		suma_total += (m * cantidad_x_monedas[m])
		for _ in range(cantidad_x_monedas[m]):
			total_billetes.append(m)
	if suma_total < n:
		return []
	elif suma_total == n:
		return total_billetes

	mejor_sol = [None]
	obtener_cambio(n, monedas, cantidad_x_monedas, suma_total, ([], 0), 0, mejor_sol)
	return [] if mejor_sol[0] is None else mejor_sol[0]