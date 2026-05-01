import ctypes

# Un número que supera el límite del 'int' tradicional de 32 bits
numero_grande = 7000000000

# Forzamos la conversión a 'int' de 32 bits (Conversión Estrecha)
# Esto simula exactamente el comportamiento de (int) numeroGrande en Java
numero_cortado = ctypes.c_int32(numero_grande).value

print(f"Valor original: {numero_grande}")
print(f"Valor tras el corte: {numero_cortado}")
