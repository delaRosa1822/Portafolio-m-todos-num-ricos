# Comparación Directa con == 

## ¿Qué es?
Debido a los errores de redondeo en el sistema binario (punto flotante), realizar una operación matemática con números decimales y luego comparar el resultado directamente usando el operador de igualdad (`==`) suele fallar. Aunque matemáticamente dos valores deberían ser idénticos (por ejemplo, `1.1 - 1.0` y `0.1`), en la memoria de la computadora el resultado de la operación tiene decimales extra minúsculos que hacen que la comparación estricta resulte falsa.

## Fórmula
Para demostrar por qué falla la comparación, podemos calcular la diferencia real (el error) entre el resultado de la operación y el número esperado:

Error = | (1.1 - 1.0) - 0.1 |
Error = | 0.10000000000000009 - 0.1 | = 0.00000000000000009


## Algoritmo
1. Realizar una operación matemática simple con números decimales (ej. restar 1.0 de 1.1).
2. Imprimir el resultado de la operación para observar cómo lo almacenó la computadora.
3. Utilizar una estructura condicional (`if/else`) para comparar si el resultado es estrictamente igual (`==`) al valor esperado (0.1).
4. Imprimir un mensaje en consola dependiendo de si la comparación fue verdadera o falsa.

Entrada: 
Operación: 1.1 - 1.0
Condición a evaluar: resultado == 0.1

Salida:
Resultado de la resta: 0.10000000000000009
No es 0.1!

## Código Fuente
* [Comparacion en python](./Comparacion.py)
---

## Problemario
https://drive.google.com/file/d/1yPJyQ21aJCbsrpvLeyoU1FiKDvC7gtZt/view?usp=drive_link
---

🔙 [Volver al Índice Principal](../../README.md)
