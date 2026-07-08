'''
Implementar un modelo de programación lineal que determine la cantidad mínima de colores a utilizar para poder pintar a un grafo de colores, de tal forma que ningún adyacente comparta color entre sí.
'''

'''
P_{pais, color}: "Variable binaria, al pais se le asigna ese color"
Y_{color}: "Variable binaria, se usa el color"

\min{\sum_{colores} Y_{color}} -> Buscamos minimizar la cantidad de colores a utilizar

Donde:
    - \sum_{para todos los colores} P_{pais, color} = 1 -> Todos los paises tienen que tener un solo color asignado.
    - P_{i, color} + \sum_{j pertenece a los adyacentes de i}^{n} P_{j, color} <= 1 + M(1 - P_{i, color}) -> Que los paises adyacentes no compartan el mismo color que el pais actual.
'''