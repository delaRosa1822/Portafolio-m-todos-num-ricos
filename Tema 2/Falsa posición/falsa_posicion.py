import sympy as sp

def ejecutar_falsa_posicion():
    print("--- Calculadora Universal de Falsa Posición ---")
    
    # 1. Entrada dinámica de la función
    x = sp.symbols('x')
    func_input = input("Introduce la función f(x) (ejemplo: x**3 - x - 2): ")
    f = sp.sympify(func_input)
    f_num = sp.lambdify(x, f)  # Convierte la función de texto a una evaluable
    
    # 2. Entradas del intervalo y parámetros
    a = float(input("Introduce el límite inferior (a): "))
    b = float(input("Introduce el límite superior (b): "))
    tol = float(input("Introduce la tolerancia (ejemplo: 0.0001): "))
    max_iter = 50
    
    # Validación inicial crítica: Comprobar que hay una raíz en el intervalo
    fa = f_num(a)
    fb = f_num(b)
    
    if fa * fb >= 0:
        print("\nError: La función no cambia de signo en el intervalo [a, b].")
        print("El método de Falsa Posición requiere que f(a) y f(b) tengan signos opuestos.")
        return

    xr_old = a  # Valor inicial temporal para poder calcular el error en la primera vuelta
    
    for i in range(max_iter):
        fa = f_num(a)
        fb = f_num(b)
        
        # Aplicación de la fórmula
        xr = b - (fb * (a - b)) / (fa - fb)
        fxr = f_num(xr)
        
        print(f"Iteración {i+1}: a={a:.4f}, b={b:.4f}, xr={xr:.6f}, f(xr)={fxr:.6f}")
        
        # Condición de parada por tolerancia
        if abs(xr - xr_old) < tol:
            print(f"\n¡Éxito! La raíz es: {xr:.6f}")
            return
        
        xr_old = xr
        
        # Actualización de los límites del intervalo
        if fa * fxr < 0:
            b = xr  # La raíz está del lado izquierdo, ajustamos límite superior
        elif fa * fxr > 0:
            a = xr  # La raíz está del lado derecho, ajustamos límite inferior
        else:
            print(f"\n¡Éxito! La raíz exacta es: {xr:.6f}")
            return

    print("Se alcanzó el límite de iteraciones.")

if __name__ == "__main__":
    ejecutar_falsa_posicion()
