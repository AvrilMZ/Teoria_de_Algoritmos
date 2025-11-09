'''
Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto, es el de maximizar la ganancia dada por p[k] - p[j].

Implementar un modelo de programación lineal que determine el día de compra y el día de venta del inmueble. Indicar la cantidad de restricciones implementadas para esto.
'''

'''
P_i: "Variable continua, precio del dia i"
X_i: "Variable binaria, compro en el dia i"
Y_i: "Varaible binaria, vendo en el dia i"

\max{\sum_{j}^{n}(P_j * Y_j) - \sum_{i}^{j}(P_i * X_i)} -> maximizar la ganancia de la venta del inmueble

Donde:
    - \sum_{i = 0}^{n} X_i = 1 -> Solo se puede comprar un dia
    - \sum_{i = 0}^{n} Y_i = 1 -> Solo se puede vender un dia
    - \sum_{j}(j * Y_j) > \sum_{i}(i * X_i) -> El dia de venta debe ser posterior al dia de compra (hacemos esto ya que j > i no se puede plantear debido a que j e i no son variables)
'''