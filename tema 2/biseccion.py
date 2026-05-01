# Método de Bisección
# Extraído de la estructura del Excel: requiere f(x), un intervalo [a, b] donde f(a)*f(b)<0 y tolerancia.

def f(x):
    # Reemplaza con tu función. Ejemplo: f(x) = x**2 - 3
    return x**2 - 3

def biseccion(a, b, tol=1e-5, max_iter=50):
    if f(a) * f(b) >= 0:
        print("El intervalo es inválido. f(a) y f(b) deben tener signos opuestos.")
        return None
        
    print(f"{'Iter':<5} | {'a':<10} | {'b':<10} | {'c':<10} | {'f(a)':<10} | {'f(c)':<10} | {'Error':<10}")
    print("-" * 80)
    
    c_prev = a
    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        f_a = f(a)
        f_c = f(c)
        error = abs(c - c_prev)
        
        print(f"{i:<5} | {a:<10.5f} | {b:<10.5f} | {c:<10.5f} | {f_a:<10.5f} | {f_c:<10.5f} | {error:<10.5f}")
        
        if abs(f_c) < tol or (i > 1 and error < tol):
            print(f"\n--> Raíz aproximada encontrada: {c:.6f}")
            return c
            
        if f_a * f_c < 0:
            b = c
        else:
            a = c
            
        c_prev = c
        
    print("\n--> Límite de iteraciones alcanzado.")
    return c

if __name__ == '__main__':
    print("EJECUTANDO MÉTODO DE BISECCIÓN")
    biseccion(a=1.0, b=2.0)
