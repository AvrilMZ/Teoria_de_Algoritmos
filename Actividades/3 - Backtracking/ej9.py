'''
Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, cada materia está representada con una lista de cursos/horarios posibles a cursar (solo debe elegirse un horario por cada curso). Cada materia puede tener varios cursos. 

Implementar un algoritmo de backtracking que devuelva un listado con todas las combinaciones posibles que permitan asistir a un curso de cada materia sin que se solapen los horarios. 

Considerar que existe una función `son_compatibles(curso_1, curso_2)` que dados dos cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo.
'''

from compatibles import *

def comb_backtracking(materias, i, visitados, combinaciones):
	if i == len(materias):
		combinaciones.append(visitados.copy())
		return

	for curso in materias[i]:
		if all(son_compatibles(curso, c) for c in visitados):
			visitados.append(curso)
			comb_backtracking(materias, i + 1, visitados, combinaciones)
			visitados.pop()

def obtener_combinaciones(materias):
	combinaciones = []
	visitados = []
	comb_backtracking(materias, 0, visitados, combinaciones)
	return combinaciones