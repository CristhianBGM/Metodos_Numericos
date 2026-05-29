def extrapolacion_lineal(x0, y0, x1, y1, x):
    """
    Proyecta el valor de 'y' para un 'x' que se encuentra fuera del intervalo [x0, x1].
    """
    if (x0 <= x <= x1 or x1 <= x <= x0):
        print("Nota: El punto está dentro del intervalo (Conceptualmente es interpolación).")
        
    y = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)
    return y

# Ejemplo de uso:
if __name__ == "__main__":
    # Datos: (1, 2) y (3, 6). Proyectamos hacia el futuro en x = 5
    print(f"Y extrapolado: {extrapolacion_lineal(1, 2, 3, 6, 5)}")
