import numpy as np

def runge_kutta_4(f, x0, y0, xf, h):
    """
    Resuelve la EDO y' = f(x, y) con condición inicial y(x0) = y0
    usando el método de Runge-Kutta de 4to Orden (RK4).
    """
    x_val = np.arange(x0, xf + h, h)
    y_val = np.zeros(len(x_val))
    y_val[0] = y0
    
    for i in range(len(x_val) - 1):
        x = x_val[i]
        y = y_val[i]
        
        k1 = f(x, y)
        k2 = f(x + h/2, y + (h/2)*k1)
        k3 = f(x + h/2, y + (h/2)*k2)
        k4 = f(x + h, y + h*k3)
        
        y_val[i+1] = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        
    return x_val, y_val

# Ejemplo de uso:
if __name__ == "__main__":
    # EDO: y' = x + y, con y(0) = 1
    f = lambda x, y: x + y
    x0, y0 = 0, 1
    xf = 2
    h = 0.5
    
    x, y = runge_kutta_4(f, x0, y0, xf, h)
    print("Método de Runge-Kutta 4to Orden:")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.2f}, y = {yi:.4f}")
