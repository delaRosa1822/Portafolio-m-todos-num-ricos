import numpy as np
import sys

def ejecutar_gauss_jordan():
    print("--- Calculadora de Sistemas por Gauss-Jordan ---")
    
    # 1. Ingreso de dimensiones
    try:
        n = int(input("Ingresa el número de incógnitas del sistema: "))
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
        return

    # Crear la matriz aumentada inicial llena de ceros
    matriz_aumentada = np.zeros((n, n + 1))
    
    # 2. Captura de datos
    print("\nIngresa los coeficientes fila por fila.")
    for i in range(n):
        fila_valida = False
        while not fila_valida:
            entrada = input(f"Fila {i+1} (separa los {n} coeficientes y el resultado con espacios): ")
            valores = entrada.split()
            
            if len(valores) == n + 1:
                for j in range(n + 1):
                    matriz_aumentada[i][j] = float(valores[j])
                fila_valida = True
            else:
                print(f"Error: Se esperaban {n + 1} valores. Inténtalo de nuevo.")

    print("\nMatriz Aumentada Inicial:")
    print(matriz_aumentada)

    # 3. Proceso principal de Gauss-Jordan
    for i in range(n):
        # Pivoteo Parcial: Buscar el máximo en la columna actual
        max_index = np.argmax(abs(matriz_aumentada[i:n, i])) + i
        if matriz_aumentada[max_index, i] == 0:
            print("Error: El sistema no tiene solución única.")
            sys.exit()
            
        # Intercambio de filas si es necesario
        if max_index != i:
            matriz_aumentada[[i, max_index]] = matriz_aumentada[[max_index, i]]
            print(f"\n-> Se intercambió la fila {i+1} con la fila {max_index+1}")

        # Normalizar la fila pivote (hacer el pivote 1)
        pivote = matriz_aumentada[i, i]
        matriz_aumentada[i] = matriz_aumentada[i] / pivote
        
        # Eliminación de elementos arriba y abajo del pivote
        for k in range(n):
            if k != i: # Para todas las filas excepto la del pivote actual
                factor = matriz_aumentada[k, i]
                matriz_aumentada[k] = matriz_aumentada[k] - (factor * matriz_aumentada[i])

    print("\nMatriz Identidad Resultante (Matriz Reducida):")
    print(np.round(matriz_aumentada, decimals=4))

    # 4. Resultados directos
    print("\n--- Solución Directa del Sistema ---")
    for i in range(n):
        print(f"Incógnita x_{i} = {matriz_aumentada[i, n]:.6f}")

if __name__ == "__main__":
    ejecutar_gauss_jordan()
