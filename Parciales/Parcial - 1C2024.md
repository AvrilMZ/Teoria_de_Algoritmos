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
Para este problema nos conviene "forzar" a que se compre la casa en un dia, luego en otro y comparar las ganancias quedandome con la mayor:
	OPT[j] = 
```py

```

## Ejercicio 4
(SEGUNDO PARCIAL)

## Ejercicio 5
```py
def buscar_min(predi):
	if len(predi) <= 1:
		return predi

	medio = len(predi) // 2
	izq = buscar_min(predi[medio:])
	der = buscar_min(predi[:medio])

	if izq[0] 


def buscar_dias(predi):
	if len(predi) < 2:
		return []
	

```