# Interpolación Segmentada (Lineal a Trozos)

## ¿Qué es?
La interpolación segmentada resuelve el problema de tener múltiples puntos de datos. En lugar de usar todos los puntos a la vez para crear una ecuación gigantesca, este método divide los datos en "segmentos" o intervalos.
Cuando buscamos un valor desconocido, el algoritmo primero averigua en qué segmento cae nuestro punto y, una vez localizado, aplica una interpolación lineal simple única y exclusivamente usando los dos puntos que forman ese segmento.

## Fórmula
Dada una tabla de datos con puntos (x_0, y_0), (x_1, y_1),  (x_n, y_n) ordenados de menor a mayor respecto a x, primero encontramos el intervalo [x_i, x_{i+1}] que contiene a nuestro valor objetivo x. Luego aplicamos la fórmula:

y = y_i + (x - x_i) {y_{i+1} - y_i}{x_{i+1} - x_i}

Donde:
* x_i y y_i son las coordenadas del inicio del segmento.
* x_{i+1} y y_{i+1} son las coordenadas del final del segmento.
* x es el valor que queremos interpolar.

## Algoritmo
1. Definir dos arreglos (listas): uno para las coordenadas x y otro para las y, asegurando que las x estén ordenadas de menor a mayor.
2. Establecer el valor objetivo $x$ que queremos buscar.
3. Recorrer los puntos usando un bucle (`for`) para identificar en qué segmento [x_i, x_{i+1}] se encuentra nuestro valor x.
4. Extraer las coordenadas exactas de ese par de puntos.
5. Aplicar la fórmula de interpolación lineal sobre esos dos puntos.
6. Imprimir el valor estimado en consola.


## Datos

Entrada: 
Puntos X: [0.0, 2.0, 4.0, 6.0]
Puntos Y: [1.0, 5.0, 3.0, 9.0]
Valor a buscar: x = 3.0

Salida:
--- Interpolación Segmentada ---
Para x = 3.0, el valor estimado de y es: 4.0
