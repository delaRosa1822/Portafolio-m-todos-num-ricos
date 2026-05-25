# Método de Jacobi

## Descripción
El método de Jacobi es un algoritmo numérico iterativo utilizado para resolver sistemas de ecuaciones lineales. A diferencia de los métodos directos, comienza con una aproximación inicial (normalmente ceros) y refina los resultados iteración tras iteración. Su característica distintiva frente a Gauss-Seidel es que realiza **actualizaciones simultáneas**: calcula todos los nuevos valores de las incógnitas basándose únicamente en los valores de la iteración anterior, sin usar los resultados recién calculados hasta que termina el ciclo completo.

---

## Ecuación / Fórmula
Para un sistema de $n$ ecuaciones, el valor de la incógnita $x_i$ en la iteración $k+1$ se calcula utilizando exclusivamente los valores $x_j$ de la iteración anterior $k$:

$$ x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right) $$

Donde:
- $a_{ii}$ es el coeficiente en la diagonal principal.
- $b_i$ es el término independiente.
- $x_j^{(k)}$ son los valores de las incógnitas obtenidos en la iteración anterior (ninguno está actualizado al ciclo actual).

---

## Algoritmo
1. **Inicio.**
2. Identificar la matriz de coeficientes $A$ y el vector de términos independientes $B$.
3. Verificar si la matriz es "diagonalmente dominante" para garantizar que el método converja.
4. Establecer un vector de aproximaciones iniciales (usualmente ceros), una tolerancia de error y un límite máximo de iteraciones.
5. Para cada ecuación $i$, calcular el nuevo valor temporal de $x_i$ usando los valores fijos de la iteración anterior.
6. Una vez calculados todos los nuevos valores temporales, actualizar el vector principal de soluciones simultáneamente.
7. Calcular el error absoluto máximo entre los nuevos valores y los antiguos.
8. Si el error es menor a la tolerancia, terminar y mostrar resultados. Si no, repetir desde el paso 5.
9. **Fin.**

---

## Código Fuente
* [Método de jacobi en python](./jacobi.py)

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
    * Iteraciones requeridas: 11
    * `x_0 = 2.0`
    * `x_1 = 1.0`
    * `x_2 = 1.0`

*(Nota: En comparación, Gauss-Seidel resuelve este mismo sistema en 6 iteraciones debido a su actualización secuencial).*
## Problemario
https://drive.google.com/file/d/1uJzHxw1KtA_l0951911ma6kquPS7wDDU/view?usp=drive_link
---
🔙 [Volver al Índice Principal](../../README.md)
