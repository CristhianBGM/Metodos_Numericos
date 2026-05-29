import numpy as np

def regresion_y_correlacion(x, y):
    """
    Calcula la pendiente (m), la intersección (b) y el coeficiente 
    de correlación (r) para un conjunto de puntos (x, y).
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)
    
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x**2)
    sum_y2 = np.sum(y**2)
    
    # Fórmulas de mínimos cuadrados
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_y - m * sum_x) / n
    
    # Coeficiente de correlación de Pearson
    r = (n * sum_xy - sum_x * sum_y) / np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
    
    return m, b, r

# Ejemplo de uso:
if __name__ == "__main__":
    x_datos = [1, 2, 3, 4, 5]
    y_datos = [2.1, 3.9, 6.2, 8.1, 10.2]
    m, b, r = regresion_y_correlacion(x_datos, y_datos)
    print(f"Ecuación: y = {m:.4f}x + {b:.4f}")
    print(f"Coeficiente de correlación (r): {r:.4f}")
