import numpy as np
# Ingresar las dimensiones de la matriz
n= int(input('Ingrese el numero de filas (n):'))
m= int(input('Ingrese el numero de columnas (m):'))
# Crear matrices A y B vacias
A= np.zeros((n,m))
B= np.zeros((n,m))
# Pedir elementos de la matriz A
print('Ingrese los elementos de la matriz (A):')
for i in range(n):
    for j in range(m):
        A[i,j] = int(input(f'Elemento [{i+1}, {j+1}] de A:'))
# Pedir elementos de la matriz B
print('Ingrese los elementos de la matriz (B):')
for i in range(n):
    for j in range(m):
        B[i,j] = int(input(f'Elemento [{i+1}, {j+1}] de B:'))

# Suma de las matrices
C= np.add(A,B)
# Imprimir la matriz resultante
print('La matriz resultante C es: ')
print(C)