# Interpolación Cuadrática

## ¿Qué es?
La interpolación cuadrática es un método numérico que estima un valor desconocido utilizando un polinomio de segundo grado (una parábola). A diferencia de la interpolación lineal que solo necesita dos puntos, este método requiere **tres puntos de datos conocidos** $(x_0, y_0)$, $(x_1, y_1)$ y $(x_2, y_2)$. Al capturar la curvatura de los datos, proporciona estimaciones mucho más precisas para funciones no lineales que el método lineal.

## Fórmula
Existen varias formas de expresar este polinomio (como el método de Newton), pero la más directa para programar es la **Fórmula de Lagrange para polinomios de segundo grado**:

$$y = y_0 \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)} + y_1 \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} + y_2 \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}$$

Donde:
* $(x_0, y_0), (x_1, y_1), (x_2, y_2)$ son nuestros tres puntos conocidos.
* $x$ es el valor objetivo del cual queremos estimar su pareja $y$.

## Algoritmo
1. Definir las coordenadas de los tres puntos conocidos $(x_0, y_0)$, $(x_1, y_1)$ y $(x_2, y_2)$.
2. Establecer el valor de $x$ que deseamos interpolar.
3. Calcular el primer término de la ecuación matemática (correspondiente a $y_0$).
4. Calcular el segundo término de la ecuación (correspondiente a $y_1$).
5. Calcular el tercer término de la ecuación (correspondiente a $y_2$).
6. Sumar los tres términos para obtener el valor estimado de $y$.
7. Imprimir el resultado en la consola.

## Datos
Entrada: 
Punto 0: (1.0, 1.0)
Punto 1: (2.0, 4.0)
Punto 2: (3.0, 9.0)
Valor a buscar: x = 2.5

Salida:
--- Interpolación Cuadrática ---
Puntos: (1.0, 1.0), (2.0, 4.0), (3.0, 9.0)
Para x = 2.5, el valor estimado de y es: 6.25
