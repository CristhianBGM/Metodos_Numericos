import numpy as np

def gauss_seidel(A, b, iter_max=100, tol=1e-6):
    n = len(b)
    x = np.zeros(n)
    
    for k in range(iter_max):
        x_old = np.copy(x)
        for i in range(n):
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma -= A[i, j] * x[j]
            x[i] = suma / A[i, i]
            
        if np.max(np.abs(x - x_old)) < tol:
            return x
    return x

# Ejemplo 1 del PDF adaptado
A = np.array([[12.350, 1.036, 5.401], 
              [-7.947, 18.398, -0.896], 
              [-5.117, 9.470, 26.752]])
b = np.array([-6.152, -9.457, -8.622])
solucion = gauss_seidel(A, b)
print("Solución Gauss-Seidel:", solucion)