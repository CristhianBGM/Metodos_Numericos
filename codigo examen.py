# Variables utilizadas
registros = [10.0, 20.0, 30.0]
tiempos = [80.0, 110.0, 200.0]
x_estimar = 25.0

# Fórmulas implementadas (Diferencias Divididas de Newton)
dif_1_0 = (tiempos[1] - tiempos[0]) / (registros[1] - registros[0])
dif_1_1 = (tiempos[2] - tiempos[1]) / (registros[2] - registros[1])
dif_2 = (dif_1_1 - dif_1_0) / (registros[2] - registros[0])

# Construcción del polinomio
tiempo_estimado = tiempos[0] + dif_1_0 * (x_estimar - registros[0]) + dif_2 * (x_estimar - registros[0]) * (x_estimar - registros[1])

# Resultado obtenido
print("--- Validación de Rendimiento SQL ---")
print(f"Registros procesados: {x_estimar} mil")
print(f"Tiempo de respuesta estimado: {tiempo_estimado} ms")