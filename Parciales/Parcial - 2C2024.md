# PARCIAL - 2C2024

## Ejercicio 1
```py
def cubre_otro(matriz, i, j):
	for f in range(max(0, i - 2), min(len(matriz[0]), i + 3)):
		for c in range(max(0, j - 2), min(len(matriz[0]), j + 3)):
			if matriz[f][c]:
				return True
	return False

def colocar_guardias(matriz):
	for i in range(matriz[0]):
		for j in range(matriz):
			if not matriz[i][j] and not cubre_otro(matriz, i, j):
				matriz[i][j] = True
	return matriz
```
Complejidad:
Se itera la matriz posicion por posicion (O(n * m)) y en caso de encontrar una posicion vacia se itera una submatriz de radio dos para verificar si existe un guardia que superponga el radio de vigilancia (O(f * c)). Dado a que la submatriz es mas chica que la original su complejidad queda incluida en O(n * m) por ser cota superior.
Por lo que la complejidad resulta en:
	O(n * m)

Es un algoritmo greedy ya que dada una matriz con guardias en ella se itera cada celda y en caso de no haber un guardia se verifica si es posible agregar uno en esa posición, verificando si otro cubre al área adyacente. Esta tecnica busca maximizar el área cubierta sin superposicion y cantidad de guardias puestos brindando el optimo local de cubrir una posicion vacia al encontrarla. Este algoritmo es optimo, ya que se busca agregar la mayor cantidad de guardias, y dado a que se recorren todas las posiciones verificando el area cubierta, no habria manera de poner mas sin reubicar los guardias ya dados. En el caso de querer maximizar el area cubierta con la menor cantidad de guardias posibles ahi si que no seria optimo ya que dada una matriz vacia se colocaria el primer guardia en la posicion (0,0) cuando deberia colocarse en la (1,1).

## Ejercicio 2
```py
def buscar_cambio(n, monedas, cantidad_x_monedas, i, i_moneda, actual, sum_actual):
	if i == len(monedas) or sum_actual + monedas[i] > n:
		return actual.copy()
	
	moneda = monedas[i]
	agrego = []
	if i_moneda <= cantidad_x_monedas[f"{moneda}"]:
		actual.append(moneda)
		agrego = buscar_cambio(n, monedas, cantidad_x_monedas, i, i_moneda + 1, actual, sum_actual + moneda)
		actual.pop()

	salteo = buscar_cambio(n, monedas, cantidad_x_monedas, i + 1, 0, actual, sum_actual)

	if len(agrego) <= len(salteo):
		return agrego
	return salteo

def cambio(n, monedas, cantidad_x_monedas):
	if n == 0:
		return []
	if n == 1:
		return [1]
	return buscar_cambio(n, monedas, cantidad_x_monedas, 0, 0, [], 0)
```

## Ejercicio 3
(SEGUNDO PARCIAL)

## Ejercicio 4
```py

```

## Ejercicio 5
Para ir formando el camino con peso maximo debemos considerar cada vertice adyacente del vertice actual y quedarnos con aquel cuyo peso sea mayor. Es asi que podemos plantear la ecuacion de recurrencia:
	OPT[n] = OPT[n - 1] + peso(n)
donde n es el vecino con peso maximo de n - 1.

```py
def buscar_camino(grafo, )

def camino_max(grafo, s, t):
```

DUDOSO