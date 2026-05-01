# Método de Newton-Raphson
# Extraído de la estructura del Excel: requiere f(x), derivada f'(x), valor inicial y tolerancia.

def f(x):
    # Reemplaza con tu función. Ejemplo: f(x) = x**2 - 3
    return x**2 - 3

def df(x):
    # Derivada de f(x). Ejemplo: f'(x) = 2*x
    return 2*x

def newton_raphson(x0, tol=1e-5, max_iter=50):
    print(f"{'Iteración':<10} | {'xi':<15} | {'f(xi)':<15} | {'f\'(xi)':<15} | {'xi+1':<15} | {'Error':<15}")
    print("-" * 95)
    
    xi = x0
    for i in range(1, max_iter + 1):
        f_xi = f(xi)
        df_xi = df(xi)
        
        if df_xi == 0:
            print("Error: La derivada es cero.")
            break
            
        xi_next = xi - (f_xi / df_xi)
        error = abs(xi_next - xi)
        
        print(f"{i:<10} | {xi:<15.6f} | {f_xi:<15.6f} | {df_xi:<15.6f} | {xi_next:<15.6f} | {error:<15.6f}")
        
        if error < tol:
            print(f"\n--> Raíz aproximada encontrada: {xi_next:.6f}")
            return xi_next
            
        xi = xi_next
        
    print("\n--> Límite de iteraciones alcanzado.")
    return xi

if __name__ == '__main__':
    print("EJECUTANDO MÉTODO DE NEWTON-RAPHSON")
    newton_raphson(x0=1.0)
