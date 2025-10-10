'''
Se define que el mejor alineamiento entre dos cadenas es aquel que minimice la Distancia de Edición. El criterio será:
	- Por cada par de letras que coinciden en el alineamiento, no hay costo
	- Existe la penalidad δ que refiere a no alinear las letras. Una brecha (gap)
	- Por cada par de letras que no coinciden hay un costo \alpha(xi,yj) según la diferencia entre las letras xi y yj. Por ejemplo, el costo al alinear V y B puede ser bajo, para considerar su parecido y cercanía en el teclado.
	- El costo total del alineamiento seleccionado es la suma total de todos los costos pagados por brechas y por costo de reemplazo (cambiar letras)
Calcular la Distancia de Edición significa encontrar el alineamiento óptimo, tal que se minimice el valor de la distancia de edición, es decir, minimizar la sumatoria de costos de brechas y de reemplazos. Encontrar dicho alineamiento entre dos cadenas X e Y, plantear la ecuacion de recurrencia e implementar un algoritmo que minimice su distancia de edicion.
'''

'''
Para este problema tenemos cuatro posibilidades:
	- Que coincidan las letras de ambas cadenas;
	- Que difieran, por haber letras distintas, y haya que reemplazar;
	- Que difieran, por haber espacio vacio, y haya que insertar;
	- Que difieran, por haber letra demas, y haya que eliminar.
Para esto se puede plantear la ecuacion de recurrencia:
	OPT[i][j] = min{ OPT[i - 1][j - 1],
			 OPT[i - 1][j - 1] + (costo_reemplazo),
			 OPT[i][j - 1] + (costo_brecha),
			 OPT[i - 1][j] + (costo_brecha)}
'''

def distancia_edicion(X, Y, costo_reemplazo, costo_brecha):
	OPT = [[0] * (len(Y) + 1) for _ in range(len(X) + 1)]

	for i in range(len(X) + 1):
		OPT[i][0] = i * costo_brecha
	for j in range(len(Y) + 1):
		OPT[0][j] = j * costo_brecha

	for i in range(1, len(X) + 1):
		for j in range(1, len(Y) + 1):
			if X[i - 1] == Y[j - 1]:
				costo = 0
			else:
				costo = costo_reemplazo
			OPT[i][j] = min(
				OPT[i - 1][j - 1] + costo,
				OPT[i][j - 1] + costo_brecha,
				OPT[i - 1][j] + costo_brecha)
			
	return OPT[len(X)][len(Y)]

'''
Complejidad:
	- O(n * m), siendo n la cantidad de caracteres de la cadena X y m la cantidad de caracteres de la cadena Y.
'''