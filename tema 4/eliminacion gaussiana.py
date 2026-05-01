import numpy as np

def eliminacion_gaussiana(A, B):
    n = len(B)
    Ab = np.hstack([A.astype(float), B.reshape(-1, 1).astype(float)])
    
    for i in range(n):
        # Pivoteo parcial
        if abs(Ab[i, i]) < 1e-10:
            for k in range(i + 1, n):
                if abs(Ab[k, i]) > 1e-10:
                    Ab[[i, k]] = Ab[[k, i]]
                    break
                    
        # Eliminación
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j] = Ab[j] - factor * Ab[i]
            
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, n]
        for j in range(i + 1, n):
            x[i] -= Ab[i, j] * x[j]
        x[i] = x[i] / Ab[i, i]
        
    return x

# Ejemplo 1 del PDF
A = np.array([[2, 1], [4, -6]])
B = np.array([5, -2])
solucion = eliminacion_gaussiana(A, B)
print("Solución Eliminación Gaussiana:", solucion)