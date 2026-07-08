'''
Una red de satélites se construyó para permitir la comunicación entre una nave espacial y la tierra. Ciertos Satélites pueden intercambiar mensajes entre otros (ida y vuelta). Algunos con la tierra, otros con la nave espacial. Contamos con la red y se pide medir su robustez: ¿cuántos satélites (en el peor de los casos) se pueden romper que dejen incomunicada la nave con la tierra? ¿Cuáles? Utilizando redes de flujo, resolver el problema. Indicar y justificar la complejidad del algoritmo implementado. Recordar que esto último debe estar en las variables del problema.
'''

'''
Tengo que aplicar dos trucos:
    - Debemos impelementar el corte minimo, para esto debo duplicar cada vertice y crear una arista intermedia de flujo 1 que lo una con el original.
    - Al ser un grafo no direccionado debemos crear vertices intermedios para evitar aristas antiparalelas.
'''