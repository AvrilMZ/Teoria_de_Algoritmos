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
	OPT[i][w] = max(OPT[i - 1][w - peso(elem_i)] + (valor(elem_i), precio(elem_i)), OPT[i - 1][w])
Esto es siempre y cuando OPT[i - 1][w - peso(elem_i)] + (valor(elem_i), precio(elem_i)) <= P.

```py
def crear_opt(productos, W):
	OPT = [[0] * (W + 1) for _ in range(len(productos + 1))]
	for i in range(1, len(productos) + 1):
		valor, precio, peso = productos[i]
		for j in range(0, W + 1):
			if j <= W:
				OPT[i][j] = max(OPT[i - 1][j - peso] + (valor, precio), OPT[i - 1][j])
			else:
				OPT[i][j] = max(OPT[i - 1][j], OPT[i][j] + (valor, precio))
	return OPT

def reconstruccion(OPT, W, P):
	res = []
	p = P
	w = W
	for i in range(len(OPT) + 1):
		valor, precio = OPT[i][w]
		if 

def laura_compra(productos, W, P):
	if len(productos) == 0:
		return []
	OPT = crear_opt(productos, W)
	
```