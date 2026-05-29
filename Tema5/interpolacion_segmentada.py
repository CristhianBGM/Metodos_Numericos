import numpy as np

def interpolacion_segmentada(x_data, y_data, x):
    """
    Realiza una interpolación lineal por segmentos (trazadores lineales) para un conjunto de datos.
    """
    x_data = np.array(x_data, dtype=float)
    y_data = np.array(y_data, dtype=float)
    
    if x < x_data[0] or x > x_data[-1]:
        raise ValueError("El valor de x está fuera del rango. Use extrapolación segmentada.")
        
    # Encontrar el índice del segmento correspondiente
    idx = np.searchsorted(x_data, x) - 1
    idx = max(0, min(idx, len(x_data) - 2))
    
    x0, x1 = x_data[idx], x_data[idx+1]
    y0, y1 = y_data[idx], y_data[idx+1]
    
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

# Ejemplo de uso:
if __name__ == "__main__":
    x_pts = [0, 2, 5, 8]
    y_pts = [1, 4, 2, 9]
    print(f"Y interpolado segmentado en x=3: {interpolacion_segmentada(x_pts, y_pts, 3)}")
