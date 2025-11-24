'''
Debido a la trágica situación actual, es necesario realizar tests para detectar si alguna persona está contagiada de COVID-19. El problema es que los insumos tienden a ser bastante caros, y no vivimos en un país al que los recursos le sobren.

Supongamos que por persona se toma más de una muestra (lo cual es cierto, pero a fines del ejercicio supongamos que son muchas muestras), y que podemos realizar un testeo a más de una persona al mismo tiempo mezclando las muestras (lo cual también es cierto): determinamos un conjunto de personas a testear, obtenemos una muestra de cada una de ellas, las “juntamos”, y al conjunto le realizamos el test. Si el test resulta negativo, implica que todas las personas testeadas en conjunto resultaron negativas. Si resulta positivo, implica que al menos una de las personas testedas resulta positiva.

Suponer que existe una función `pcr(grupo)`, que devuelve true si al menos una persona del `grupo` es COVID-positivo, y `false` en caso contrario (los `grupos` pueden estar formados por 1 o más personas). Suponer que la positividad es extremadamente baja, e inclusive pueden suponer que va a haber una única persona contagiada (por simplicidad).

Implementar un algoritmo que dado un conjunto de `n` personas, devuelva la o las personas contagiadas, utilizando la menor cantidad de tests posibles (considerando la notación Big Oh). En dicha notación, ¿cuántos tests se estarán utilizando?

Pueden considerar que habrá una única persona contagiada, pero esto no cambiará el análisis a realizar.
'''