'''
La Escuela Nacional 32 "Alan Turing" de Bragado tiene una forma particular de requerir que los alumnos formen fila. 
En vez del clásico "de menor a mayor altura", lo hacen primero con alumnos yendo con altura decreciente, hasta llegado un punto que 
empieza a ir de forma creciente, hasta terminar con todos los alumnos.

Por ejemplo las alturas podrían ser 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.

Implementar una función indice_mas_bajo que dado un arreglo/lista de alumnos(*) que represente dicha fila, devuelva el índice del 
alumno más bajo, en tiempo logarítmico. Se puede asumir que hay al menos 3 alumnos. En el ejemplo, el alumno más bajo es aquel con altura 0.98.

Implementar una función validar_mas_bajo que dado un arreglo/lista de alumnos(*) y un índice, valide (devuelva True o False) si dicho 
índice corresponde al del alumno más bajo de la fila. (Aclaración: esto debería poder realizarse en tiempo constante)

(*)
Los alumnos son de la forma:

alumno {
	nombre (string)
	altura (float)
}

Se puede acceder a la altura de un alumno haciendo varible_tipo_alumno.altura.

Importante: considerar que si la prueba de volumen no pasa, es probable que sea porque no están cumpliendo con la complejidad requerida.
'''

def dyc_indice_mas_bajo(inicio, fin, alumnos):
    if inicio == fin:
        return inicio

    medio = (inicio + fin) // 2
    if validar_mas_bajo(alumnos, medio):
        return medio
    if alumnos[medio + 1].altura < alumnos[medio].altura:
        return dyc_indice_mas_bajo(medio + 1, fin, alumnos)
    else:
        return dyc_indice_mas_bajo(inicio, medio, alumnos)

def indice_mas_bajo(alumnos):
    return dyc_indice_mas_bajo(0, len(alumnos) - 1, alumnos)

def validar_mas_bajo(alumnos, indice):
    if indice == 0:
        return alumnos[indice + 1].altura > alumnos[indice].altura
    if indice == len(alumnos) - 1:
        return alumnos[indice - 1].altura > alumnos[indice].altura
    if alumnos[indice - 1].altura > alumnos[indice].altura and alumnos[indice + 1].altura > alumnos[indice].altura:
        return True
    return False