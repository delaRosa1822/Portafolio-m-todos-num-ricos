# Método de Newton-Raphson

## ¿Qué es?
Es un algoritmo eficiente para encontrar aproximaciones de las raíces (ceros) de una función real. Utiliza la recta tangente a la curva para acercarse iterativamente al valor donde la función cruza el eje x.

---

## Fórmula
La relación de recurrencia es:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

---

## Algoritmo
1. **Inicio.**
2. Definir la función $f(x)$ y obtener su derivada $f'(x)$.
3. Establecer un valor inicial $x_0$, una tolerancia y el máximo de iteraciones.
4. Calcular la siguiente aproximación: $x_{new} = x_{old} - (f(x_{old}) / f'(x_{old}))$.
5. Verificar si el error relativo es menor a la tolerancia.
6. Si cumple, mostrar el resultado. Si no, repetir el paso 4 usando $x_{new}$.
7. **Fin.**

---

## Código Fuente
El código fuente completo se encuentra en el archivo `newton_raphson.py` de este repositorio. Utiliza la librería **SymPy** para permitir el ingreso de cualquier función matemática y calcular su derivada automáticamente.

---

## Compilación con datos de entrada y de salida

### Ejemplo 1: Función Polinómica
* **Datos de entrada:**
    * Función: `x**2 - 2`
    * Punto inicial ($x_0$): `1`
* **Datos de salida:**
    * Iteraciones: 4
    * Raíz aproximada: `1.414214`

### Ejemplo 2: Función Trascendente
* **Datos de entrada:**
    * Función: `exp(-x) - x`
    * Punto inicial ($x_0$): `0`
* **Datos de salida:**
    * Iteraciones: 5
    * Raíz aproximada: `0.567143`

---

## Si el algoritmo es diferente a la codificación
En este caso, la codificación incluye una validación crítica que no siempre se menciona en el algoritmo básico: **la división por cero**. Si la derivada evaluada es 0, el programa lanza una alerta para evitar el error lógico de ejecución. Además, se implementó el uso de "Sympify" para que el programa sea dinámico y acepte cualquier entrada de texto como función matemática.
