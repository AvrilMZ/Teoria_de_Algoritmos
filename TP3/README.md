# Trabajo Práctico 3: Problemas NP-Completos para la defensa de la Tribu del Agua

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo 
de Backtracking para resolver un Problema NP-Completo, así como el análisis 
de posibles aproximaciones. 

## Introducción

Es el año 95 DG. 
La Nación del Fuego sigue su ataque, esta vez hacia la Tribu del Agua, luego de
una humillante derrota a manos del Reino de la Tierra, gracias a nuestra ayuda. 
La tribu debe defenderse del ataque. 

El maestro Pakku ha recomendado hacer lo siguiente: 
Separar a todos los Maestros Agua en $k$ grupos ($S_1, S_2, \cdots, S_k$). 
Primero atacará el primer grupo. A medida que el primer grupo se vaya cansando 
entrará el segundo grupo. Luego entrará el tercero, y de esta manera se busca 
generar un ataque constante, que sumado a la ventaja del agua por sobre el fuego, 
buscará lograr la victoria. 

En función de esto, lo más conveniente es que los grupos estén parejos para que,
justamente, ese ataque se mantenga constante. 

Conocemos la fuerza/maestría/habilidad de cada uno de los maestros agua, la cuál
podemos cuantificar diciendo que para el maestro $i$ ese valor es $x_i$, y 
tenemos todos los valores $x_1, x_2, \cdots, x_n$ (todos valores positivos). 

Para que los grupos estén parejos, lo que buscaremos es minimizar la adición
de los cuadrados de las sumas de las fuerzas de los grupos. Es decir:

$$\min \sum_{i = 1}^k \left( \sum_{x_j \in S_i} x_j\right)^2$$

El Maestro Pakku nos dice que esta es una tarea difícil, pero que _con tiempo y paciencia_
podemos obtener el resultado ideal.


## Consigna

Para los primeros dos puntos, considerar la versión de decisión del Problema de la Tribu del Agua:

Dado una secuencia de $n$ fuerzas/habilidades de maestros agua $x_1, x_2, \cdots, x_n$, y dos 
números $k$ y $B$, definir si existe una partición en $k$ subgrupos $S_1, S_2, \cdots, S_k$ 
tal que: 

$$\sum_{i = 1}^k \left( \sum_{x_j \in S_j} x_j\right)^2 \leq B$$

Cada elemento $x_i$ debe estar asignado a un grupo y sólo un grupo. 


1. 	Demostrar que el Problema de la Tribu del Agua se encuentra en NP.

2. 	Demostrar que el Problema de la Tribu del Agua es, en efecto, un problema NP-Completo. 
	Si se hace una reducción involucrando un problema no visto en clase, agregar una
	(al menos resumida) demostración que dicho problema es NP-Completo. 

3. 	Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema (valga la 
	redundancia) en la versión de optimización planteada originalmente. 
	Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos. 

4. 	Escribir un modelo de programación lineal que resuelva el problema. Dado la dificultad de
	la función objetivo para volverla lineal, planteamos dos alternativas. Ejecutar el modelo implementado 
	para los mismos sets de datos para corroborar su correctitud, o una cota
 	de aproximación empírica. Tomar mediciones de tiempo y compararlas con las del algoritmo que implementa 
 	Backtracking.  

	* Obtener la solución óptima al problema (más allá del planteo, demorará bastante en su ejecución).
	Considerar que esto implicará agregar bastantes variables de decisión. 
	* Que el objetivo sea minimizar la diferencia del grupo de mayor suma con el de menor suma. Es decir,
	si el grupo $Z$ es el del mayor suma de habilidades de los maestros ($\sum_i Z_i$) y Y es el de
	menor suma, entonces se busca minimizar $\sum_i Z_i - \sum_j Y_j$. 
	En este caso, la solución será una aproximación al resultado óptimo. 

5. 	El Maestro Pakku nos propone el siguiente algoritmo de aproximación:
 	Generar los $k$ grupos vacíos. Ordenar de mayor a menor los maestros en función de su habilidad
 	o fortaleza. Agregar al más habilidoso al grupo con menos habilidad hasta ahora (cuadrado de la 
 	suma). Repetir siguiendo con el siguiente más habilidoso, hasta que no queden más maestros por
 	asignar.
   
	Este algoritmo sirve como una aproximación para resolver el problema de la tribu del agua. 
	Implementar dicho algoritmo, analizar su complejidad
	y analizar cuán buena aproximación es. Para esto, considerar lo siguiente: 
	Sea $I$ una instancia cualquiera del problema, y $z(I)$ una
	solución óptima para dicha instancia, y sea $A(I)$ la solución aproximada, 
	se define $\frac{A(I)}{z(I)} \leq r(A)$ para todas las instancias posibles.
	Realizar mediciones utilizando el algoritmo exacto y la aproximación,
	con el objetivo de definir dicha relación. Realizar también mediciones
	que contemplen volúmenes de datos ya inmanejables para el algoritmo exacto,
	a fin de corroborar empíricamente la cota calculada anteriormente (implementando
	para sets de datos cuya solución se sepa de antemano).
   	Para este punto no es requisito la demostracion formal de la cota.  

7.	**Opcional**: Implementar alguna otra aproximación (o algoritmo greedy) que 
	les parezca de interés. Comparar sus resultados con los dados por la aproximación 
	del punto anterior. Indicar y justificar su complejidad. No es obligatorio
	hacer este punto para aprobar el trabajo práctico (pero si resta puntos no hacerlo).

8. 	Agregar cualquier conclusión que parezca relevante.
