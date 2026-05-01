Conversión Estrecha (Narrowing Primitive Conversion)

## ¿Qué es?
La conversión estrecha ocurre cuando intentamos guardar un tipo de dato de mayor capacidad (como un número de 64 bits o un decimal) dentro de una variable de menor capacidad (como un entero de 32 bits). El sistema, al no tener espacio suficiente, simplemente recorta o trunca los bits sobrantes más significativos. Esto puede cambiar drásticamente el valor original sin previo aviso, transformando incluso números positivos gigantes en números negativos.

*Nota sobre Python:* A diferencia de lenguajes como Java o C, Python maneja enteros de tamaño arbitrario de forma nativa (no se desbordan). Para simular o interactuar con este límite estricto de 32 bits en Python, podemos usar la librería `ctypes` o librerías numéricas como `numpy`.

## Fórmula
El comportamiento matemático de este desbordamiento (overflow) en un sistema de enteros con signo de 32 bits se calcula mediante aritmética modular:

Valor\_Truncado = Valor\_Original \pmod{2^{32}}

*(Si el resultado de los bits cae en el rango de los números negativos según el complemento a dos, el número se vuelve negativo).*

## Algoritmo
1. Importar la librería necesaria para simular tipos de datos estrictos (`ctypes`).
2. Definir un número enorme que supere el límite máximo de un entero estándar de 32 bits (2,147,483,647).
3. Forzar la conversión (cast) de ese número gigante a un formato estricto de 32 bits con signo.
4. Imprimir el valor original intacto.
5. Imprimir el valor resultante tras la conversión estrecha para observar la pérdida masiva de información.

Entrada: 
numero_grande = 7000000000

Salida:
Valor original: 7000000000
Valor tras el corte: -1589934592
