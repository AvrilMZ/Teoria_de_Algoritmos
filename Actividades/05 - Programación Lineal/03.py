"""
Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).
"""

"""
V_i: Variable binaria, si el vertice i se encuentra en la solucion.

\min{\sum_{i = 0}^{n} V_i}

Restrincciones:
- V_i + V_j >= 1, para todo V_i conectado mediante una arista a V_j
"""
