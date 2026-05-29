# Método de Series de Taylor para Ecuaciones Diferenciales

## Descripción
El método de las Series de Taylor resuelve Ecuaciones Diferenciales Ordinarias (EDO) expandiendo la solución en un polinomio de Taylor alrededor de un punto conocido. A diferencia de Euler (que es equivalente a un Taylor de primer orden), este método permite incorporar derivadas de orden superior (segunda, tercera, cuarta derivada, etc.) para capturar mejor la curvatura de la función real, lo que permite utilizar pasos ($h$) más grandes manteniendo una alta precisión.

---

## Ecuación / Fórmula
La fórmula iterativa basada en el desarrollo de Taylor de orden $k$ es:

$$y_{i+1} = y_i + h y'_i + \frac{h^2}{2!} y''_i + \frac{h^3}{3!} y'''_i + \dots + \frac{h^k}{k!} y^{(k)}_i$$
$$x_{i+1} = x_i + h$$

Recordando que, dado que $y' = f(x, y)$, las derivadas superiores se obtienen aplicando derivación implícita (regla de la cadena). Por ejemplo, la segunda derivada es:
$$y'' = \frac{d}{dx} f(x,y) = \frac{\partial f}{\partial x} + \frac{\partial f}{\partial y} y' = f_x + f_y f$$

---

## Algoritmo
1. **Inicio.**
2. Definir la ecuación diferencial $dy/dx = f(x, y)$.
3. Proporcionar las condiciones iniciales: $x_0$ e $y_0$.
4. Definir el tamaño del paso $h$, el valor final de $x$ y el **orden** $k$ del polinomio de Taylor deseado.
5. Calcular simbólicamente las derivadas totales de orden superior de $f(x,y)$ con respecto a $x$ utilizando la regla de la cadena, hasta llegar al orden $k$.
6. Calcular el número total de pasos necesarios.
7. Iniciar un ciclo para cada paso iterativo:
   - Evaluar numéricamente cada una de las derivadas calculadas en el punto actual $(x_i, y_i)$.
   - Multiplicar cada evaluación por $\frac{h^j}{j!}$ (donde $j$ es el orden de esa derivada específica) y sumar todos los términos al valor actual $y_i$.
   - Avanzar el valor de $x$: $x_{i+1} = x_i + h$.
8. Mostrar el valor estimado de $y$.
9. **Fin.**

---

## Código Fuente
* [Taylor en python](./taylor_edo.py)
  
---

## Compilación con datos de entrada y de salida

### Ejemplo 1: Taylor de Orden 2
Resolver $dy/dx = x - y$
* **Datos de entrada:**
    * Ecuación $f(x, y)$: `x - y`
    * $x$ inicial ($x_0$): `0`
    * $y$ inicial ($y_0$): `2`
    * Tamaño del paso ($h$): `0.1`
    * Orden de Taylor ($k$): `2`
    * $x$ final a evaluar: `0.2`
* **Datos de salida:**
    * Iteración 1: $x = 0.100$, $y = 1.815000$
    * Iteración 2: $x = 0.200$, $y = 1.656150$
    * Resultado final estimado en $x = 0.2$: `1.656150`

### Ejemplo 2: Mayor precisión (Orden 4)
Resolver la misma ecuación $dy/dx = x - y$
* **Datos de entrada:**
    * Ecuación $f(x, y)$: `x - y`
    * $x$ inicial ($x_0$): `0`
    * $y$ inicial ($y_0$): `2`
    * Tamaño del paso ($h$): `0.1`
    * Orden de Taylor ($k$): `4`
    * $x$ final a evaluar: `0.2`
* **Datos de salida:**
    * Iteración 1: $x = 0.100$, $y = 1.814513$
    * Iteración 2: $x = 0.200$, $y = 1.655494$
    * Resultado final estimado en $x = 0.2$: `1.655494`

---

## Problemario
https://drive.google.com/file/d/1vN8_-Q39ma0lwOa0vDzmYkyOkVhOT3xx/view?usp=sharing

---

🔙 [Volver al Índice Principal](../../README.md)
