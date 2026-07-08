'''
Implementar un modelo de programación lineal que resuelva el problema de Independent Set Máximo.
'''

'''
W_i: "Constante continua, peso del vertice i"
X_i: "Variable binaria, vertice i agregado"

\max(\sum_{i = 0}^{n} W_i * X_i) -> Contabilizo el peso solo de los vertices incluidos en la solucion

Donde:
    - X_i + \sum_{a pertenece a los adyacentes de i} X_a <= 1 + M(1 - X_i) -> para que se cumpla la inecuacion del caso de que el vertice i no este pero sus adyacentes si.
'''