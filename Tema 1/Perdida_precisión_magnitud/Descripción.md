## ¿Qué es?
Cuando operamos con números de punto flotante que tienen magnitudes drásticamente diferentes (uno gigante y uno diminuto), el número más pequeño puede "desaparecer". Esto sucede porque, bajo el estándar IEEE 754, la memoria asignada para guardar los dígitos de un número (la *mantisa*) tiene un límite físico (53 bits para precisión doble, que equivalen a unos 15-17 dígitos decimales). 

Para sumar dos números, la computadora primero debe alinear sus puntos decimales. Al hacer esto con una diferencia de magnitud tan grande, los dígitos del número pequeño son empujados fuera del espacio disponible en la memoria y simplemente se truncan o descartan.

## Fórmula
Podemos ilustrar esto observando la suma real frente a la capacidad de la máquina.

Matemáticamente:
$$1.0 \times 10^{16} + 1.0 \times 10^{-1} = 10000000000000000.1$$

Sin embargo, en precisión doble, los enteros exactos se mantienen seguros hasta el límite de $2^{53} - 1$ (aproximadamente $9.0 \times 10^{15}$). Al tener $10^{16}$, hemos ocupado toda la mantisa con el lado entero. Por lo tanto, el sistema descarta la fracción:
$$10000000000000000.1 \approx 1.0 \times 10^{16}$$

## Algoritmo
1. Definir una variable (`A`) con un número de punto flotante de una magnitud muy grande (ej. un 1 seguido de 16 ceros).
2. Definir una variable (`B`) con un número de punto flotante de magnitud muy pequeña (ej. 0.1).
3. Sumar ambas variables.
4. Imprimir los valores originales y el resultado de la suma para observar cómo el valor de `B` no afectó en lo absoluto al valor de `A`.

   
Entrada: 
a = 10000000000000000.0
b = 0.1

Salida:
Valor de A: 1e+16
Valor de B: 0.1
Suma (A + B): 1e+16

## Código Fuente
* [Perdida_precision_magnitud en python](./codigo.py)
---

## Problemario
https://drive.google.com/file/d/1yPJyQ21aJCbsrpvLeyoU1FiKDvC7gtZt/view?usp=drive_link
---

🔙 [Volver al Índice Principal](../../README.md)
