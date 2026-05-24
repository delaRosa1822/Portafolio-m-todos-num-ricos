# Método de Gauss-Jordan

## Descripción
El método de Gauss-Jordan es un algoritmo de álgebra lineal que se utiliza para resolver sistemas de ecuaciones lineales, así como para encontrar la matriz inversa. Consiste en aplicar una secuencia de operaciones elementales por filas para transformar la matriz aumentada del sistema en una matriz identidad (donde la diagonal principal está compuesta por unos y el resto de los elementos son ceros). Una vez lograda esta estructura, el valor de cada incógnita se lee directamente en la última columna.

---

## Ecuación / Fórmula
El proceso se basa en operaciones elementales donde se calcula un factor para anular los elementos por encima y por debajo de la diagonal principal, y se normaliza la fila para que el pivote sea igual a 1:

1. **Normalización del pivote:**
$$ F_{pivote} \leftarrow \frac{F_{pivote}}{a_{jj}} $$

2. **Eliminación en otras filas:**
$$ F_i \leftarrow F_i - (a_{ij} \cdot F_{pivote}) $$

Donde:
- $F_i$ es la fila que se va a modificar.
- $a_{jj}$ es el elemento en la diagonal (pivote).
- $a_{ij}$ es el elemento que se desea convertir en cero.

---

## Algoritmo
1. **Inicio.**
2. Representar el sistema de ecuaciones como una matriz aumentada $[A | B]$.
3. Para cada columna $j$ (desde la primera hasta la última incógnita):
   - Localizar el elemento en la diagonal principal $a_{jj}$ (pivote).
   - Dividir toda la fila $j$ entre $a_{jj}$ para que el pivote se convierta en $1$.
   - Para cada fila $i$ del sistema (excepto la fila $j$):
     - Multiplicar la fila $j$ (que ahora tiene un $1$ en el pivote) por el valor $a_{ij}$.
     - Restar este resultado a la fila $i$ para que el elemento $a_{ij}$ se convierta en $0$.
4. Al finalizar el ciclo de todas las columnas, la matriz $A$ se habrá convertido en una matriz identidad.
5. Los valores resultantes en el vector $B$ son la solución directa de las incógnitas.
6. **Fin.**

---

## Código Fuente
El código fuente completo se encuentra en el archivo `gauss_jordan.py`. El script utiliza la librería **NumPy** en Python para manejar las matrices de manera práctica y ejecutar las operaciones por filas mediante arreglos multidimensionales.

---

## Compilación con datos de entrada y de salida

### Caso de Prueba: Sistema de 3x3
Sistema a resolver:
1) $2x + y - z = 8$
2) $-3x - y + 2z = -11$
3) $-2x + y + 2z = -3$

* **Datos de entrada:**
    * Número de incógnitas: `3`
    * Fila 1: `2, 1, -1, 8`
    * Fila 2: `-3, -1, 2, -11`
    * Fila 3: `-2, 1, 2, -3`
* **Datos de salida:**
    * `x_0 = 2.0`
    * `x_1 = 3.0`
    * `x_2 = -1.0`

---

---

## Notas sobre el Algoritmo y la Codificación
En la codificación en Python, se incorporó un bloque de instrucciones para realizar **Pivoteo Parcial**. El algoritmo matemático teórico asume que los elementos de la diagonal nunca son cero, pero en la práctica computacional, si el programa encuentra un cero en la diagonal, la operación de normalización causaría un error por "división entre cero". El código identifica esto, busca la fila inferior con el mayor valor absoluto en esa columna y las intercambia automáticamente antes de realizar las divisiones.
