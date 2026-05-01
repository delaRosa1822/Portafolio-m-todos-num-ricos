import numpy as np
import sys

def ejecutar_gauss():
    print("--- Resolución por Eliminación Gaussiana ---")
    
    # 1. Ingreso del tamaño del sistema
    try:
        n = int(input("Ingresa el número de incógnitas del sistema: "))
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
        return

    # Inicializar matriz A (coeficientes) y vector B (términos independientes)
    A = np.zeros((n, n))
    B = np.zeros(n)
    
    # 2. Captura de datos de la matriz aumentada
    print("\nIngresa los coeficientes fila por fila.")
    for i in range(n):
        fila_valida = False
        while not fila_valida:
            entrada = input(f"Fila {i+1} (separa los {n} coeficientes y el resultado con espacios): ")
            valores = entrada.split()
            
            if len(valores) == n + 1:
                for j in range(n):
                    A[i][j] = float(valores[j])
                B[i] = float(valores[n])
                fila_valida = True
            else:
                print(f"Error: Debes ingresar {n + 1} valores. Inténtalo de nuevo.")

    print("\nMatriz Aumentada Inicial:")
    matriz_aumentada = np.column_stack((A, B))
    print(matriz_aumentada)

    # 3. Proceso de Eliminación Gaussiana con Pivoteo Parcial
    for k in range(n - 1):
        # Pivoteo Parcial
        max_index = np.argmax(abs(A[k:n, k])) + k
        if A[max_index, k] == 0:
            print("El sistema no tiene solución única (columna de ceros).")
            sys.exit()
            
        # Intercambiar filas si el mayor no está en el pivote actual
        if max_index != k:
            A[[k, max_index]] = A[[max_index, k]]
            B[[k, max_index]] = B[[max_index, k]]
            print(f"\nSe intercambió la fila {k+1} con la fila {max_index+1} por pivoteo.")

        # Eliminación hacia adelante
        for i in range(k + 1, n):
            if A[i, k] != 0.0:
                factor = A[i, k] / A[k, k]
                A[i, k:n] = A[i, k:n] - factor * A[k, k:n]
                B[i] = B[i] - factor * B[k]

    print("\nMatriz Triangular Superior obtenida:")
    print(np.column_stack((A, B)))

    # 4. Sustitución hacia atrás
    X = np.zeros(n)
    X[n - 1] = B[n - 1] / A[n - 1, n - 1]
    
    for i in range(n - 2, -1, -1):
        suma = np.dot(A[i, i+1:n], X[i+1:n])
        X[i] = (B[i] - suma) / A[i, i]

    # 5. Imprimir resultados
    print("\n--- Solución del Sistema ---")
    for i in range(n):
        # Imprime x_0, x_1, etc.
        print(f"Incógnita x_{i} = {X[i]:.6f}")

if __name__ == "__main__":
    ejecutar_gauss()
