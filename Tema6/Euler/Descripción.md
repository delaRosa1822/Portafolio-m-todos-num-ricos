# Método de Euler para Ecuaciones Diferenciales

## Descripción
El método de Euler es el procedimiento numérico más básico para resolver Ecuaciones Diferenciales Ordinarias (EDO) de primer orden con un valor inicial dado. Funciona trazando rectas tangentes paso a paso; partiendo de un punto inicial conocido, utiliza la derivada (la pendiente) en ese punto para estimar el valor de la función un pequeño paso más adelante, y repite el proceso hasta llegar al punto deseado.

---

## Ecuación / Fórmula
La fórmula iterativa para calcular el siguiente punto es:

$$y_{i+1} = y_i + h \cdot f(x_i, y_i)$$
$$x_{i+1} = x_i + h$$

Donde:
- $y_{i+1}$ es el nuevo valor estimado de la función.
- $y_i$ es el valor actual de la función.
- $h$ es el tamaño del paso (incremento en $x$).
- $f(x_i, y_i)$ es la ecuación diferencial evaluada en el punto actual (representa la pendiente $dy/dx$).

---

## Algoritmo
1. **Inicio.**
2. Definir la ecuación diferencial de la forma $dy/dx = f(x, y)$.
3. Proporcionar las condiciones iniciales: el valor de $x_0$ y su correspondiente $y_0$.
4. Definir el tamaño del paso $h$ y el valor final de $x$ al que se desea llegar ($x_{final}$).
5. Calcular el número total de pasos necesarios: $n = (x_{final} - x_0) / h$.
6. Iniciar un ciclo desde $i = 0$ hasta $n-1$:
   - Calcular la pendiente actual evaluando la función: $m = f(x_i, y_i)$.
   - Calcular el nuevo valor de $y$: $y_{i+1} = y_i + h \cdot m$.
   - Calcular el nuevo valor de $x$: $x_{i+1} = x_i + h$.
7. Mostrar los valores de $x$ e $y$ en cada iteración.
8. **Fin.**

---

## Código Fuente
El script se encuentra en el archivo `euler.py`. Emplea la librería **SymPy** de Python para que puedas introducir cualquier ecuación diferencial con dos variables ($x$, $y$) directamente desde la consola, sin necesidad de reprogramar la función internamente.

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
    * Iteración 1: $x = 0.100$, $y = 1.100$
    * Iteración 2: $x = 0.200$, $y = 1.220$
    * Resultado final estimado en $x = 0.2$: `1.220000`

### Ejemplo 2: Ecuación No Lineal
Resolver $dy/dx = x^2 - y$
* **Datos de entrada:**
    * Ecuación $f(x, y)$: `x**2 - y`
    * $x$ inicial ($x_0$): `0`
    * $y$ inicial ($y_0$): `1`
    * Tamaño del paso ($h$): `0.5`
    * $x$ final a evaluar: `1.0`
* **Datos de salida:**
    * Iteración 1: $x = 0.500$, $y = 0.500$
    * Iteración 2: $x = 1.000$, $y = 0.375$
    * Resultado final estimado en $x = 1.0$: `0.375000`

---

## Otro: Problemario
Para visualizar gráficamente cómo el tamaño del paso $h$ afecta el error de truncamiento de este método, revisa el documento de apoyo:
* [Ver Problemario de Ecuaciones Diferenciales](./problemario.pdf)

---

## Notas sobre el Algoritmo y la Codificación
A diferencia de los algoritmos de raíces vistos anteriormente donde la función dependía de una sola variable ($x$), en este código la función se parsea para que dependa de dos símbolos simultáneos (`x` e `y`). Esto se logra usando `sp.lambdify((x, y), f)` en SymPy, lo que permite evaluar la pendiente de forma dinámica en cada punto del plano cartesiano durante el ciclo iterativo.
