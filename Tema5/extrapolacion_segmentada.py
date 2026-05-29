import numpy as np

def extrapolacion_segmentada(x_data, y_data, x):
    """
    Extrapola un valor extendiendo linealmente el primer o último segmento de los datos.
    """
    x_data = np.array(x_data, dtype=float)
    y_data = np.array(y_data, dtype=float)
    
    if x_data[0] <= x <= x_data[-1]:
        print("Nota: El punto está dentro de los datos. Debería usar interpolación segmentada.")
        
    if x < x_data[0]:
        # Extrapolamos por la izquierda usando el primer tramo [0, 1]
        x0, x1 = x_data[0], x_data[1]
        y0, y1 = y_data[0], y_data[1]
    else:
        # Extrapolamos por la derecha usando el último tramo [-2, -1]
        x0, x1 = x_data[-2], x_data[-1]
        y0, y1 = y_data[-2], y_data[-1]
        
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

# Ejemplo de uso:
if __name__ == "__main__":
    x_pts = [0, 2, 5, 8]
    y_pts = [1, 4, 2, 9]
    # Proyectamos más allá del último límite (x = 10)
    print(f"Y extrapolado segmentado en x=10: {extrapolacion_segmentada(x_pts, y_pts, 10)}")
