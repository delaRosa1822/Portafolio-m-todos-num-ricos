# Ejemplo de Interpolación Lineal en Python

# 1 y 2. Definimos nuestros dos puntos conocidos
x0 = 2.0
y0 = 4.0

x1 = 6.0
y1 = 12.0

# 3. Definimos el valor de 'x' que queremos interpolar
x_objetivo = 4.0

# 4, 5 y 6. Aplicamos la fórmula de interpolación lineal
pendiente = (y1 - y0) / (x1 - x0)
y_estimado = y0 + pendiente * (x_objetivo - x0)

# 7. Mostramos los resultados en consola
print("--- Interpolación Lineal ---")
print(f"Punto conocido 1: ({x0}, {y0})")
print(f"Punto conocido 2: ({x1}, {y1})")
print(f"Para x = {x_objetivo}, el valor estimado de y es: {y_estimado}")
