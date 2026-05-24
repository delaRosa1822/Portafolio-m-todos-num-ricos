import sympy as sp

def ejecutar_runge_kutta():
    print("--- Solución de EDOs: Método de Runge-Kutta (4to Orden) ---")
    
    # 1. Definición de variables simbólicas
    x, y = sp.symbols('x y')
    
    # 2. Entrada dinámica de la ecuación diferencial dy/dx = f(x, y)
    func_input = input("Introduce la ecuación f(x, y) (ejemplo: x + y): ")
    f = sp.sympify(func_input)
    f_num = sp.lambdify((x, y), f)  # Función evaluable estricta con dos parámetros
    
    # 3. Entrada de condiciones iniciales y parámetros
    x0 = float(input("Introduce el valor inicial de x (x0): "))
    y0 = float(input("Introduce el valor inicial de y (y0): "))
    h = float(input("Introduce el tamaño de paso (h): "))
    x_final = float(input("Introduce el valor final de x a evaluar: "))
    
    # 4. Validación para evitar ciclos infinitos
    if h <= 0 or x_final <= x0:
        print("\n[Error]: El paso 'h' debe ser positivo y 'x_final' debe ser mayor que 'x0'.")
        return
        
    pasos = int(round((x_final - x0) / h))
    
    xi = x0
    yi = y0
    
    print("\n--- Iniciando iteraciones ---")
    print("Punto inicial: x = {0:.4f}, y = {1:.6f}".format(xi, yi))
    
    # 5. Ciclo iterativo del método de Runge-Kutta
    for i in range(1, pasos + 1):
        # Cálculo de las 4 pendientes
        k1 = f_num(xi, yi)
        k2 = f_num(xi + h/2, yi + (h/2)*k1)
        k3 = f_num(xi + h/2, yi + (h/2)*k2)
        k4 = f_num(xi + h, yi + h*k3)
        
        # Aplicar la fórmula del promedio ponderado para y
        yi = yi + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        xi = xi + h
        
        # Imprimir resultados del paso actual
        print("Iteración {0}: x = {1:.4f}, y = {2:.6f}".format(i, xi, yi))
        print("   (Detalle de pendientes -> k1={0:.4f}, k2={1:.4f}, k3={2:.4f}, k4={3:.4f})".format(k1, k2, k3, k4))
        
    # 6. Resultado final
    print("\n--- Resultado Final ---")
    print("El valor estimado de y en x = {0} es: {1:.6f}".format(x_final, yi))

if __name__ == "__main__":
    ejecutar_runge_kutta()
