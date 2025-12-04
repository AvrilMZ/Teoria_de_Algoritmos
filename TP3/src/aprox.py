def grupos_maestros_aprox(lista_maestros, cant_grupos) -> tuple[list, int]:
    ordenados = sorted(lista_maestros, key=lambda x: x[1], reverse=True)
    grupos = [[] for _ in range(cant_grupos)]
    sumas = [0 for _ in range(cant_grupos)]

    for nom, fuerza in ordenados:
        indice = min(range(cant_grupos), key=lambda i: (sumas[i] + fuerza)**2 - sumas[i]**2)
        grupos[indice].append(nom)
        sumas[indice] += fuerza

    return grupos, sum(s**2 for s in sumas)