# PRIMER PARCIAL - 2C2025

## Ejercicio 1
```py
def buscar_min(nodo, padre):
	if padre and nodo.valor < padre.valor and nodo.valor < nodo.hijo_izq.valor and nodo.valor < nodo.hijo_der.valor:
		return nodo

	if nodo.hijo_izq.valor < nodo.hijo_der.valor:
		return buscar_min(nodo.hijo_izq, nodo)
	else:
		return buscar_min(nodo.hijo_der, nodo)
	
	return None

def min_local(arbol):
	if len(arbol) == 0:
		return None
	elif len(arbol) == 1:
		return arbol.raiz
	return buscar_min(arbol.raiz, None)
```
La complejidad de este algoritmo se puede justificar mediante el teorema maestro dado a que se trata de un problema de divide y conquista:
	T(n) = A T(n/B) + O(f(n)) -> A >= 1 y B > 1
Donde A es la cantidad de llamadas recursivas, en este caso es 1, B por cuanto se divide el problema, en este caso por 2, y f(n) es el costo adicional por procesamiento de datos, que es este caso al solo realizar comparaciones con sus adyacentes se mantiene lineal:
	T(n) = 1T(n/2) + O(1)
Entonces como:
	O(1) = n^(log_2(1))
La complejidad en tiempo resulta O(log(n)).

## Ejercicio 2
```py
def conseguir_paradas(n, distancias, n_rober, n_por_KM):
	contador = 0
	for i in range(len(distancias)):
		if i >= len(distancias) - 2:
			continue
		if (distancias[i] + distancias[i + 1]) * n_por_KM > n_rober:
			contador += 1
			n_rober += n[i]
		n_rober -= distancias[i] * n_por_KM
	return contador

def paradas_robert(n, distancias, n_rober, n_por_KM):
	if len(distancias) == 0:
		return 0
	return conseguir_paradas(n, distancias. n_rober, n_por_KM)
```
El algoritmo implementado es greedy dado a que en cada iteracion se decide parar unicamente si no se llega a la siguientes dos paradas con las proviciones actuales, buscando el optimo local de minimizar la cantidad de paradas. Este no es un algoritmo optimo dado a que no se realiza un analisis completo de todas las estaciones con sus respectivas proviciones, un ejemplo seria:
	Comienzo con 10 de proviciones, gasto 5 por kilometro, y entre paradas hay una distancia de un kilometro. En la primer parada el oasis tiene 100 proviciones mientras que los siguientes 10.
En este caso se saltearia el primer oasis dado a que con las proviciones actuales se consigue llegar a su siguiente, pero en un caso optimo se pararia ya que es significativamente mayor la cantidad que se consiguen en comparacion con el resto, minimizando a una sola parada en caso de tener 20 oasis mientras que en el otro algoritmo pararia 10 veces.

La complejidad del algoritmo es $O(n)$ dado a que solo se recorre una vez el arreglo de distancias.

## Ejercicio 3
```py
def son_compatibles(charla1, charla2):
	return charla1[1] <= charla2[0]

def backtracking(charlas, indice, a_dar):
	if indice == len(charlas):
		return a_dar.copy()

	charla = charlas[indice]

	agrego = None
	if not a_dar or son_compatibles(a_dar[indice - 1], charlas[indice]):
		a_dar.append(charla)
		agrego = backtracking(charlas, indice + 1, a_dar)
		a_dar.pop()

	salteo = backtracking(charlas, indice + 1, a_dar)

	mejor = None
	if agrego is not None and (mejor is None or len(agrego) > len(mejor)):
		mejor = agrego
	elif salteo is not None and (mejor is None or len(salteo) > len(mejor)):
		mejor = salteo
	return mejor

def scheduling(charlas):
	if len(charlas) == 0:
		return []
	elif len(charlas) == 1:
		return [charlas[0]]
	charlas_ord = sorted(charlas, key=lambda x: x[0])
	return backtracking(charlas_ord, 0, [])
```

## Ejercicio 4
Dado el problema, por cada iteracion se pueden plantear dos posibilidades:
	i. Agregar el elemento a la mochila, achicando la brecha con el peso total (W) y con su presupuesto (P).
	ii. No agregar el elemento a la mochila, manteniendo el peso (w) y presupuesto (p) anterior.
Por lo que se puede plantear una ecuacion de recurrencia de la forma:
	OPT[i][w][p] = max(OPT[i - 1][w - peso(elem_i)][p - precio(elem_i)] + valor(elem_i), OPT[i - 1][w][p])

```py
def crear_opt(productos, W, P):
	OPT = [[0] * (W + 1) for _ in range(len(productos) + 1) for _ in range(P + 1)]
	for i in range(1, len(productos) + 1):
		valor, precio, peso = productos[i - 1]
		for j in range(W + 1):
			for k in range(P + 1):
				if peso <= j and precio <= k:
					OPT[i][j][k] = max(OPT[i - 1][j - peso][k - precio] + valor, OPT[i - 1][j][k])
				else:
					OPT[i][j][k] = OPT[i - 1][j][k]
	return OPT

def laura_compra(productos, W, P):
	if len(productos) == 0:
		return []
	OPT = crear_opt(productos, W, P)
	res = []
	w = W
	p = P
	for i in range(len(productos) - 1, -1, -1):
		valor, precio, peso = productos[i]
		if OPT[i][w][p] != OPT[i - 1][w][p]:
			res.append(OPT[i][w][p])
			w -= peso
			p -= precio
	res.reverse()
	return res
```

Complejidad:
	- Crear la matriz OPT: O(n * W * P), siendo n la cantidad de productos, W el peso total, y P el presupuesto total.
	- Reconstruccion: O(n) + O(n) -> (recorrer los productos) + (reverse la solucion)
Por lo que la complejidad final es:
	O(n * W * P) + O(n) + O(n) = O(n * W * P)