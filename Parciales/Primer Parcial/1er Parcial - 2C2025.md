# PRIMER PARCIAL - 2C2025

## Ejercicio 1
```py
def es_max(matriz, f, c):
	max_pos = (f, c)
	for i in range(f - 1, f + 2): # O(k)   
		for j in range(c - 1, c + 2):  # O(k)
 			if (i, j) == (f, c):
				continue
			if matriz[i][j] > matriz[f][c]:
				max_pos = (i, j)
	return max_pos
# k -> cant. de adyacentes; constante -> no empeora la complejidad total

def _buscar_max(matriz, c_inicio, c_fin):
	if c_inicio > c_fin:
		return None

	medio = (c_inicio + c_fin) // 2
	fila_max = float("-inf")
	for i in range(len(matriz)):
		if matriz[i][medio] > fila_max:
			fila_max = matriz[i][medio]

	f_m, c_m = es_max(matriz, fila_max, medio)
	if (f_m, c_m) == (fila_max, medio):
		return matriz[fila_max][medio]
	if c_m > medio:
		return _buscar_max(matriz, medio + 1, c_fin)
	return _buscar_max(matriz, c_inicio, medio)

def buscar_max(matriz):
	return _buscar_max(matriz, 0, len(matriz))
```
**Complejidad**

Teniendo en cuenta el teorema maestro:  
- $T(n) = A \cdot T(\frac{n}{B}) + O(f(n)) \rightarrow A \ge 1, B \gt 1$

Dado que en nuestro problema tenemos:  
- $A = 1$ (cantidad de llamadas recursivas)  
- $B = 2$ (tamaño de los subproblemas respecto al problema original)  
- $O(f(n)) = O(n) = (C = 1)$ (Costo adicional)

Por lo tanto:  
- $T(n) = 1 \cdot T(\frac{n}{2}) + O(n)$  
- $O(n) > n^{\log_2(1)}$

Resultando en:  
- $T(n) = O(n)$


## Ejercicio 2
```python
def determinar_intervalos(intervalos):
    i_ordenados = sorted(intervalos, key=lambda x : x[0])

    mejor_inicio = i_ordenados[0][0]
    mejor_fin = i_ordenados[0][1]

    solucion = []
    for intervalo in i_ordenados: 
        inicio, fin = intervalo
        if inicio > mejor_fin:
            solucion.append(mejor_inicio, mejor_fin)
            mejor_inicio = inicio
            mejor_fin = fin
        elif (inicio > mejor_inicio and inicio < mejor_fin) and (fin > mejor_fin):
            mejor_fin = fin

    return solucion
```
**Complejidad**

- Ordenar el arreglo: $O(n \cdot \log(n))$
- Dado que se recorren todos los intervalos una vez, verificando si se encuentran contenidos en el ultimo agregado: $O(n)$

Por lo que la complejidad resulta en:
- $O(n \cdot \log(n))$

**Regla greedy**

En cada iteración intento que el intervalo actual sea lo más grande posible con el objetivo de minimizar la cantidad de intervalos restantes, consiguiendo un óptimo local. Esto se logra teniendo en cuenta que el inicio del intervalo recibido sea mayor al final de mi intervalo actual, donde para optimizar esta logica, se realiza un ordenamiento por valor de inicio.  
El algoritmo es **óptimo** ya que por cada iteracion muta o mantene los limites del intervalo para minimizar la cantidad final, si arrancaramos en el intervalo $n$ siempre obtendriamos la misma solucion.


## Ejercicio 3
```py
def reconstruir_ciclo(padre, inicio, fin):
    v = fin
    camino = []
    while v != inicio:
        camino.append(v)
        v = padre[v]
    camino.append(inicio)
    return camino[::-1]

def devolver_ciclo(grafo, v, visitados, padre): # Se puede simplificar
    visitados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            padre[w] = v
            ciclo = devolver_ciclo(grafo, w, visitados, padre)
            if ciclo is not None:
                return ciclo
        elif padre.get(v) != w:
            return reconstruir_ciclo(padre, w, v)
    return None # Si llega a esta linea es porque el grafo no tiene ciclos

def existe_ciclo(grafo): # DFS completo por si es un grafo que tenga mas de una componente conexa
    visitados = set()
    padre = {}
    for v in grafo:
        if v not in visitados: # Origen de la primera (o única) componente conexa
            ciclo = devolver_ciclo(grafo, v, visitados, padre) # DFS para cada componente
            if ciclo is not None:
                return True
    return False

def _buscar_fvs(grafo, vertices, indice, parcial, mejor):
    sol_m, sum_m = mejor
    sol_p, sum_p = parcial

	if indice == len(vertices):
        copia = grafo.copy()
        for v in sol_parcial:
            copia.borrar_vertice(v)
        if not existe_ciclo(copia):
            if mejor is None or sum_p < sum_m:
                sol_m = sol_parcial.copy()
                sum_m = sum_p
        return sol_m, sum_m

    sol_p.append(vertices[indice])
    sol_p += grafo.valor(vertices[indice])
    sol_m, sum_m = _buscar_fvs(grafo, vertices, indice + 1, (sol_p, sum_p), (sol_m, sum_m))
    sol_p.pop()
    sol_p -= grafo.valor(vertices[indice])

    sol_m, sum_m = _buscar_fvs(grafo, vertices, indice + 1, (sol_p, sum_p), (sol_m, sum_m))

    return sol_m, sum_m

def buscar_fvs(grafo):
	mejor = None
	_buscar_fvs(grafo, grafo.obtener_vertices(), 0, ([], 0), (mejor, 0))
	return mejor
```


## Ejercicio 4
Para contar la cantidad de formas diferentes para conseguir dicho cambio podemos tomar la cantidad de combinaciones obtenidas de todas las combinaciones anteriores y agregar las actuales:
- $OPT[n] = OPT[n] + OPT[n - i]$

Donde $i$ son todas las monedas posibles hasta $n$.  

```py
def formas(monedas, monto):
    OPT = [0] * (monto + 1)
    OPT[0] = 1
    for moneda in monedas:
        for i in range(moneda, monto + 1): # Desde moneda ya que no tendria sentido contar las formas por debajo del monto del billete ya que seria 0. -> ej: billete 100, para monto 1 = 0, monto 2 = 0, ..., monto 99 = 0
            OPT[i] += OPT[i - moneda]
    return OPT[monto]
```
**Complejidad**

Dado que por cada moneda se recorren todos los valores hasta el monto:
- $O(c \cdot m)$, siendo $c$ la cantidad de monedas y $m$ el monto.