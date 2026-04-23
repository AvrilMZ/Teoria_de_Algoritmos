# RECUPERATORIO PRIMER PARCIAL - 2C2025

## Ejercicio 1
```py
def merge(izq, der):
        resul = []
        i = 0
        j = 0
        while len(izq) > i and len(der) > j:
                if izq[i] <= der[j]:
                        resul.append(izq[i])
                        i += 1
                else:
                        resul.append(der[j])
                        j += 1

        resul.extend(izq[i:])
        resul.extend(der[j:])
        return resul

def ordenar(arr):
        if len(arr) <= 1:
                return arr[0]
        
        medio = len(arr) // 2
        izq = merge_ordenar(arr[:medio])
        der = merge_ordenar(arr[medio:])

        return merge(izq, der)
```
Para calcular la complejidad no podriamos utilizar el teorema maestro la recurrencia queda expresada en función de $K$, pero el costo de combinación depende de $n = K \cdot H$, por lo que no se obtiene una función en una sola variable.  
La complejidad del algoritmo seria $O(n log(K))$ dado que se dividen las $K$ listas en mitades y luego se realizan los merges linealmente.

# Ejercicio 2
```py
# catalogo = [(producto1,precio1,cantidad1),(producto2,precio2,cantidad2),...]
def robo(catalogo, L):
        cata_ord = sorted(catalogo, lambda x:x[1], reverse=True)
        resul = []
        restante = L
        for producto, precio, cant in cata_ord:
                if restante - cant >= 0:
                        resul.append((producto, cant))
                        restante -= cant
                else:
                        resul.append((producto, restante))
                        break
        return resul
```
El algoritmo propuesto es greedy dado que en cada iteracion se busca el óptimo local maximizando el precio a obtener cuando se vendan los farmacos robados. Es óptimo ya que no existe mejor manera de ir recorriendo los productos y consiguiendo mejores combinaciones que mejoren el precio de venta, ya que inicialmente se ordena el arreglo del catalogo por precios descendentes para asegurarnos de esto.

Complejidad:  
- Ordenar: $O(n log(n))$
- Recorrer: $O(n)$  
Por lo tanto la complejidad final resulta en $O(n log(n))$ por ser cota superior a $O(n)$.

# Ejercicio 3
```py
def fes_bt(grafo, vertices, aristas, indice, actual, mejor):
        if indice == len(aristas):
                nuevo = eliminar_aristas(grafo.copy(), actual)
                if not tiene_ciclo(nuevo, vertices) and (mejor is None or len(actual) < len(mejor)):
                        mejor = actual[:]
                return mejor
        
        actual.append(aristas[indice])
        mejor = fes_bt(grafo, vertices, aristas, indice + 1, actual, mejor)
        actual.pop()

        mejor = fes_bt(grafo, vertices, aristas, indice + 1, actual, mejor)

        return mejor

def fes(grafo):
        sol = []
        vertices = grafo.obtener_vertices()
        cc = componentes_debilmente_conexas(grafo, vertices)
        for componente in cc:
                aristas = []
                for v in componente:
                        for vecino in grafo.adyacentes(v):
                                if (v, vecino) not in aristas:
                                aristas.append((v, vecino))
                if aristas:
                        mejor = fes_bt(grafo, componente, aristas, 0, [], None)
                        if not mejor:
                                continue
                        sol.extend(mejor)
        return sol
```

# Ejercicio 4
Para resolver el problema de independent set podemos plantear la siguiente ecuacion de recurrencia para la solucion optima de la posicion n:

- $OPT[n] = \max(OPT[n - 1], OPT[n - 2] + grafo.valor(n))$

Dado que si tomamos como parte de nuestra solucion al vertice anterior no podriamos incluir al actual, y si tomaramos al actual podriamos tomar al de dos posiciones anteriores. La decision de cual elegir se define por aquel que maximice la suma de los valores de los vertices de la solucion.

```py
def opt(grafo, vertices):
        OPT = [0] * len(vertices)
        OPT[0] = grafo.valor(vertices[0])
        OPT[1] = max(OPT[0], grafo.valor(vertices[1]))
        for i in range(2, len(vertices)):
                valor = grafo.valor(vertices[i])
                OPT[i] = max(OPT[i - 1], OPT[i - 2] + valor)
        return OPT

def ind_set(grafo):
        vertices = grafo.obtener_vertices()
        OPT = opt(grafo, vertices)

        rec = []
        i = len(vertices) - 1
        while i >= 0:
                if i < 0:
                        anterior = 0
                else:
                        anterior = OPT[i - 1]

                if i < 1:
                        antepenultimo = 0 
                else:
                        antepenultimo = OPT[i - 2]
                        
                if OPT[i] + antepenultimo > anterior:
                        rec.append(vertices[i])
                        i -= 2
                else:
                        i -= 1

        rec.reverse()
        return rec
```
Complejidad:
- PD: $O(n)$ ya que solo recorremos todos los elementos 1 vez.
- Reconstrucción: $O(n)$ ya que solo recorremos todos los elementos 1 vez. 