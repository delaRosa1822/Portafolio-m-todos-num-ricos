import numpy as np

def es_diagonalmente_dominante(A):
    # Verifica si la matriz garantiza la convergencia
    n = len(A)
    for i in range(n):
        suma_fila = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= suma_fila:
            return False
    return True

def ejecutar_jacobi():
    print("--- Método Iterativo de Jacobi ---")
    
    # 1. Ingreso de dimensiones
    try:
        n = int(input("Ingresa el número de incógnitas del sistema: "))
    except ValueError:
        print("Entrada no válida.")
        return

    A = np.zeros((n, n))
    B = np.zeros(n)
    
    # 2. Captura de datos
    print("\nIngresa los coeficientes fila por fila (asegúrate de que la diagonal sea la dominante).")
    for i in range(n):
        entrada = input(f"Fila {i+1} (separa los {n} coeficientes y el resultado con espacios): ")
        valores = entrada.split()
        for j in range(n):
            A[i][j] = float(valores[j])
        B[i] = float(valores[n])

    # Validar convergencia
    if not es_diagonalmente_dominante(A):
        print("\n[Advertencia]: La matriz NO es diagonalmente dominante.")
        print("El método podría no converger.")
        continuar = input("¿Deseas continuar de todos modos? (s/n): ")
        if continuar.lower() != 's':
            return

    # 3. Parámetros iterativos
    tol = float(input("\nIntroduce la tolerancia de error (ejemplo: 0.001): "))
    max_iter = 100
    
    # Vectores de solución
    X = np.zeros(n)          # Valores de la iteración anterior (k)
    X_nuevo = np.zeros(n)    # Valores temporales de la iteración actual (k+1)
    
    print("\n--- Iniciando iteraciones ---")
    for k in range(max_iter):
        
        # Calcular los nuevos valores de X basados SOLO en los valores anteriores
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i][j] * X[j] # Usa los valores de X de la iteración pasada
            
            # Guardar en el arreglo temporal
            X_nuevo[i] = (B[i] - suma) / A[i][i]
            
        # Calcular el error máximo entre la iteración actual y la anterior
        error = np.max(np.abs(X_nuevo - X))
        
        print(f"Iteración {k+1}: X = {np.round(X_nuevo, 4)} | Error = {error:.6f}")
        
        # Actualizar el arreglo principal SIMULTÁNEAMENTE
        X = X_nuevo.copy()
        
        # Condición de parada
        if error < tol:
            print(f"\n¡Convergencia alcanzada en la iteración {k+1}!")
            print("--- Solución Final ---")
            for i in range(n):
                print(f"Incógnita x_{i} = {X[i]:.6f}")
            return

    print("\nSe alcanzó el límite de iteraciones sin lograr la tolerancia requerida.")

if __name__ == "__main__":
    ejecutar_jacobi()
