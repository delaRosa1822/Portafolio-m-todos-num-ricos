def interpolacion_cuadratica(x0, y0, x1, y1, x2, y2, x):
    """
    Realiza una interpolación cuadrática (usando Polinomio de Lagrange) 
    para estimar el valor de y en un punto x dado, basándose en tres puntos.
    
    Argumentos:
    x0, y0, x1, y1, x2, y2: Coordenadas de los tres puntos conocidos.
    x: El valor de x donde se desea hacer la estimación.
    
    Retorna:
    El valor de y estimado (float).
    """
    # Verificación de que los valores de x sean distintos para evitar división por cero
    if x0 == x1 or x0 == x2 or x1 == x2:
        raise ValueError("Los valores de x0, x1 y x2 deben ser distintos entre sí.")

    # Cálculo de los términos de Lagrange (L0, L1, L2)
    l0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    l1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    l2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    
    # Suma ponderada de los valores y_i por sus términos L_i
    y = (y0 * l0) + (y1 * l1) + (y2 * l2)
    return y

# --- Compilación con Datos de Entrada y Salida (Ejemplo) ---
print("--- EJEMPLO DE COMPILACIÓN: INTERPOLACIÓN CUADRÁTICA ---")

# Datos de Entrada (Puntos que siguen y = x^2 para verificar)
point_0 = (0, 0)    # (x0, y0)
point_1 = (1, 1)    # (x1, y1)
point_2 = (2, 4)    # (x2, y2)
x_estimate = 1.5    # Valor de x a estimar

# Cálculo
try:
    y_result = interpolacion_cuadratica(point_0[0], point_0[1], point_1[0], point_1[1], point_2[0], point_2[1], x_estimate)
    
    # Datos de Salida
    print(f"Punto 0 conocido: {point_0}")
    print(f"Punto 1 conocido: {point_1}")
    print(f"Punto 2 conocido: {point_2}")
    print(f"Se estimó el valor en x = {x_estimate}")
    print(f"-----------------------------------")
    print(f"Resultado estimado en y: {y_result:.4f}")
    
except ValueError as e:
    print(f"Error: {e}")
