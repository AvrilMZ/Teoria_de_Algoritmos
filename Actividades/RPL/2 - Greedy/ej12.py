'''
Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad República. 
Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales no es otro sino Arnook. 
En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos por el control de diferentes kilómetros de la ruta costera. 
Cada pequeña mafia le pide a Arnook control sobre un rango de kilómetros 
(por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ). 
Si hay una mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden solaparse). 
Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”, indistintamente de los kilómetros pedidos. 
Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie, así lo único que es de interés es maximizar la cantidad de permisos otorgados 
(asegurándose de no otorgarle algún lugar a dos mafias diferentes). 

Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine a cuáles se les otorgará control, de forma que no hayan 
dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados. Indicar y justificar la complejidad del algoritmo implementado. 
Justificar por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
'''

def hay_interseccion(fin_anterior, inicio_nueva):
	return fin_anterior > inicio_nueva

# Pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
	pedidos_ordenados = sorted(pedidos, key=lambda x: x[1])
	control = []
	km_fin_anterior = None
	for inicio, fin in pedidos_ordenados:
		if len(control) == 0 or not hay_interseccion(km_fin_anterior, inicio):
			control.append((inicio, fin))
			km_fin_anterior = fin
	return control

'''
Ordenar el arreglo por km de finalizacion tiene un costo de O(n*log(n)).
Recorrer cada pedido del arreglo ordenado realizando acciones constantes resulta en O(n).
Finalmente concluimos en una complejidad de O(n*log(n)).

El algoritmo es Greedy dado que al ordenar el arraglo por km de finalizacion siempre se busca siempre el rango mas proximo al fin del pedido anterior
para maximizar la cantidad de pedidos otorgados. El algoritmo es optimo, ya que en caso de existir un k+1 cuya finalizacion sea luego de la de k invertir los
pedidos resulta en el mismo resultado o peor ya que le puede quitar la posibilidad de otorgar otro pedido.
'''