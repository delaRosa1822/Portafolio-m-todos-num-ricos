## Código Fuente
```python
# Ejemplo de Interpolación Cuadrática en Python

# 1. Definimos nuestros tres puntos conocidos
# (En este caso, simulamos la curva y = x^2 para probar la precisión)
x0, y0 = 1.0, 1.0
x1, y1 = 2.0, 4.0
x2, y2 = 3.0, 9.0

# 2. Definimos el valor de 'x' que queremos buscar
x_objetivo = 2.5

# 3, 4 y 5. Calculamos cada término de la fórmula de Lagrange por separado
termino_0 = y0 * ((x_objetivo - x1) * (x_objetivo - x2)) / ((x0 - x1) * (x0 - x2))
termino_1 = y1 * ((x_objetivo - x0) * (x_objetivo - x2)) / ((x1 - x0) * (x1 - x2))
termino_2 = y2 * ((x_objetivo - x0) * (x_objetivo - x1)) / ((x2 - x0) * (x2 - x1))

# 6. Sumamos los términos para obtener el valor interpolado
y_estimado = termino_0 + termino_1 + termino_2

# 7. Mostramos los resultados
print("--- Interpolación Cuadrática ---")
print(f"Puntos: ({x0}, {y0}), ({x1}, {y1}), ({x2}, {y2})")
print(f"Para x = {x_objetivo}, el valor estimado de y es: {y_estimado}")
