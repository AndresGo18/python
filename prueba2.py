import math #realizar operaciones necesarias matg.ceil es redondear la cifra

print("-----------------------------------------")
print("numero de micro discos 3.5 necesarios")
print("-----------------------------------------")

#entrada

GB= float(input("ingrese Gb"))


#proceso
MG = GB*1024
MD = MG/1.44

#salida
print("\nsalida")
print("-----------------------------------------")
print(MD)


# usar la funcion decimal aproximar
print("numero de discos necesarios", math.ceil(MD))