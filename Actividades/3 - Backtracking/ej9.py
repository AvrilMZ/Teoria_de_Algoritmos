'''
Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, cada materia está representada con una lista de cursos/horarios posibles a cursar (solo debe elegirse un horario por cada curso). Cada materia puede tener varios cursos. 

Implementar un algoritmo de backtracking que devuelva un listado con todas las combinaciones posibles que permitan asistir a un curso de cada materia sin que se solapen los horarios. 

Considerar que existe una función `son_compatibles(curso_1, curso_2)` que dados dos cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo.
'''

from compatibles import *

def compatible_con_todos(curso, visitados):
	for c in visitados:
		if not son_compatibles(curso, c):
			return False
	return True

def comb_backtracking(materias, indice, visitados):
	if indice == len(materias):
		return [visitados[:]]

	combinaciones = []
	for curso in materias[indice]:
		if compatible_con_todos(curso, visitados):
			visitados.append(curso)
			sol = comb_backtracking(materias, indice + 1, visitados)
			combinaciones.extend(sol)
			visitados.pop()
	
	return combinaciones

def obtener_combinaciones(materias):
	return comb_backtracking(materias, 0, [])