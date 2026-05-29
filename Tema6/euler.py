import numpy as np

def euler(f, x0, y0, xf, h):
    """
    Resuelve la EDO y' = f(x, y) con condición inicial y(x0) = y0
    desde x0 hasta xf con un tamaño de paso h usando el método de Euler.
    """
    x_val = np.arange(x0, xf + h, h)
    y_val = np.zeros(len(x_val))
    y_val[0] = y0
    
    for i in range(len(x_val) - 1):
        y_val[i+1] = y_val[i] + h * f(x_val[i], y_val[i])
        
    return x_val, y_val

# Ejemplo de uso:
if __name__ == "__main__":
    # EDO: y' = x + y, con y(0) = 1
    f = lambda x, y: x + y
    x0, y0 = 0, 1
    xf = 2
    h = 0.5
    
    x, y = euler(f, x0, y0, xf, h)
    print("Método de Euler:")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.2f}, y = {yi:.4f}")
