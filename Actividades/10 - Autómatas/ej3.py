'''
Implementar un algoritmo que "acepte" el mismo lenguaje que el siguiente Autómata Finito Determinista.
Es decir, implementar una función es_parte_lenguaje que reciba una cadena y devuelva True si la cadena forma del lenguaje del siguiente autómata. La función debe ejecutar en tiempo constante. Se garantiza que la cadena solamente contiene como posibles símbolos a, b y c.

El mismo está definido en la página recomendada con el siguiente link directo: https://www.cs.odu.edu/~zeil/automat/automat.cgi?saved=1&lang=eyJzcGVjaWZpY2F0aW9uIjoiYXV0b21hdG9uRkEiLCJjcmVhdGVkQnkiOiJBbm9ueW1vdXMiLCJwcm9ibGVtSUQiOiIiLCJ1bmxvY2vGDHN0YXRlcyI6W3sibGFiZWwiOiJxMCIsImluaXRpYWwiOnRydWUsImZpbsQNZmFsc2UsIngiOjEzNiwieSI6MTQzfSzLPDHMPMcv0T0yNzTGPTM5zT0y2j3mAId4Ijo0MDfHeTDNPDPfecZ5OS40NzE4MDc2NDIwMTQ3NsZMMzc4LjU4NDU3NzA3Mzk1NTfNWjTfWsZaNDMuNjA5MTQ2MzE4ODI1NcVZMjkxLjE2ODc3MjE1Njg0MM5ZNdpZ6gDvMzPFSjM3Mi4yNjQ2MTg4OTDEAjV9XSwidHJhbnNp5AIM5gHDZnJvbegBwnRv6AGQyHFhIsR%2FyCTEGsYk5AF3yCRjzSTEGtIkYVxuYlxuzirKTuQA1sgqYtck5AFT9gCW6gC65AHRyUjQb8Qd3yfOJ9pyxBr%2FALrFGt9vziffb9FLzkjKJM9IXX0%3D
'''

def es_parte_lenguaje(cadena):
	if len(cadena) < 2:
		return False
	if cadena[0] == 'a' and cadena[1] == 'c':
		return True
	if cadena[-1] != 'b' or cadena[-2] != 'a':
		return False
	return True