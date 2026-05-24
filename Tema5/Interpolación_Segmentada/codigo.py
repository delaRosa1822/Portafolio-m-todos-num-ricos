# 1. Definimos nuestros arreglos de puntos conocidos
x_datos = [0.0, 2.0, 4.0, 6.0]
y_datos = [1.0, 5.0, 3.0, 9.0]

# 2. Definimos el valor de 'x' que queremos interpolar
x_objetivo = 3.0
y_estimado = None

# 3. Buscamos el segmento correcto
for i in range(len(x_datos) - 1):
    if x_datos[i] <= x_objetivo <= x_datos[i+1]:
        # 4. Extraemos los puntos del segmento encontrado
        x0, y0 = x_datos[i], y_datos[i]
        x1, y1 = x_datos[i+1], y_datos[i+1]
        
        # 5. Aplicamos la fórmula lineal para este segmento
        pendiente = (y1 - y0) / (x1 - x0)
        y_estimado = y0 + pendiente * (x_objetivo - x0)
        break # Salimos del bucle una vez que encontramos el resultado

# 6. Mostramos los resultados en consola
print("--- Interpolación Segmentada ---")
if y_estimado is not None:
    print(f"Para x = {x_objetivo}, el valor estimado de y es: {y_estimado}")
else:
    print("El valor está fuera del rango de datos conocidos.")
