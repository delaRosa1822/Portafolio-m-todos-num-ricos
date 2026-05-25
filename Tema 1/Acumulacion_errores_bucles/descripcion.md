# Acumulación de errores en bucles

## ¿Qué es?
La acumulación de errores en bucles ocurre cuando realizamos miles de operaciones aritméticas consecutivas utilizando números de punto flotante (decimales). Como las computadoras no pueden representar fracciones como `0.01` de forma exacta en sistema binario, se genera un minúsculo error de redondeo en cada operación. Al repetir esta operación muchas veces dentro de un ciclo, estos pequeños errores se van sumando, resultando en una desviación significativa al final del proceso.

## Fórmula
Para medir la desviación generada al final del bucle, calculamos el **Error Absoluto**, que es la diferencia entre el valor exacto que esperábamos y el valor aproximado que nos dio la máquina:

$$E_a = | Valor\_Real\_Esperado - Valor\_Aproximado |$$

En nuestro caso:
$$E_a = | 10.00 - 9.999999999999831 | = 0.000000000000169$$

## Algoritmo
1. Inicializar una variable acumuladora (ej. `saldo`) en 0.0.
2. Iniciar un ciclo o bucle que se repita 1000 veces.
3. En cada iteración del bucle, sumarle 0.01 a la variable acumuladora.
4. Al finalizar el ciclo, imprimir el valor que esperábamos obtener (10.00).
5. Imprimir el valor real obtenido para observar el margen de error acumulado.

## Codigo fuente


Entrada: 
Ciclos del bucle: 1000
Incremento en cada ciclo: 0.01

Salida:
Saldo esperado: 10.00
Saldo real: 9.999999999999831

