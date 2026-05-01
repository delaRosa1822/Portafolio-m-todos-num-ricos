import sympy as sp

def ejecutar_newton():
    print("--- Calculadora Universal de Newton-Raphson ---")
    
    # 1. Entrada de la función (acepta cualquier función)
    x = sp.symbols('x')
    func_input = input("Introduce la función f(x) (ejemplo: x**3 - x - 2): ")
    f = sp.sympify(func_input)
    
    # 2. Cálculo automático de la derivada
    df = sp.diff(f, x)
    
    # 3. Entradas de parámetros
    x0 = float(input("Introduce el valor inicial (x0): "))
    tol = float(input("Introduce la tolerancia (ejemplo: 0.0001): "))
    max_iter = 50
    
    # Convertir a funciones evaluables
    f_num = sp.lambdify(x, f)
    df_num = sp.lambdify(x, df)
    
    xn = x0
    for i in range(max_iter):
        fxn = f_num(xn)
        dfxn = df_num(xn)
        
        if dfxn == 0:
            print("Error: Derivada es cero. No hay solución.")
            return

        # Aplicación de la fórmula
        x_next = xn - (fxn / dfxn)
        
        print(f"Iteración {i+1}: x = {x_next:.6f}")
        
        if abs(x_next - xn) < tol:
            print(f"\n¡Éxito! La raíz es: {x_next:.6f}")
            return
        
        xn = x_next

    print("Se alcanzó el límite de iteraciones.")

if __name__ == "__main__":
    ejecutar_newton()
