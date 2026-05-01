import numpy as np

def es_diagonalmente_dominante(A):
    # Verifica si la matriz garantiza la convergencia
    n = len(A)
    for i in range(n):
        # Suma de los valores absolutos de la fila (excluyendo la diagonal)
        suma_fila = sum(abs(A[i][j]) for j in range(n) if j != i)
        # Si el elemento en la diagonal no es mayor estrictamente, no es dominante
        if abs(A[i][i]) <= suma_fila:
            return False
    return True

def ejecutar_gauss_seidel():
    print("--- Método Iterativo de Gauss-Seidel ---")
    
    # 1. Ingreso de dimensiones
    try:
        n = int(input("Ingresa el número de incógnitas del sistema: "))
    except ValueError:
        print("Entrada no válida.")
        return

    A = np.zeros((n, n))
    B = np.zeros(n)
    
    # 2. Captura de datos
    print("\nIngresa los coeficientes fila por fila (asegúrate de que la diagonal sea la más grande).")
    for i in range(n):
        entrada = input(f"Fila {i+1} (separa los {n} coeficientes y el resultado con espacios): ")
        valores = entrada.split()
        for j in range(n):
            A[i][j] = float(valores[j])
        B[i] = float(valores[n])

    # Validar convergencia
    if not es_diagonalmente_dominante(A):
        print("\n[Advertencia]: La matriz NO es diagonalmente dominante.")
        print("El método podría no converger. Asegúrate de ordenar las ecuaciones.")
        continuar = input("¿Deseas continuar de todos modos? (s/n): ")
        if continuar.lower() != 's':
            return

    # 3. Parámetros iterativos
    tol = float(input("\nIntroduce la tolerancia de error (ejemplo: 0.001): "))
    max_iter = 100
    
    # Vector de soluciones iniciales (empezamos en ceros)
    X = np.zeros(n)
    
    print("\n--- Iniciando iteraciones ---")
    for k in range(max_iter):
        X_anterior = X.copy()
        
        # Calcular los nuevos valores de X
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i][j] * X[j] # Usa los valores de X actualizados en tiempo real
            
            # Aplicar la fórmula despejada
            X[i] = (B[i] - suma) / A[i][i]
            
        # Calcular el error máximo entre la iteración actual y la anterior
        error = np.max(np.abs(X - X_anterior))
        
        print(f"Iteración {k+1}: X = {np.round(X, 4)} | Error = {error:.6f}")
        
        # Condición de parada
        if error < tol:
            print(f"\n¡Convergencia alcanzada en la iteración {k+1}!")
            print("--- Solución Final ---")
            for i in range(n):
                print(f"Incógnita x_{i} = {X[i]:.6f}")
            return

    print("\nSe alcanzó el límite de iteraciones sin lograr la tolerancia requerida.")

if __name__ == "__main__":
    ejecutar_gauss_seidel()
