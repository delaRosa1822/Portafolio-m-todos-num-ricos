import ctypes

# Definimos el límite máximo de un entero de 32 bits (equivalente a Integer.MAX_VALUE)
maximo = 2147483647

# Realizamos la suma
suma = maximo + 1

# Simulamos el desbordamiento forzando el tipo a int de 32 bits
resultado = ctypes.c_int32(suma).value

print(f"Valor Max: {maximo}")
print(f"Valor Maximo + 1: {resultado}")
