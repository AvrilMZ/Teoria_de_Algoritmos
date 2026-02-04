# TP1: Algoritmos Greedy en la Nación del Fuego

### FIUBA Teoría de Algoritmos (TB024) Curso Buchwald - Genender 

#### Integrantes:
- Martin Ariel Kupa (112560)
- Facundo Camilo Stifman (112541)
- Juan Ignacio Moore (112479)
- Avril Victoria Morfeo Zerbi (112563)

## Compilación

Para compilar es necesario instalar una distribución de `Tex`, por ejemplo `texlive`. En la mayoria de sistemas linux es posible instalarlo junto con todas las dependencias mediante el package manager:
```sh
apt install texlive-full # Reemplazar apt por el package manager de su distribución
```
Si el paquete no esta listado en su package manager refiérase a la [documentación oficial](https://www.tug.org/texlive/doc.html) de `texlive` para realizar una instalación manual.

El informe se compila mediante el comando:
```sh
latexmk main.tex
```

También se provee un makefile para facilitar el desarrollo:
```sh
make # Compila el informe
make clean # Elimina archivos compilados y comprimidos
make test # Compara los algoritmos con los resultados de la catedra
```

Originalmente desarrollado en `TeX 3.141592653 (TeX Live 2023/Debian)`

## Uso

Para ejecutar el algoritmo hacer:
```sh
./tp1 <ruta_datos> [<criterio>] # Ejecuta el algoritmo especificado por `criterio` sobre `ruta_datos`.
```

Ejemplo:
```sh
./tp1 datos/sets/catedra/10.txt # Ejecuta el algoritmo por coeficientes
./tp1 datos/sets/catedra/10.txt duracion # Ejecuta el algoritmo por duración
```

Para generar sets de datos:
```sh
./tp1 generar <cantidad_datos> <ruta_salida> <tipo_generador> # Genera `cantidad_datos` con el `tipo_generador` en `ruta_salida`
```

Ejemplo:
```sh
./tp1 generar 100 datos/sets/salida.txt generico # Genera 100 batallas balanceadas
./tp1 generar 10000 datos/sets/salida.txt b_mayor_t # Genera 10000 batallas con mayor importancia
```

Para generar los graficos:
```sh
./tp1 graficar [<ruta_salida>] # Genera los graficos del ajusta en `ruta_salida` o por defecto en datos/graficos
```
