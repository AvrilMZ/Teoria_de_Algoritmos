# PARCIAL - 1C2024

## Ejercicio 1
```py
def buscar_elem(elementos, W, K, i, temp, peso_temp):
	if i == len(elementos):
		if len(temp) >= K:
			return temp.copy()
		else:
			return []
	
	actual = elementos[i]
	valor, peso = actual
	agrego = []
	if peso_temp + peso <= W:
		temp.append(actual)
		agrego = buscar_elem(elementos, W, K, i + 1, temp, peso_temp + peso)
		temp.pop()
	
	salteo = buscar_elem(elementos, W, K, i + 1, temp, peso_temp)

	if len(agrego) >= K and sum(x[0] for x in agrego) > sum(x[0] for x in salteo):
		return agrego
	if len(salteo) >= K:
		return salteo
	return []

def mochila(elementos, W, K):
	if K == 0:
		return []
	elif K > len(elementos):
		return []
	return buscar_elem(elementos, W, K, 0, [], 0)
```


## Ejercicio 2
(SEGUNDO PARCIAL)


## Ejercicio 3
Para este problema podemos pensar ¿vendo o no vendo hoy?:
- La mejor solución hasta el día $i - 1$ (no vendo);
- La mejor ganancia vendiendo exactamente en el día $i$ (vendo).

Por lo que la ecuacion de recurrencia seria:
- $OPT[i] = max(OPT[i - 1], p[i] - (min_precio_hasta_i - 1))$

```py
def crear_opt(p):
	OPT = [0] * len(p)

	min_precio = p[0]
	min_dia = 0
	dia_compra = 0
	dia_venta = 0

	for i in range(1, len(p)):
		if p[i] - min_precio > OPT[i - 1]:
			OPT[i] = p[i] - min_precio
			if OPT[i] > OPT[dia_venta]:
				dia_compra = min_dia
				dia_venta = i
		else:
			OPT[i] = OPT[i - 1]

		if p[i] < min_precio:
			min_precio = p[i]
			min_dia = i

	return OPT, (dia_compra, dia_venta)

def compra_venta(p):
	if len(p) < 2:
		return (0, 0)
	OPT, res = crear_opt(p)
	return res
```
**Complejidad**

- $O(n)$, siendo $n$ la cantidad de predicciones del arreglo.


## Ejercicio 4
(SEGUNDO PARCIAL)


## Ejercicio 5
```py
def _buscar_dias(izq, der):
	
	
def buscar_dias(predi):
	if len(predi) <= 1:
		return predi

	
```
**Complejidad**

