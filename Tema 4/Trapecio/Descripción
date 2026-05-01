# Regla del Trapecio

## Descripción
La regla del trapecio es uno de los métodos de integración numérica más básicos y directos para aproximar el área bajo una curva (la integral definida). Funciona uniendo los puntos de la función con líneas rectas, formando así trapecios en lugar de los rectángulos que se usan en las sumas de Riemann. En su aplicación compuesta, el área total se divide en $n$ subintervalos (múltiples trapecios pequeños) para reducir el error de estimación.

---

## Ecuación / Fórmula
La fórmula general para la regla del trapecio compuesta con $n$ subintervalos de igual ancho es:

$$ \int_{a}^{b} f(x) dx \approx \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right] $$

Donde:
- $h = \frac{b - a}{n}$ (el ancho de cada subintervalo o trapecio).
- $x_0 = a$ (límite inferior).
- $x_n = b$ (límite superior).

---

## Algoritmo
1. **Inicio.**
2. Definir la función a integrar $f(x)$.
3. Proporcionar el límite inferior $a$, el límite superior $b$ y el número total de trapecios (intervalos) $n$.
4. Validar que el número de intervalos $n$ sea al menos 1.
5. Calcular el ancho de cada intervalo: $h = (b - a) / n$.
6. Evaluar la función en los extremos y sumarlos: $Suma = f(a) + f(b)$.
7. Iniciar un ciclo desde $i = 1$ hasta $n - 1$:
   - Calcular la posición del punto actual: $x_i = a + i \cdot h$.
   - Evaluar $f(x_i)$, multiplicarlo por 2 y agregarlo a la $Suma$.
8. Multiplicar la $Suma$ total por el factor $\frac{h}{2}$.
9. Mostrar el resultado como el área aproximada.
10. **Fin.**

---

## Código Fuente
El código fuente se encuentra en el archivo `trapecio.py`. Utiliza la librería **SymPy** para leer la función matemática como un texto y convertirla en una expresión evaluable de forma dinámica.

---

## Compilación con datos de entrada y de salida

### Ejemplo 1: Función Polinómica
* **Datos de entrada:**
    * Función: `x**2`
    * Límite inferior ($a$): `0`
    * Límite superior ($b$): `2`
    * Número de intervalos ($n$): `4`
* **Datos de salida:**
    * Ancho del intervalo ($h$): `0.500000`
    * Área aproximada (Integral): `2.750000` *(El valor exacto es 2.666...)*

### Ejemplo 2: Función Exponencial
* **Datos de entrada:**
    * Función: `exp(x)`
    * Límite inferior ($a$): `0`
    * Límite superior ($b$): `1`
    * Número de intervalos ($n$): `5`
* **Datos de salida:**
    * Ancho del intervalo ($h$): `0.200000`
    * Área aproximada (Integral): `1.724006` *(El valor exacto es aprox. 1.71828)*

---

## Notas sobre el Algoritmo y la Codificación
En el código de Python, a diferencia del diagrama matemático general, se incluyó una validación lógica que impide que el usuario ingrese un valor de $n \le 0$. Matemáticamente no se pueden formar "cero trapecios" ni trapecios negativos, y si $n=0$, el cálculo del ancho $h$ provocaría un error fatal en el programa por división entre cero. El código detiene amablemente la ejecución si detecta esta entrada inválida.
