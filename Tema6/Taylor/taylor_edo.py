import sympy as sp
import math

def ejecutar_taylor_edo():
    print("--- Solución de EDOs: Método de Series de Taylor ---")
    
    # 1. Definición de variables simbólicas
    x, y = sp.symbols('x y')
    
    # 2. Entrada de la ecuación y parámetros
    func_input = input("Introduce la ecuación dy/dx = f(x, y) (ejemplo: x - y): ")
    f = sp.sympify(func_input)
    
    orden = int(input("Introduce el orden del polinomio de Taylor (k) (ejemplo: 2, 3 o 4): "))
    x0 = float(input("Introduce el valor inicial de x (x0): "))
    y0 = float(input("Introduce el valor inicial de y (y0): "))
    h = float(input("Introduce el tamaño de paso (h): "))
    x_final = float(input("Introduce el valor final de x a evaluar: "))
    
    if h <= 0 or x_final <= x0 or orden < 1:
        print("\n[Error]: Parámetros de intervalo u orden inválidos.")
        return

    # 3. Cálculo analítico de las derivadas sucesivas
    # derivadas[1] será y', derivadas[2] será y'', etc.
    derivadas = [y, f] # y^(0) = y, y^(1) = f
    
    print("\nCalculando derivadas analíticas internamente...")
    for i in range(2, orden + 1):
        expr_anterior = derivadas[-1]
        # Regla de la cadena: d(expr)/dx = parcial(expr)/dx + parcial(expr)/dy * (dy/dx)
        der_parcial_x = sp.diff(expr_anterior, x)
        der_parcial_y = sp.diff(expr_anterior, y)
        der_total = der_parcial_x + der_parcial_y * f
        derivadas.append(der_total)
        
    # Convertir todas las expresiones a funciones evaluables para mayor rapidez
    funcs_eval = []
    for d in derivadas:
        funcs_eval.append(sp.lambdify((x, y), d))
        
    pasos = int(round((x_final - x0) / h))
    xi = x0
    yi = y0
    
    print("\n--- Iniciando iteraciones ---")
    print("Punto inicial: x = {0:.4f}, y = {1:.6f}".format(xi, yi))
    
    # 4. Ciclo iterativo evaluando la Serie de Taylor
    for i in range(1, pasos + 1):
        yi_nuevo = yi
        
        # Sumatoria de la serie de Taylor hasta el orden 'k'
        for j in range(1, orden + 1):
            valor_derivada = funcs_eval[j](xi, yi)
            termino_taylor = (math.pow(h, j) / math.factorial(j)) * valor_derivada
            yi_nuevo += termino_taylor
            
        yi = yi_nuevo
        xi = xi + h
        
        print("Iteración {0}: x = {1:.4f}, y = {2:.6f}".format(i, xi, yi))
        
    # 5. Resultado final
    print("\n--- Resultado Final ---")
    print("El valor estimado de y en x = {0} es: {1:.6f}".format(x_final, yi))

if __name__ == "__main__":
    ejecutar_taylor_edo()
