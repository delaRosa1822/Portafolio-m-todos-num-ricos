# Cancelación por Resta (Loss of Significance)

## ¿Qué es?
La cancelación por resta (o cancelación catastrófica) ocurre cuando restamos dos números de punto flotante que son extremadamente cercanos o casi idénticos. Al hacer la resta, los dígitos más significativos (los de la izquierda, que coinciden en ambos números) se cancelan y desaparecen. 

El problema es que la computadora debe llenar el espacio vacío resultante, y lo hace dejando expuestos los "dígitos basura" que se generaron por el error de redondeo binario inicial. Como resultado, pierdes toda la precisión y te quedas con un número que es básicamente el puro margen de error de la máquina.

## Fórmula
Matemáticamente, si restamos nuestros dos números exactos, el resultado debería ser:
1.000000000000002 - 1.000000000000001 = 0.000000000000001
(o\ 1.0 \times 10^{-15})

Sin embargo, debido a la representación binaria interna, la computadora calcula un número totalmente distinto. Podemos medir el error absoluto de la siguiente forma:
E_a = | Valor\_Real\_Esperado - Valor\_Calculado |
E_a = | 1.0 \times 10^{-15} - 2.220446049250313 \times 10^{-16} |

## Algoritmo
1. Definir una variable (`x`) con un número decimal con muchos dígitos de precisión.
2. Definir una variable (`y`) con un número decimal casi idéntico al anterior.
3. Realizar la resta de `x - y`.
4. Imprimir el resultado para observar cómo la diferencia esperada es reemplazada por un valor residual incorrecto.

Entrada: 
x = 1.000000000000002
y = 1.000000000000001
Operación: x - y

Salida:
Resultado de la resta:
2.220446049250313e-16
