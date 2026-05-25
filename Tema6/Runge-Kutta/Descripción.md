# Método de Runge-Kutta (4to Orden)

## Descripción
El método de Runge-Kutta de cuarto orden (RK4) es uno de los algoritmos numéricos más utilizados y precisos para resolver Ecuaciones Diferenciales Ordinarias (EDO) con condiciones iniciales. A diferencia del método de Euler (que solo evalúa la pendiente al inicio del intervalo), RK4 calcula cuatro pendientes diferentes dentro de cada paso ($k_1$, $k_2$, $k_3$, $k_4$) y hace un promedio ponderado de ellas. Esto permite dar pasos mucho más grandes con un margen de error drásticamente menor.

---

## Ecuación / Fórmula
Para avanzar de un punto $(x_i, y_i)$ al siguiente $(x_{i+1}, y_{i+1})$, la fórmula principal del método es:

$$y_{i+1} = y_i + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)$$
$$x_{i+1} = x_i + h$$

Donde las cuatro pendientes ($k$) se calculan secuencialmente de la siguiente manera:
- $k_1 = f(x_i, y_i)$
- $k_2 = f\left(x_i + \frac{h}{2}, y_i + \frac{h}{2} k_1\right)$
- $k_3 = f\left(x_i + \frac{h}{2}, y_i + \frac{h}{2} k_2\right)$
- $k_4 = f(x_i + h, y_i + h k_3)$

---

## Algoritmo
1. **Inicio.**
2. Definir la ecuación diferencial $dy/dx = f(x, y)$.
3. Proporcionar las condiciones iniciales: el valor de $x_0$ y $y_0$.
4. Definir el tamaño del paso $h$ y el valor final de $x$ objetivo.
5. Calcular el número total de pasos necesarios.
6. Iniciar un ciclo desde $i = 0$ hasta finalizar los pasos:
   - Calcular $k_1$ evaluando la función en el punto actual.
   - Calcular $k_2$ evaluando la función en el punto medio (usando $k_1$).
   - Calcular $k_3$ evaluando la función en el punto medio (usando $k_2$).
   - Calcular $k_4$ evaluando la función en el punto final del intervalo (usando $k_3$).
   - Calcular el nuevo valor de $y_{i+1}$ aplicando la fórmula del promedio ponderado.
   - Avanzar el valor de $x$: $x_{i+1} = x_i + h$.
7. Mostrar el valor final estimado de $y$.
8. **Fin.**

---

## Código Fuente
* [Runge-Kutta en python](./runge_kutta.py)

---

## Compilación con datos de entrada y de salida

### Ejemplo 1: Ecuación Lineal Simple
Resolver $dy/dx = x + y$
* **Datos de entrada:**
    * Ecuación $f(x, y)$: `x + y`
    * $x$ inicial ($x_0$): `0`
    * $y$ inicial ($y_0$): `1`
    * Tamaño del paso ($h$): `0.1`
    * $x$ final a evaluar: `0.2`
* **Datos de salida:**
    * Iteración 1: $x = 0.100$, $y = 1.110342$
    * Iteración 2: $x = 0.200$, $y = 1.242805$
    * Resultado final estimado en $x = 0.2$: `1.242805`

### Ejemplo 2: Ecuación No Lineal
Resolver $dy/dx = x^2 - y$
* **Datos de entrada:**
    * Ecuación $f(x, y)$: `x**2 - y`
    * $x$ inicial ($x_0$): `0`
    * $y$ inicial ($y_0$): `1`
    * Tamaño del paso ($h$): `0.5`
    * $x$ final a evaluar: `1.0`
* **Datos de salida:**
    * Iteración 1: $x = 0.500$, $y = 0.627604$
    * Iteración 2: $x = 1.000$, $y = 0.534293$
    * Resultado final estimado en $x = 1.0$: `0.534293`

---

## Otro: Problemario
Para comparar la gran diferencia de precisión entre este método y el método de Euler para los mismos intervalos de paso $h$, puedes consultar el documento:
* [Ver Problemario de Ecuaciones Diferenciales](./problemario.pdf)

---

🔙 [Volver al Índice Principal](../../README.md)

