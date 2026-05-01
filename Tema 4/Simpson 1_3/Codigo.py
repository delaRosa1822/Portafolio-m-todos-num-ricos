# 1. Definimos la función a integrar (ejemplo: f(x) = x^2)
def f(x):
    return x**2

# 2. Definimos los límites de integración
a = 0.0
b = 2.0

# 3 y 4. Calculamos el punto medio (m) y el tamaño del paso (h)
m = (a + b) / 2.0
h = (b - a) / 2.0

# 5 y 6. Aplicamos la fórmula simple de Simpson 1/3
integral = (h / 3.0) * (f(a) + 4 * f(m) + f(b))

# 7. Mostramos los resultados en consola
print("--- Método de Simpson 1/3 (Simple) ---")
print(f"Límite inferior (a): {a}")
print(f"Límite superior (b): {b}")
print(f"Aproximación del área: {integral}")
