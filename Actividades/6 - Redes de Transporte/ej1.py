'''
Explicar para cada uno de los siguientes casos, qué modificaciones se deben aplicar sobre una red para convertirla en una red de flujo apta para la utilización del algoritmo de Ford-Fulkerson.
	a. En la red existen bucles.
	b. En la red hay ciclos de dos vértices (aristas antiparalelas).
	c. En la red hay más de una fuente.
	d. En la red hay más de un sumidero.
'''

'''
a. Se eliminan ya que esto no afectaria el flujo de la red.
b. Se agrega un vertice que interrumpa alguna de las dos arristas y cuyo caudal de entrada sea el mismo que el de salida, asi no se afecta la red previa.
c. Se agrega un vertice nuevo que se lo va a considerar fuente y conecta todas las fuentes previamente considerados fuente con aristas de capacidad infinita (cierra la red).
d. Similar al problema de la fuente, se agrega un nuevo vertice que se lo va a considerar sumidero uniendo todos los vertices previamente considerados sumidero con aristas de capacidad infinita (cierra la red).
'''