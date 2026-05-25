# Método de Falsa Posición (Regula Falsi)

## ¿Qué es?
Es un método numérico cerrado para encontrar raíces de ecuaciones. Este método requiere dos valores iniciales (un intervalo $[a, b]$) que encierren la raíz. Funciona uniendo los puntos de la función evaluada en esos límites con una línea recta (la "falsa posición" de la curva) y calcula dónde esa recta cruza el eje x para encontrar una nueva aproximación más precisa.

---

## Fórmula
La ecuación para calcular la nueva aproximación (la raíz $x_r$) es:

$$ x_r = b - \frac{f(b)(a - b)}{f(a) - f(b)} $$

---

## Algoritmo
1. **Inicio.**
2. Definir la función $f(x)$.
3. Elegir dos valores iniciales $a$ y $b$ tales que la función cambie de signo en el intervalo, es decir, $f(a) \cdot f(b) < 0$.
4. Establecer la tolerancia de error y el número máximo de iteraciones.
5. Calcular la aproximación $x_r$ usando la fórmula de la falsa posición.
6. Evaluar el producto $f(a) \cdot f(x_r)$:
   - Si es menor a 0, la raíz está en el subintervalo $[a, x_r]$. Actualizar $b = x_r$.
   - Si es mayor a 0, la raíz está en el subintervalo $[x_r, b]$. Actualizar $a = x_r$.
   - Si es igual a 0, $x_r$ es la raíz exacta.
7. Calcular el error y verificar si es menor a la tolerancia. Si no lo es, repetir desde el paso 5.
8. **Fin.**

---

## Código Fuente
* [Falsa Posición en python](./falsa_posicion.py)

---

## Compilación con datos de entrada y de salida

### Ejemplo 1: Función Polinómica
* **Datos de entrada:**
    * Función: `x**3 - x - 2`
    * Límite inferior ($a$): `1`
    * Límite superior ($b$): `2`
* **Datos de salida:**
    * Iteraciones: 8
    * Raíz aproximada: `1.521380`

### Ejemplo 2: Función Logarítmica
* **Datos de entrada:**
    * Función: `log(x) - x + 2`
    * Límite inferior ($a$): `3`
    * Límite superior ($b$): `4`
* **Datos de salida:**
    * Iteraciones: 3
    * Raíz aproximada: `3.146193`

---

🔙 [Volver al Índice Principal](../../README.md)
