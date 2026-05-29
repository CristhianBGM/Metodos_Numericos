import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Resuelve el sistema Ax = b usando el método iterativo de Gauss-Seidel.
    """
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
        
    x = x0.copy()
    
    for k in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            s1 = sum(A[i, j] * x[j] for j in range(i))
            s2 = sum(A[i, j] * x_old[j] for j in range(i+1, n))
            x[i] = (b[i] - s1 - s2) / A[i, i]
            
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x
            
    return x

# Ejemplo de uso:
if __name__ == "__main__":
    A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]])
    b = np.array([6, 25, -11])
    solucion = gauss_seidel(A, b)
    print(f"Solución por Gauss-Seidel: {solucion}")
