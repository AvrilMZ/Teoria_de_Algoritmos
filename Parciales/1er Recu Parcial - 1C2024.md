# PRIMER RECUPERATORIO PARCIAL - 1C2024

## Ejercicio 1
```py
def eliminar_camino(grafo, camino, v, w):
	copia = grafo.copy()
	for vertice in camino:
		if vertice != v and vertice != w:
			copia.borrar_vertice(vertice)
	return copia

def buscar_camino(grafo, visitados, actual, w, camino):
	if actual == w:
		camino.append(w)
		return camino.copy()

	if all(vecino in visitados for vecino in grafo.adyacentes(actual)): # Poda: camino sin salida a 'w'
		return None
	
	for vecino in grafo.adyacentes(actual):
		if vecino not in visitados:
			visitados.append(vecino)
			camino.append(vecino)
			resultado = buscar_camino(grafo, visitados, vecino, w, camino)
			if resultado is not None:
				return resultado
			camino.pop()
			visitados.pop()

	return None

def caminos_disjuntos(grafo, v, w):
	grafo_en_uso = grafo
	caminos = []
	while True:
		visitados = [v]
		opcion = [v]
		salida = buscar_camino(grafo_en_uso, visitados, v, w, opcion)
		if salida is None:
			break
		caminos.append(salida)
		grafo_en_uso = eliminar_camino(grafo, salida, v, w)
	return caminos
```
**Complejidad**

Dado que por cada busqueda se recorrio mediante backtracking nuevamente el grafo:
- Cantidad de caminos entre `v` y `w` vertices: $O(2^n)$, queda como cota superior ya que en las llamadas siguientes a la primera el grafo se reduce.
- Copia y eliminacion de vertices: $O(n)$

Resultando en:
- $O(2^n * n)$

## Ejercicio 2
```py
# heladeras = [(c_1,c_2)(c_3)] -> donde cada c_i tiene su valor de perdida
def mover_c(heladeras):
	if len(heladeras) == 0 or len(heladeras) == 1:
		return 0

	heladeras_ord = sorted(heladeras, key=lambda x: len(x))

	perdida = 0
	for heladera in len(0, len(heladeras) - 1):
		perdida += sum(heladera)

	return perdida
```
**Complejidad**

- Ordenar el arreglo por longitud de componentes en cada heladera: $O(n \cdot \log(n))$.  
- Recorrer cada heladera sumando al acumulado la perdida correspondiente de cada heladera menos la ultima: $O(n - 1)$.

Por lo que la complejidad final resulta en:  
- $O(n \cdot \log(n)) + O(n - 1) = O(n \cdot \log(n))$

Este algoritmo es greedy dado a que por cada iteracion se busca mover la menor cantidad de elementos (óptimo local) para minimizar la cantidad de perdia, es asi que la ultima heladera (osea la que preservamos) es la que mas elementos tiene. No es un algoritmo óptimo ya que no se tiene en cuenta la perdida de cada elemento, puede pasar que haya una heladera con un elemento de perdida 100 y luego otra mucho mas adelante con 10 elementos y cada uno con perdida de 1, por lo que mover ese elemento mas grande afectaria negativamente la suma acumulada.

## Ejercicio 3
(SEGUNDO PARCIAL)

## Ejercicio 4
Dado a que se pueden repetir elementos la ecuacion de recurrencia es igual a la de la mochila solo que con una leve modificacion:
- $OPT[n][w] = \max(OPT[n][w - peso(elem[n])] + valor(elem[n]), OPT[n - 1][w])$

En este caso no haria falta cambiar de fila en caso de agregar el elemento porque podemos volver a usarlo.

```py
def crear_opt(elementos, W):
	OPT = [[0] * (W + 1) for _ in range(len(elementos) + 1)]
	for i in range(1, len(elementos) + 1):
		valor, peso = elementos[i - 1]
		for j in range(W + 1):
			if peso <= j:
				OPT[i][j] = max(OPT[i][j - peso] + valor, OPT[i - 1][j])
			else:
				OPT[i][j] = OPT[i - 1][j]
	return OPT

def mochila(elementos, W):
	OPT = crear_opt(elementos, W)
	res = []
	w = W
	for i in range(len(elementos), 0, -1):
		if OPT[i][w] != OPT[i - 1][w]:
			res.append(elementos[i])
			w -= elementos[i - 1][1]
	res.reverse()
	return res
```
**Complejidad**

- Crear matriz OPT: $O(n * m)$, siendo n la cantidad de elementos y m el peso maximo
- Reconstruccion: $O(n) + O(n)$ -> (recorrer los elementos) + (reverse)

Por lo que la complejidad resulta en:  
- $O(n \cdot m) + O(n) + O(n) = O(n \cdot m)$

## Ejercicio 5
$P_i$: "Variable continua, precio del dia $i$"  
$X_i$: "Variable binaria, compro en el dia $i$"  
$Y_i$: "Varaible binaria, vendo en el dia $i$"  

$\max{\sum_{j}^{n}(P_j \cdot Y_j) - \sum_{i}^{j}(P_i \cdot X_i)}$ -> maximizar la ganancia de la venta del inmueble

Donde:  
- $\sum_{i = 0}^{n} X_i = 1$ -> Solo se puede comprar un dia  
- $\sum_{i = 0}^{n} Y_i = 1$ -> Solo se puede vender un dia  
- $\sum_{j}(j \cdot Y_j) > \sum_{i}(i \cdot X_i)$ -> El dia de venta debe ser posterior al dia de compra (hacemos esto ya que $j > i$ no se puede plantear debido a que $j$ e $i$ no son variables)