"""
Implementar un algoritmo randomizado que permita estimar el valor de π (pi).
Para esto, recomendamos recordar que el área de un cuadrado de lado 2 es 4, mientras que el área de un círculo de diámetro 2 es, casualmente, π.

El algoritmo recibirá la cantidad de iteraciones a utilizar para aproximar, y se espera que a más iteraciones, se aproxime mejor.

Si el algoritmo no se trata de un algoritmo aleatorizado (de verdad), se penalizará fuertemente.
"""

"""
La idea seria crear un cadrado con un circulo interno e ir creando puntos aleatorios verificando si caen dentro de la circunferencia (estilo método Monte Carlo ya que generamos los puntos al azar).
Podemos plantear entonces:
        - La cantidad de puntos dentro del circulo sobre la cantidad de puntos totales se va a aproximar a el área del circulo sobre el área del cuadrado que es π/4.
        - Si despejo la formula obtengo que π = 4 * (puntos dentro del circulo / puntos totales)
"""

import random

RADIO = 1


def estimar_pi(iteraciones):
    cant_dentro_circulo = 0

    # Creo la cantidad de puntos solicitados por parametro y verfico si caen dentro del circulo
    for _ in range(iteraciones):
        x = random.uniform(-RADIO, RADIO)
        y = random.uniform(-RADIO, RADIO)

        if x**2 + y**2 <= RADIO**2:
            cant_dentro_circulo += 1

    return 4 * (cant_dentro_circulo / iteraciones)
