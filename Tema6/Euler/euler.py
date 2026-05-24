import sympy as sp

def ejecutar_euler():
    print("--- Solución de EDOs: Método de Euler ---")
    
    # 1. Definición de variables simbólicas
    x, y = sp.symbols('x y')
    
    # 2. Entrada dinámica de la ecuación diferencial dy/dx = f(x, y)
    func_input = input("Introduce la ecuación f(x, y) (ejemplo: x + y): ")
    f = sp.sympify(func_input)
    f_num = sp.lambdify((x, y), f)  # Función evaluable con dos parámetros
    
    # 3. Entrada de condiciones iniciales y parámetros
    x0 = float(input("Introduce el valor inicial de x (x0): "))
    y0 = float(input("Introduce el valor inicial de y (y0): "))
    h = float(input("Introduce el tamaño de paso (h): "))
    x_final = float(input("Introduce el valor final de x a evaluar: "))
    
    # 4. Validación para evitar ciclos infinitos
    if h <= 0 or x_final <= x0:
        print("\n[Error]: El paso 'h' debe ser positivo y 'x_final' debe ser mayor que 'x0'.")
        return
        
    # Calcular el número de pasos necesarios
    pasos = int(round((x_final - x0) / h))
    
    xi = x0
    yi = y0
    
    print("\n--- Iniciando iteraciones ---")
    print("Punto inicial: x = {0:.4f}, y = {1:.6f}".format(xi, yi))
    
    # 5. Ciclo iterativo del método de Euler
    for i in range(1, pasos + 1):
        # Calcular la pendiente (evaluar la función en el punto actual)
        pendiente = f_num(xi, yi)
        
        # Aplicar la fórmula de Euler para el siguiente punto
        yi = yi + h * pendiente
        xi = xi + h
        
        print("Iteración {0}: x = {1:.4f}, y = {2:.6f}".format(i, xi, yi))
        
    # 6. Resultado final
    print("\n--- Resultado Final ---")
    print("El valor estimado de y en x = {0} es: {1:.6f}".format(x_final, yi))

if __name__ == "__main__":
    ejecutar_euler()
