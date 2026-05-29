def interpolacion_cuadratica(x0, y0, x1, y1, x2, y2, x):
    """
    Interpola un valor 'y' para un 'x' usando un polinomio cuadrático a través de 3 puntos.
    """
    # Polinomios de Lagrange de grado 2
    L0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    L1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    L2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    
    y = y0 * L0 + y1 * L1 + y2 * L2
    return y

# Ejemplo de uso:
if __name__ == "__main__":
    # Puntos: (0,0), (1,1), (2,4) -> Curva exacta de y = x^2
    print(f"Y interpolado (cuadrático): {interpolacion_cuadratica(0, 0, 1, 1, 2, 4, 1.5)}")
