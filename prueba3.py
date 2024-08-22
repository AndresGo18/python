import math
print("------------------------------------------")
print("distancia entre dos puntos A y B, en 2D")
print("------------------------------------------")

#entradas
print("ingrese las cordenadas del punto A:")
AX= float(input("AX:  "))
AY= float(input("AY:  "))

print("ingrese las coordenadas del punto B")
BX = float(input("BX: "))
BY = float(input("BY: "))

#proceso
D = ((AX-BX**2)+(AY-BY**2))**0.5

#salida
print("\nsalida: ")
print("el resultado de la distancia es: ", math.ceil (D))
