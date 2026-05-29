import numpy as np

def eliminacion_gaussiana(A, b):
    """
    Resuelve el sistema Ax = b mediante Eliminación Gaussiana con pivoteo parcial.
    """
    n = len(b)
    # Crear la matriz aumentada
    M = np.hstack([A.astype(float), b.astype(float).reshape(-1, 1)])
    
    for i in range(n):
        # Pivoteo parcial para mejorar la estabilidad numérica
        max_row = np.argmax(np.abs(M[i:n, i])) + i
        if M[max_row, i] == 0:
            raise ValueError("El sistema no tiene solución única.")
        M[[i, max_row]] = M[[max_row, i]]
        
        # Eliminación hacia adelante
        for j in range(i+1, n):
            factor = M[j, i] / M[i, i]
            M[j, i:] -= factor * M[i, i:]
            
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
        
    return x

# Ejemplo de uso:
if __name__ == "__main__":
    A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
    b = np.array([1, -2, 0])
    solucion = eliminacion_gaussiana(A, b)
    print(f"Solución por Eliminación Gaussiana: {solucion}")
