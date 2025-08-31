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

def bifurcaciones_con_patrulla(ciudades):
	ciudades_ordenadas = sorted(ciudades, key=lambda ciudad: ciudad[1])
	policiales = []
	ultimo_puesto = None
	for ciudad, bifurcacion in ciudades_ordenadas:
		if not ultimo_puesto or bifurcacion - ultimo_puesto > 50:
			policiales.append((ciudad, bifurcacion))
			ultimo_puesto = bifurcacion
	return policiales

'''

'''