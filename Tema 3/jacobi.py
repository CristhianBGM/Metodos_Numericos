import numpy as np

def jacobi(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Resuelve el sistema Ax = b usando el método iterativo de Jacobi.
    """
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    
    x = x0.copy()
    x_new = np.zeros(n)
    
    for k in range(max_iter):
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(n) if i != j)
            x_new[i] = (b[i] - s) / A[i, i]
            
        # Comprobar convergencia usando la norma infinito
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new.copy()
        
    return x

# Ejemplo de uso:
if __name__ == "__main__":
    # Matriz diagonalmente dominante para asegurar convergencia
    A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]])
    b = np.array([6, 25, -11])
    solucion = jacobi(A, b)
    print(f"Solución por Jacobi: {solucion}")
