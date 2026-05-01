Error de Redondeo Binario

## ¿Qué es?
El error de redondeo binario es una limitación física de las computadoras. Así como en nuestro sistema decimal (base 10) no podemos escribir el número exacto de la fracción $1/3$ (porque es $0.333333...$ infinito), las computadoras usan el sistema binario (base 2) y no pueden representar exactamente fracciones simples como $0.1$ o $0.2$. 

El sistema convierte ese $0.1$ en una fracción binaria periódica infinita y, como la memoria de la computadora es limitada (generalmente a 64 bits según el estándar IEEE 754), tiene que "cortar" o redondear el número en algún punto. Ese corte genera un minúsculo error de precisión desde el momento en que se guarda el número.

## Fórmula
Podemos expresar esto observando cómo el sistema decimal se traduce a binario. El número $0.1$ en binario es una secuencia infinita:

0.1_{10} = 0.00011001100110011..._2

Al realizar la suma de 0.1 + 0.2, el redondeo oculto en ambos números produce un remanente. El error se calcula como:

E = | Valor\_Real - Valor\_Aproximado |
E = | 0.3 - 0.30000000000000004 | = 0.00000000000000004

## Algoritmo
1. Definir dos variables con valores decimales que sean problemáticos en binario (ej. `0.1` y `0.2`).
2. Sumar ambas variables y guardar el resultado.
3. Imprimir el resultado en pantalla.
4. Observar que el resultado no es exactamente `0.3` debido a los bits adicionales generados por el redondeo de la máquina.

Entrada: 
numero1 = 0.1
numero2 = 0.2
Operación: numero1 + numero2

Salida:
La suma de 0.1 + 0.2 es:
0.30000000000000004
