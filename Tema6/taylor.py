import numpy as np

def taylor_orden_2(f, df, x0, y0, xf, h):
    """
    Resuelve la EDO y' = f(x, y) usando el método de Taylor de 2do Orden.
    df es la derivada total de f respecto a x: y'' = d/dx[f(x, y)] = df_dx + df_dy * f
    """
    x_val = np.arange(x0, xf + h, h)
    y_val = np.zeros(len(x_val))
    y_val[0] = y0
    
    for i in range(len(x_val) - 1):
        x = x_val[i]
        y = y_val[i]
        
        # Términos de la serie de Taylor: y_next = y + h*y' + (h^2/2)*y''
        y_primera = f(x, y)
        y_segunda = df(x, y)
        
        y_val[i+1] = y + h * y_primera + (h**2 / 2) * y_segunda
        
    return x_val, y_val

# Ejemplo de uso:
if __name__ == "__main__":
    # EDO: y' = x + y  -> f(x, y) = x + y
    # Derivada total: y'' = d/dx(x + y) = 1 + y' = 1 + x + y
    f = lambda x, y: x + y
    df = lambda x, y: 1 + x + y
    
    x0, y0 = 0, 1
    xf = 2
    h = 0.5
    
    x, y = taylor_orden_2(f, df, x0, y0, xf, h)
    print("Método de Taylor (2do Orden):")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.2f}, y = {yi:.4f}")
