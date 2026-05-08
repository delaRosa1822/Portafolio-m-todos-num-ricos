# Interpolación Lineal

## ¿Qué es?
Es el método más simple de interpolación. Consiste en unir dos puntos conocidos, `(x0, y0)` y `(x1, y1)`, mediante una línea recta. Se utiliza para estimar un valor `y` correspondiente a un valor `x` que se encuentra entre los dos puntos dados.

Es ideal cuando los puntos están muy cerca entre sí o cuando el fenómeno que se está modelando cambia de forma casi constante.

## Fórmula
La fórmula para encontrar el valor estimado de `y` en un punto `x` intermedio es:

y = y_0 + \frac{y_1 - y_0}{x_1 - x_0} (x - x_0)

---
