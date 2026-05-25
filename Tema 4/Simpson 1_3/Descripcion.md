# Regla de Simpson 1/3

## Descripción
La regla de Simpson 1/3 es un método de integración numérica que aproxima el valor de una integral definida (el área bajo la curva) conectando grupos de tres puntos sucesivos en la función utilizando polinomios de segundo grado (parábolas). Es significativamente más precisa que la regla del trapecio. Para aplicar este método en su forma compuesta, es un requisito matemático estricto que el número total de subintervalos ($n$) sea un número par.

---

## Ecuación / Fórmula
La fórmula para la aplicación compuesta de la regla de Simpson 1/3, dividiendo el área en $n$ subintervalos de ancho igual, es:

$$\int_{a}^{b} f(x) dx \approx \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1, 3, 5...}^{n-1} f(x_i) + 2 \sum_{i=2, 4, 6...}^{n-2} f(x_i) + f(x_n) \right]$$

Donde:
- $h = \frac{b - a}{n}$ (el ancho de cada subintervalo).
- $x_0 = a$ (límite inferior).
- $x_n = b$ (límite superior).

---

## Algoritmo
1. **Inicio.**
2. Definir la función $f(x)$, el límite inferior $a$, el límite superior $b$ y el número de intervalos $n$.
3. Verificar si $n$ es un número par. Si es impar, el método falla y se debe solicitar un nuevo valor.
4. Calcular el ancho del intervalo: $h = (b - a) / n$.
5. Evaluar la función en los extremos y sumarlos: $Suma = f(a) + f(b)$.
6. Iniciar un ciclo desde $i = 1$ hasta $n - 1$:
   - Calcular el punto actual: $x_i = a + i \cdot h$.
   - Si el índice $i$ es impar, multiplicar $f(x_i)$ por 4 y agregarlo a la $Suma$.
   - Si el índice $i$ es par, multiplicar $f(x_i)$ por 2 y agregarlo a la $Suma$.
7. Multiplicar la $Suma$ total por el factor $\frac{h}{3}$.
8. Mostrar el resultado de la integral aproximada.
9. **Fin.**

---

## Código Fuente
* [Simpson 1_3 en python](./Codigo.py)

---

## Compilación con datos de entrada y de salida

### Ejemplo 1: Función Polinómica
* **Datos de entrada:**
    * Función: `x**4`
    * Límite inferior ($a$): `0`
    * Límite superior ($b$): `2`
    * Número de intervalos ($n$): `4` (Debe ser par)
* **Datos de salida:**
    * Ancho del intervalo ($h$): `0.500000`
    * Área aproximada (Integral): `6.416667` *(El valor exacto es 6.4)*

### Ejemplo 2: Función Logarítmica
* **Datos de entrada:**
    * Función: `log(x)`
    * Límite inferior ($a$): `1`
    * Límite superior ($b$): `3`
    * Número de intervalos ($n$): `6`
* **Datos de salida:**
    * Ancho del intervalo ($h$): `0.333333`
    * Área aproximada (Integral): `1.295837` *(El valor exacto es aprox 1.295836)*
---

## Problemario
https://drive.google.com/file/d/1bb9TTtoZdWJ3CZQOTU05oKkxEsiogW8z/view?usp=drive_link

---

🔙 [Volver al Índice Principal](../../README.md)
