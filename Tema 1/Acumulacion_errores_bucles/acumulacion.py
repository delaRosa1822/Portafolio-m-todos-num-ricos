# Inicializamos la variable en 0
saldo = 0.0

# Bucle que se ejecuta 1000 veces
for i in range(1000):
    saldo += 0.01

# Mostramos los resultados en consola
print("Saldo esperado: 10.00")
print(f"Saldo real: {saldo}")
