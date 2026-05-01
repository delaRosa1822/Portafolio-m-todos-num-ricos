# Método de Simpson 1/3 (Fórmula Simple)

## ¿Qué es?
Es un método de integración numérica utilizado para aproximar el valor de una integral definida (el área bajo una curva). A diferencia de la regla del trapecio, que une los puntos con líneas rectas, la regla de Simpson 1/3 los une utilizando polinomios de segundo grado (parábolas). La versión "simple" se aplica sobre un solo intervalo $[a, b]$, evaluando la función en los extremos y en el punto medio exacto.

## Fórmula
Para una función matemática f(x) evaluada en el intervalo [a, b], la fórmula simple de Simpson 1/3 se define como:

\int_{a}^{b} f(x) dx \approx \frac{h}{3} [f(a) + 4f(m) + f(b)]

Donde:
* a es el límite inferior.
* b es el límite superior.
* m = \frac{a + b}{2}$ es el punto medio.
* h = \frac{b - a}{2}$ es la distancia (o tamaño de paso) entre los puntos.

## Algoritmo
1. Definir la función matemática $f(x)$ que se desea integrar.
2. Establecer los límites de integración $a$ (inferior) y $b$ (superior).
3. Calcular el punto medio $m$ sumando los límites y dividiéndolos entre 2.
4. Calcular el tamaño del paso $h$.
5. Evaluar la función en los puntos $f(a)$, $f(m)$ y $f(b)$.
6. Aplicar la fórmula multiplicando por los pesos correspondientes (1, 4, 1) y multiplicando el total por $h/3$.
7. Imprimir el resultado de la aproximación.

Entrada: 
Función: f(x) = x^2
Límite a = 0.0
Límite b = 2.0

Salida:
--- Método de Simpson 1/3 (Simple) ---
Límite inferior (a): 0.0
Límite superior (b): 2.0
Aproximación del área: 2.6666666666666665
