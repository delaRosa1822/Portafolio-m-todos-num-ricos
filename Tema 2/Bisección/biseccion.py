import sympy as sp

def ejecutar_biseccion():
    print("--- Calculadora Universal de Bisección ---")
    
    # 1. Entrada de la función matemática
    x = sp.symbols('x')
    func_input = input("Introduce la función f(x) (ejemplo: x**3 - x - 2): ")
    f = sp.sympify(func_input)
    f_num = sp.lambdify(x, f)  # Convertir a función evaluable
    
    # 2. Entrada de parámetros del intervalo
    a = float(input("Introduce el límite inferior (a): "))
    b = float(input("Introduce el límite superior (b): "))
    tol = float(input("Introduce la tolerancia (ejemplo: 0.0001): "))
    max_iter = 100
    
    # Validación: Verificar si hay cambio de signo
    fa = f_num(a)
    fb = f_num(b)
    
    if fa * fb >= 0:
        print("\nError: La función no cambia de signo en el intervalo [a, b].")
        print("Asegúrate de que la raíz esté atrapada entre 'a' y 'b'.")
        return

    xr_old = a  # Variable temporal para calcular el error
    
    for i in range(max_iter):
        # Fórmula de bisección
        xr = (a + b) / 2
        fxr = f_num(xr)
        
        print(f"Iteración {i+1}: a={a:.6f}, b={b:.6f}, xr={xr:.6f}, f(xr)={fxr:.6f}")
        
        # Condición de parada por tolerancia o si encontramos la raíz exacta
        if abs(xr - xr_old) < tol or fxr == 0:
            print(f"\n¡Éxito! La raíz aproximada es: {xr:.6f}")
            return
            
        xr_old = xr
        
        # Reemplazar los límites según el cambio de signo
        if fa * fxr < 0:
            b = xr     # La raíz está en la primera mitad
        else:
            a = xr     # La raíz está en la segunda mitad
            fa = f_num(a)  # Actualizar f(a) porque 'a' acaba de cambiar

    print("Se alcanzó el límite de iteraciones sin llegar a la tolerancia deseada.")

if __name__ == "__main__":
    ejecutar_biseccion()
