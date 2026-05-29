import numpy as np

def gauss_jordan(A, b):
    """
    Resuelve el sistema Ax = b mediante el método de Gauss-Jordan.
    """
    n = len(b)
    M = np.hstack([A.astype(float), b.astype(float).reshape(-1, 1)])
    
    for i in range(n):
        # Pivoteo parcial
        max_row = np.argmax(np.abs(M[i:n, i])) + i
        if M[max_row, i] == 0:
            raise ValueError("El sistema no tiene solución única.")
        M[[i, max_row]] = M[[max_row, i]]
        
        # Normalizar la fila del pivote (hacer el pivote igual a 1)
        M[i] = M[i] / M[i, i]
        
        # Hacer cero el resto de los elementos de la columna
        for j in range(n):
            if i != j:
                M[j] -= M[j, i] * M[i]
                
    return M[:, -1]

# Ejemplo de uso:
if __name__ == "__main__":
    A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
    b = np.array([1, -2, 0])
    solucion = gauss_jordan(A, b)
    print(f"Solución por Gauss-Jordan: {solucion}")
