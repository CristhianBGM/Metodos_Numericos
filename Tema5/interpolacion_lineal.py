def interpolacion_lineal(x0, y0, x1, y1, x):
    """
    Calcula el valor interpolado de 'y' para un 'x' dado entre x0 y x1.
    """
    if not (x0 <= x <= x1 or x1 <= x <= x0):
        print("Nota: El punto está fuera del intervalo (Conceptualmente es extrapolación).")
        
    y = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)
    return y

# Ejemplo de uso:
if __name__ == "__main__":
    # Datos: (1, 2) y (3, 6). Buscamos el valor en x = 2
    print(f"Y interpolado: {interpolacion_lineal(1, 2, 3, 6, 2)}")
