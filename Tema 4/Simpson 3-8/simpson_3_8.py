import sympy as sp

def ejecutar_simpson_38():
    print("--- Integración Numérica: Regla de Simpson 3/8 ---")
    
    # 1. Entrada dinámica de la función
    x = sp.symbols('x')
    func_input = input("Introduce la función f(x) (ejemplo: x**3): ")
    f = sp.sympify(func_input)
    f_num = sp.lambdify(x, f)  # Convertir a función evaluable
    
    # 2. Entradas de límites e intervalos
    a = float(input("Introduce el límite inferior (a): "))
    b = float(input("Introduce el límite superior (b): "))
    n = int(input("Introduce el número de intervalos (n). DEBE ser múltiplo de 3: "))
    
    # 3. Validación de la regla 3/8
    if n % 3 != 0:
        print("\n[Error Crítico]: El número de intervalos 'n' debe ser un múltiplo de 3 (ej. 3, 6, 9, 12...).")
        print("El método no se puede aplicar. Inténtalo de nuevo.")
        return
        
    # 4. Cálculo de h
    h = (b - a) / n
    print(f"\nAncho de cada subintervalo (h) = {h:.6f}")
    
    # 5. Aplicación de la fórmula compuesta
    # Sumamos primero los extremos f(x_0) y f(x_n)
    suma_total = f_num(a) + f_num(b)
    
    # Iteramos sobre los puntos internos
    for i in range(1, n):
        xi = a + i * h
        
        # Si el índice es múltiplo de 3, se multiplica por 2
        if i % 3 == 0:
            suma_total += 2 * f_num(xi)
        # Si no es múltiplo de 3, se multiplica por 3
        else:
            suma_total += 3 * f_num(xi)
            
    # Multiplicar por el factor principal 3h/8
    integral_aproximada = (3 * h / 8) * suma_total
    
    # 6. Mostrar resultado
    print(f"\n--- Resultado Final ---")
    print(f"El área aproximada bajo la curva (Integral) es: {integral_aproximada:.6f}")

if __name__ == "__main__":
    ejecutar_simpson_38()
