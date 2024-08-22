import numpy as np


# Ingresar las dimensiones de la matriz
n= int(input('Ingrese el numero de filas (n):'))
m= int(input('Ingrese el numero de columnas (m):'))

print("ingrese los numeros")
matriz = np.zeros((n,m))

for i in range(n):
    for j in range(m):
        matriz[i, j] = int(input(f"ingrese el elemento [{i+1},{j+1}]: "))

positivos = np.sum(matriz > 0)
negativos = np.sum(matriz < 0)
neutros = np.sum(matriz == 0)



print("\nmatriz ingresada: ")
print(matriz)

print("\nresultados")
print(f"numeros positivos : {positivos}")
print(f"numeros negativos : {negativos}")
print(f"numeros neutros : {neutros}")
