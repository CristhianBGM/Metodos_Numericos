import numpy as np

def gauss_jordan(A, B):
    n = len(B)
    Ab = np.hstack([A.astype(float), B.reshape(-1, 1).astype(float)])
    
    for i in range(n):
        # Pivoteo
        if Ab[i, i] == 0:
            idx_max = np.argmax(np.abs(Ab[i:, i])) + i
            Ab[[i, idx_max]] = Ab[[idx_max, i]]
            
        # Normalización
        Ab[i] = Ab[i] / Ab[i, i]
        
        # Eliminación
        for j in range(n):
            if i != j:
                factor = Ab[j, i]
                Ab[j] = Ab[j] - factor * Ab[i]
                
    return Ab[:, -1]

# Ejemplo 1 del PDF
A = np.array([[2, 1], [1, 3]])
B = np.array([5, 10])
solucion = gauss_jordan(A, B)
print("Solución Gauss-Jordan:", solucion)