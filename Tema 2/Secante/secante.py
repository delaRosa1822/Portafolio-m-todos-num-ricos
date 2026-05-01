import sympy as sp

def ejecutar_secante():
    print("--- Calculadora Universal de la Secante ---")
    
    # 1. Entrada de la función (acepta cualquier función)
    x = sp.symbols('x')
    func_input = input("Introduce la función f(x) (ejemplo: x**3 - 2*x - 5): ")
    f = sp.sympify(func_input)
    f_num = sp.lambdify(x, f)  # Convierte la expresión a función evaluable
    
    # 2. Entradas de parámetros iniciales
    x0 = float(input("Introduce el primer valor inicial (x0): "))
    x1 = float(input("Introduce el segundo valor inicial (x1): "))
    tol = float(input("Introduce la tolerancia (ejemplo: 0.0001): "))
    max_iter = 50
    
    for i in range(max_iter):
        fx0 = f_num(x0)
        fx1 = f_num(x1)
        
        # Validar división por cero
        if fx1 - fx0 == 0:
            print("\nError: División por cero. La línea secante es horizontal.")
            return

        # Aplicación de la fórmula de la secante
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        
        print(f"Iteración {i+1}: x0={x0:.6f}, x1={x1:.6f}, x2 (nuevo)={x2:.6f}")
        
        # Condición de parada
        if abs(x2 - x1) < tol:
            print(f"\n¡Éxito! La raíz aproximada es: {x2:.6f}")
            return
        
        # Actualizar los puntos para la siguiente iteración
        x0 = x1
        x1 = x2

    print("Se alcanzó el límite de iteraciones sin llegar a la tolerancia.")

if __name__ == "__main__":
    ejecutar_secante()
