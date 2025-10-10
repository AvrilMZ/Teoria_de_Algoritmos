'''
Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. 
El listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde está ubicada cada una. 
Se desea ubicar la menor cantidad de policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km.
Justificar que la solución es óptima. Indicar y justificar la complejidad del algoritmo implementado.

Ejemplo:
	| Ciudad      | Bifurcación |
	|-------------|-------------|
	| Castelli    | 185         |
	| Gral Guido  | 242         |
	| Lezama      | 156         |
	| Maipú       | 270         |
	| Sevigne     | 194         |

Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. 
Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral Guido. 
Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50km.
En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única solución óptima sería colocar un móvil policial en Sevigne.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción.
'''

def ciudad_cubierta(patrulleros, km):
	if len(patrulleros) == 0:
		return False

	ultima_patrulla = patrulleros[len(patrulleros) - 1]
	_, p_km = ultima_patrulla
	if p_km - km >= 0 and p_km - km <= 50:
		return True
	elif km - p_km >= 0 and km - p_km <= 50:
		return True
	
	return False

def bifurcaciones_con_patrulla(ciudades):
	if len(ciudades) == 1:
		return [ciudades[0]]

	ciudades_ord = sorted(ciudades, key=lambda x: x[1])
	patrulleros = []

	for i in range(0, len(ciudades_ord)):
		c, km = ciudades_ord[i]
		if not ciudad_cubierta(patrulleros, km):
			if i == len(ciudades_ord) - 1:
				patrulleros.append((c, km))
				continue

			c_p, km_p = ciudades_ord[i + 1]
			if km_p - km > 50:
				patrulleros.append((c, km))
			else:
				patrulleros.append((c_p, km_p))		

	return patrulleros

'''
Complejidad:
	- Ordenar las ciudades: O(n*log(n))
	- Recorrer las ciudades: O(n)
	- Verficar si la ciudad esta cubierta: O(1)
Por lo que la complejidad resulta en:
	O(n*log(n))

La solución es óptima porque inductivamente:
	1. Se ordenan las ciudades ascendentemente por kilómetro.
	2. Cada vez que se encuentra una ciudad no cubierta, se coloca un patrullero en la última bifurcación posible dentro de los 50 km siguientes. Esto maximiza la cobertura hacia adelante y minimiza la cantidad total de patrulleros.
	3. En cada paso la decisión local es la mejor y no limita la optimalidad global. Ninguna colocación más a la izquierda podría cubrir más ciudades, y moverlo más adelante dejaría ciudades sin cubrir.
'''