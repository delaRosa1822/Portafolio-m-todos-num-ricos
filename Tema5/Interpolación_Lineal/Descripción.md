# Interpolación Lineal

## ¿Qué es?
La interpolación lineal es un método numérico que nos permite estimar un valor desconocido que se encuentra *entre* dos valores conocidos. El método asume que la relación entre estos dos puntos es una línea recta perfecta. Básicamente, calculamos la pendiente (inclinación) de la línea que une a nuestros dos puntos conocidos y usamos esa misma pendiente para descubrir el valor de y para cualquier valor de x intermedio.

## Fórmula
Si conocemos dos puntos (x_0, y_0) y (x_1, y_1), y queremos estimar el valor de y para un punto intermedio x, la fórmula es:

y = y_0 + (x - x_0) {y_1 - y_0}{x_1 - x_0}

Donde:
* (x_0, y_0) es el primer punto conocido.
* (x_1, y_1) es el segundo punto conocido.
* x es el valor objetivo del cual queremos conocer su pareja y.
* La parte de la fracción {y_1 - y_0}{x_1 - x_0} es la pendiente de la recta.

## Algoritmo
1. Definir las coordenadas del primer punto conocido (x_0, y_0).
2. Definir las coordenadas del segundo punto conocido (x_1, y_1).
3. Establecer el valor objetivo x que queremos interpolar (debe estar entre x_0 y x_1).
4. Calcular la diferencia de las y dividida entre la diferencia de las x (esto es la pendiente).
5. Multiplicar la pendiente por la diferencia entre el x objetivo y x_0.
6. Sumarle y_0 al resultado anterior para obtener el valor estimado de y.
7. Imprimir el valor estimado en consola.

Entrada: 
Punto 0: (2.0, 4.0)
Punto 1: (6.0, 12.0)
Valor a buscar: x = 4.0

Salida:
--- Interpolación Lineal ---
Punto conocido 1: (2.0, 4.0)
Punto conocido 2: (6.0, 12.0)
Para x = 4.0, el valor estimado de y es: 8.0
