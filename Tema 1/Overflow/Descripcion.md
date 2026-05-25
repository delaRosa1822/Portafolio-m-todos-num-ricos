## ¿Qué es?
A diferencia de los errores de punto flotante (decimales), el desbordamiento silencioso ocurre con tipos de datos enteros (`int`, `long`). En la mayoría de los lenguajes de programación (como Java o C++), las variables tienen un límite estricto de memoria. Si una operación matemática supera el valor máximo positivo que puede almacenar la variable, el sistema no lanza ninguna advertencia o error (excepción); simplemente "da la vuelta" como si fuera un odómetro o un reloj, volviendo al número más pequeño posible (un número negativo enorme), lo que destruye por completo la exactitud del cálculo.

*Nota: Python maneja números enteros de tamaño arbitrario de forma nativa, por lo que no sufre de este desbordamiento automáticamente. Para este ejemplo, simulamos el límite estricto de 32 bits usando la librería `ctypes`.*

## Fórmula
El comportamiento de "dar la vuelta" en un sistema binario de 32 bits con signo (Complemento a 2) se puede expresar de la siguiente manera al alcanzar el límite positivo:

Valor\_Maximo + 1 = Valor\_Minimo\_Negativo

Sustituyendo por los límites reales de 32 bits:
(2^{31} - 1) + 1 = -2^{31}
$$2147483647 + 1 = -2147483648

## Algoritmo
1. Importar la librería necesaria para simular límites de memoria de 32 bits.
2. Declarar una variable con el valor máximo permitido para un entero estándar (2,147,483,647).
3. Sumar `1` a este valor máximo.
4. Aplicar el límite de 32 bits al resultado para provocar el desbordamiento.
5. Imprimir el valor original y el resultado de la suma para observar cómo el número positivo gigante se transformó en un número negativo.

Entrada: 
maximo = 2147483647
Operación: maximo + 1 (en un entorno de 32 bits)

Salida:
Valor Max: 2147483647
Valor Maximo + 1: -2147483648

## Código Fuente
* [Overflow en python](./overflow.py)
---

## Problemario
https://drive.google.com/file/d/1yPJyQ21aJCbsrpvLeyoU1FiKDvC7gtZt/view?usp=drive_link
🔙 [Volver al Índice Principal](../../README.md)
