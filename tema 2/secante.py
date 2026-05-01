# Método de la Secante
# Extraído de la estructura del Excel: requiere f(x), dos valores iniciales xi y xi-1, y tolerancia.

import math

def f(x):
    # Ejemplo basado en el archivo: f(x) = e^(-x) - x
    return math.exp(-x) - x 

def secante(x0, x1, tol=1e-5, max_iter=50):
    print(f"{'Iter':<5} | {'xi-1':<12} | {'xi':<12} | {'f(xi-1)':<12} | {'f(xi)':<12} | {'xi+1':<12} | {'Error':<12}")
    print("-" * 90)
    
    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 - f_x0 == 0:
            print("Error: División por cero.")
            break
            
        xi_next = x1 - f_x1 * (x0 - x1) / (f_x0 - f_x1)
        error = abs(xi_next - x1)
        
        print(f"{i:<5} | {x0:<12.6f} | {x1:<12.6f} | {f_x0:<12.6f} | {f_x1:<12.6f} | {xi_next:<12.6f} | {error:<12.6f}")
        
        if error < tol:
            print(f"\n--> Raíz aproximada encontrada: {xi_next:.6f}")
            return xi_next
            
        x0 = x1
        x1 = xi_next
        
    print("\n--> Límite de iteraciones alcanzado.")
    return x1

if __name__ == '__main__':
    print("EJECUTANDO MÉTODO DE LA SECANTE")
    secante(x0=0.0, x1=1.0)
