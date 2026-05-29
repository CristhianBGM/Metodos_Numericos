def extrapolacion_cuadratica(x0, y0, x1, y1, x2, y2, x):
    """
    Extrapola un valor 'y' fuera del rango de los 3 puntos usando la parábola que los une.
    """
    L0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    L1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    L2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    
    y = y0 * L0 + y1 * L1 + y2 * L2
    return y

# Ejemplo de uso:
if __name__ == "__main__":
    # Mismos puntos (0,0), (1,1), (2,4). Extrapolamos a x = 3
    print(f"Y extrapolado (cuadrático): {extrapolacion_cuadratica(0, 0, 1, 1, 2, 4, 3)}")
