"""
El 2-Partition Problem como problema de optimización se describe tal que: Dado un conjunto de n números positivos T={T1,T2,…,Tn}, se particionan los números en dos subconjuntos S1 y S2 (con intersección vacía y unión = T) de forma de minimizar la sumatoria de cualquiera de los subconjuntos (min max(S1,S2)).

Implementar un modelo de programación lineal que dados los valores de los Ti nos permita obtener la asignación óptima para S1 y S2. Indicar la cantidad de inecuaciones definidas en el modelo.
"""

"""
T_i: Constante numero i del conjunto
X_i: Variable binaria, la constante en la posicion i pertenece a S1.

min{max{\sum{T_i*X_i}, \sum{T_i*(1 - X_i)}}}

(Poniendo 1 - X_i me ahorro la variable Y_i, por lo tanto tengo n resricciones menos (ya que no necesito X_i + Y_i = 1))

Restricciones:
Definimos Z = max{\sum{T_i*X_i}, \sum{T_i*(1 - X_i)}}, osea max(S1,S2).
- Z >= \sum{T_i*X_i}
- Z >= \sum{T_i*(1 - X_i)}

Cantidad total de inecuaciones: 2n
"""
