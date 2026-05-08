# Interpolación Cuadrática

## ¿Qué es?
A diferencia de la lineal, la interpolación cuadrática une tres puntos conocidos, `(x0, y0)`, `(x1, y1)` y `(x2, y2)`, utilizando un polinomio de segundo grado, es decir, una parábola.

Este método es más preciso cuando los datos conocidos siguen una curva (como la trayectoria de un proyectil o el crecimiento de una población), ya que captura la curvatura de los datos en lugar de asumir un cambio constante.

## Fórmula (Polinomio de Lagrange)
Una forma común de expresar el polinomio interpolador es mediante la fórmula de Lagrange para n=2:

P(x) = y_0 \cdot L_0(x) + y_1 \cdot L_1(x) + y_2 \cdot L_2(x)

Donde cada L_i(x) es un coeficiente especial que asegura que la parábola pase exactamente por los tres puntos dados.

---
