'''
Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto, es la de maximizar la ganancia dada por p[k] - p[j]. 

Implementar un algoritmo de programación dinámica que permita resolver el problema de Osvaldo. Indicar y justificar la complejidad del algoritmo implementado.
'''

def compra_venta(p):
	return 0, len(p) - 1