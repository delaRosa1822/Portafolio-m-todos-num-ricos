# Método de Gauss-Seidel

## Descripción
El método de Gauss-Seidel es un algoritmo numérico iterativo utilizado para resolver sistemas de ecuaciones lineales. A diferencia de los métodos directos que buscan una solución exacta en un número finito de pasos, este método parte de una estimación inicial (generalmente ceros) y la mejora iteración tras iteración. Su característica principal es que utiliza los valores actualizados de las incógnitas tan pronto como se calculan dentro de la misma iteración, lo que acelera su convergencia.

---

## Ecuación / Fórmula
Para un sistema de $n$ ecuaciones, el valor de la incógnita $x_i$ en la iteración $k+1$ se calcula despejando $x_i$ de su respectiva ecuación y sustituyendo los valores más recientes:

$$ x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} x_j^{(k)} \right) $$

Donde:
- $a_{ii}$ es el coeficiente en la diagonal principal.
- $b_i$ es el término independiente.
- Los $x_j^{(k+1)}$ son los valores ya calculados en la iteración actual.
- Los $x_j^{(k)}$ son los valores de la iteración anterior que aún no se han actualizado.

---

## Algoritmo
1. **Inicio.**
2. Escribir el sistema de ecuaciones e identificar la matriz de coeficientes $A$ y el vector de términos independientes $B$.
3. Verificar si el sistema es "diagonalmente dominante" (el valor absoluto del elemento en la diagonal principal de cada fila debe ser mayor que la suma de los valores absolutos del resto de los elementos de esa fila). Esto garantiza que el método converja.
4. Establecer un vector de aproximaciones iniciales (usualmente $x_i = 0$), una tolerancia de error y un límite de iteraciones.
5. Para cada ecuación $i$ (desde $1$ hasta $n$), despejar $x_i$ y calcular su nuevo valor usando las estimaciones más recientes de las demás variables.
6. Calcular el error (la diferencia entre los nuevos valores calculados y los anteriores).
7. Si el error es menor a la tolerancia, los valores actuales son la solución. Si no, repetir el paso 5.
8. **Fin.**

---

## Código Fuente
El código completo está en el archivo `gauss_seidel.py`. Está diseñado de forma muy práctica y amigable para principiantes utilizando **NumPy**, separando claramente la inicialización del sistema y el ciclo de iteraciones.

---

## Compilación con datos de entrada y de salida

### Caso de Prueba: Sistema 3x3 Diagonalmente Dominante
Sistema a resolver:
1) $5x - y + z = 10$
2) $2x + 8y - z = 11$
3) $-x + y + 4z = 3$

* **Datos de entrada:**
    * Número de incógnitas: `3`
    * Fila 1: `5, -1, 1, 10`
    * Fila 2: `2, 8, -1, 11`
    * Fila 3: `-1, 1, 4, 3`
    * Tolerancia: `0.001`
* **Datos de salida:**
    * Iteraciones requeridas: 6
    * `x_0 = 2.0`
    * `x_1 = 1.0`
    * `x_2 = 1.0`

---

## Notas sobre el Algoritmo y la Codificación
En el código fuente, si bien la lógica central sigue la fórmula al pie de la letra, se agregó una función previa que evalúa estrictamente si la matriz ingresada es **diagonalmente dominante**. El algoritmo clásico a veces asume que el usuario ya preparó el sistema, pero a nivel de programación es fundamental realizar esta validación, ya que si la matriz no cumple esta condición, el método de Gauss-Seidel podría divergir (los valores se irían al infinito en lugar de encontrar la solución). El código avisa al usuario si esto ocurre.
