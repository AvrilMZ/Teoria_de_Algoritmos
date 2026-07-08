'''
Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).
'''

'''
W: "Constante, peso máximo de la mochila".
P: "Constante, peso del producto".
X: "Constante, valor del producto".
A: "Variable binaria, agrego o no agrego el producto"

$\max{\sum_{i = 1}^{n} X_i * A_i}$

Restricción:
	$\sum_{i = 1}^{n} P_i * A_i <= W$
'''