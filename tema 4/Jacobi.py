import numpy as np

def jacobi(A, b, max_iter=100, tol=1e-10):
    n = len(A)
    x = np.ones(n) # Valor inicial
    x_old = np.ones(n)
    
    for k in range(1, max_iter + 1):
        for i in range(n):
            suma = 0.0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * x_old[j]
            x[i] = (b[i] - suma) / A[i, i]
            
        error = np.max(np.abs(x - x_old))
        if error < tol:
            return x, k
        x_old = np.copy(x)
        
    return x, max_iter

# Ejemplo 1 del PDF
A = np.array([[5.0, 2.0, -3.0], 
              [2.0, 10.0, -8.0], 
              [3.0, 8.0, 13.0]])
b = np.array([1.0, 4.0, 7.0])
solucion, iteraciones = jacobi(A, b)
print(f"Solución Jacobi (Iteraciones: {iteraciones}):", solucion)