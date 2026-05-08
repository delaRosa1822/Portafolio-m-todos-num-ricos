import math

def interpolacion_lineal(x0, y0, x1, y1, x):
    """
    Realiza una interpolación lineal para estimar el valor de y en un punto x dado.
    
    Argumentos:
    x0, y0: Coordenadas del primer punto conocido.
    x1, y1: Coordenadas del segundo punto conocido.
    x: El valor de x donde se desea hacer la estimación.
    
    Retorna:
    El valor de y estimado (float).
    """
    if x1 == x0:
        raise ValueError("x1 no puede ser igual a x0 (división por cero).")
        
    y = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)
    return y

# --- Compilación con Datos de Entrada y Salida (Ejemplo) ---
print("--- EJEMPLO DE COMPILACIÓN: INTERPOLACIÓN LINEAL ---")

# Datos de Entrada
point_0 = (2, 4)    # (x0, y0)
point_1 = (5, 10)   # (x1, y1)
x_estimate = 3      # Valor de x a estimar

# Cálculo
try:
    y_result = interpolacion_lineal(point_0[0], point_0[1], point_1[0], point_1[1], x_estimate)
    
    # Datos de Salida
    print(f"Punto 0 conocido: {point_0}")
    print(f"Punto 1 conocido: {point_1}")
    print(f"Se estimó el valor en x = {x_estimate}")
    print(f"-----------------------------------")
    print(f"Resultado estimado en y: {y_result:.4f}")
    
except ValueError as e:
    print(f"Error: {e}")

print("-----------------------------------------------------")
