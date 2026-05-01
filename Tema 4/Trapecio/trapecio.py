import sympy as sp

def ejecutar_trapecio():
    print("--- Integración Numérica: Regla del Trapecio ---")
    
    # 1. Entrada de la función
    x = sp.symbols('x')
    func_input = input("Introduce la función f(x) (ejemplo: x**2): ")
    f = sp.sympify(func_input)
    f_num = sp.lambdify(x, f)  # Convertir la expresión a una función de Python
    
    # 2. Entradas de límites y número de intervalos
    a = float(input("Introduce el límite inferior (a): "))
    b = float(input("Introduce el límite superior (b): "))
    try:
        n = int(input("Introduce el número de intervalos (trapecios, n): "))
    except ValueError:
        print("El número de intervalos debe ser un número entero.")
        return
        
    # 3. Validación de intervalos lógicos
    if n <= 0:
        print("\n[Error]: El número de intervalos 'n' debe ser mayor a 0.")
        return
        
    # 4. Cálculo del paso (h)
    h = (b - a) / n
    print(f"\nAncho de cada subintervalo (h) = {h:.6f}")
    
    # 5. Aplicación de la fórmula
    # Se suman primero las evaluaciones de los límites extremos
    suma_total = f_num(a) + f_num(b)
    
    # Ciclo para sumar los puntos intermedios multiplicados por 2
    for i in range(1, n):
        xi = a + i * h
        suma_total += 2 * f_num(xi)
        
    # Multiplicar por el factor final (h / 2)
    integral_aproximada = (h / 2) * suma_total
    
    # 6. Salida del resultado
    print(f"\n--- Resultado Final ---")
    print(f"El área aproximada bajo la curva (Integral) es: {integral_aproximada:.6f}")

if __name__ == "__main__":
    ejecutar_trapecio()
