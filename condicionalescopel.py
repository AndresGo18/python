#entrada de datos
genero = str(input("por favor ingrese genero(M o F): ")).upper()
edad = int(input("por favor ingrese su edad: "))


#condicional
if(genero =="M" or edad >=18):
    print("cumple con los requisitos para el servicio militar")
else:
    print("no cumples con los requisitos para el servicio militar")
