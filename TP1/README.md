# Trabajo Práctico 1: Algoritmos Greedy en la Nación del Fuego

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo Greedy. 

## Introducción

Es el año 10 AG, y somos asesores del Señor del Fuego (líder supremo de la Nación del Fuego).
El Señor del Fuego cuenta con un ejército de Maestros Fuego, muy temidos en el mundo. Tiene 
varias batallas con las cuales lidiar: una contra el Templo Aire del Este, otra en la Tribu 
del Agua del Norte, otra en la Isla de Kyoshi, una muy importante en Ba Sing Se (capital del 
Reino de la Tierra), y muchas otras más. Sabemos cuánto tiempo necesita el ejército para ganar 
cada una de las batallas ($t_i$). El ejército ataca todo junto, no puede ni conviene que se
separen en grupos. Es decir, no participan de más de una batalla en simultáneo.

La felicidad que produce saber que se logró una victoria depende del momento en el que ésta
se obtenga (es decir, que la batalla termine). Es por esto que podemos definir a $F_i$ 
como el momento en el que se termina la batalla $i$. Si la primera batalla es la $j$, 
entonces $F_j = t_j$, en cambio si la batalla $j$ se realiza justo después de la batalla 
$i$, entonces $$F_j = F_i + t_j$$. 

Además del tiempo que consume cada batalla, sabemos que al Señor del Fuego no le da lo mismo
el orden en el que se realizan, porque comunicar la victoria a su nación en diferentes batallas
genera menos impacto si pasa mucho tiempo. Además, cada batalla tiene una importancia diferente. 
Vamos a definir que tenemos un peso $b_i$ que nos define cuán importante es una batalla. 

Dadas estas características, se quiere buscar tener el orden de las batallas tales que 
se logre **minimizar** la suma ponderada de los tiempos de finalización: $$\sum_{i=1}^n b_i F_i$$.

El Señor del Fuego nos pide diseñar un algoritmo que determine aquel orden de las batallas que 
logre minimizar dicha suma ponderada. 


## Consigna

1. Hacer un análisis del problema, y proponer un algoritmo greedy que obtenga **la solución óptima** al 
problema planteado:
Dados los $n$ valores de todos los $t_i$ y $b_i$, determinar cuál es el orden óptimo para realizar 
las batallas en el cuál se minimiza $$\sum_{i=1}^n b_i F_i$$.
2. Demostrar que el algoritmo planteado obtiene siempre la solución óptima. 
3. Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. Analizar si 
(y cómo) afecta la variabilidad de los valores de $t_i$ y $b_i$ a los tiempos del algoritmo planteado. 
4. Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente, el
curso proveerá con algunos casos particulares para que puedan usar de prueba.
5. Hacer mediciones de tiempos para corroborar la complejidad teórica indicada. Esto, por supuesto, implica que deben generar sus _sets_ de datos.
Agregar los casos de prueba necesarios para dicha corroboración. Esta corroboración empírica debe realizarse confeccionando gráficos correspondientes, y utilizando la técnica de cuadrados mínimos. Para esto, [proveemos una explicación detallada](https://github.com/algoritmos-rw/tda_ejemplos/blob/main/analisis_complejidad/cuadrados_minimos.ipynb), en conjunto de ejemplos. Recomendamos tomar más de una medición de la misma muestra y quedarse con el promedio para reducir el ruido en la medición.
6. Agregar cualquier conclusión que les parezca relevante.
