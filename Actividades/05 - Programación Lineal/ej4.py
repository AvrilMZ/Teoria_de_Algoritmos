'''
Implementar un modelo de programación lineal que resuelva el problema de Dominating Set mínimo (ejercicio 14 de BT).
'''

'''
X: "Constante, vertice"
V: "Variable binaria, agrego el vertice o no"

\min{\sum_{i = 0}^{n} X_i * V_i}

donde V_i + \sum_{j pertenece a los vecinos de i} V_j >= 1 -> siendo j vecino de i.

Se debe plantear la sumatoria ya que si el chequeo es individual por cada vecino (V_i + V_j) puede pasar que un vecino de i este en el subconjunto y luego un vecino del vecino tambien, descartando la necesidad de que alguno, i o ese vecino, este en el set final.
'''