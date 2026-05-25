# Método de Bisección

## ¿Qué es?
Es uno de los métodos numéricos cerrados más simples, intuitivos y confiables para encontrar las raíces de una ecuación. Funciona dividiendo repetidamente un intervalo a la mitad (bisección) y seleccionando el subintervalo donde la función cambia de signo, lo que garantiza matemáticamente que la raíz se encuentra "atrapada" en ese nuevo espacio.

---

## Fórmula
La fórmula para encontrar la nueva aproximación (que es simplemente el punto medio del intervalo actual) es:

$$ x_r = \frac{a + b}{2} $$

Donde:
- $x_r$ es la raíz aproximada (punto medio).
- $a$ es el límite inferior del intervalo.
- $b$ es el límite superior del intervalo.

---

## Algoritmo
1. **Inicio.**
2. Definir la función $f(x)$.
3. Elegir dos valores iniciales $a$ y $b$ tales que la función cambie de signo en el intervalo, es decir, $f(a) \cdot f(b) < 0$.
4. Establecer la tolerancia de error y el número máximo de iteraciones.
5. Calcular la aproximación $x_r$ usando la fórmula del punto medio: $x_r = (a + b) / 2$.
6. Evaluar el producto $f(a) \cdot f(x_r)$:
   - Si es menor a 0, la raíz está en el lado izquierdo. Actualizar el límite superior: $b = x_r$.
   - Si es mayor a 0, la raíz está en el lado derecho. Actualizar el límite inferior: $a = x_r$.
   - Si es igual a 0, $x_r$ es la raíz exacta.
7. Calcular el error y verificar si es menor a la tolerancia. Si no lo es, repetir desde el paso 5 con los nuevos límites.
8. **Fin.**

---

## Código Fuente
* [Biseccion en python](./biseccion.py)
---

## Compilación con datos de entrada y de salida

### Ejemplo 1: Función Polinómica
* **Datos de entrada:**
    * Función: `x**3 - x - 2`
    * Límite inferior ($a$): `1`
    * Límite superior ($b$): `2`
* **Datos de salida:**
    * Iteraciones: 14
    * Raíz aproximada: `1.521423`

### Ejemplo 2: Función Trigonométrica
* **Datos de entrada:**
    * Función: `cos(x) - x`
    * Límite inferior ($a$): `0`
    * Límite superior ($b$): `1`
* **Datos de salida:**
    * Iteraciones: 14
    * Raíz aproximada: `0.739075`

---

## Si el algoritmo es diferente a la codificación
En el código se agregó una validación de seguridad fundamental antes de iniciar el ciclo `while` o `for`: **la comprobación del Teorema de Bolzano**. El programa evalúa si `f(a) * f(b) >= 0`. Si el resultado es positivo o cero, significa que no hay garantía de que exista una raíz en ese intervalo (no hay cambio de signo), por lo que el programa arroja una alerta y detiene la ejecución para evitar procesar datos inútiles.
