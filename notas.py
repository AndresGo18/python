#entrada de datos

nota1 = float(input("ingrese la primera nota: "))
nota2 = float(input("ingrese la segunda nota: "))
nota3 = float(input("ingrese la tercera nota: "))

promedio = (nota1+nota2+nota3)/3.0

if promedio> 3.0:
    print("aprobaste con", promedio )
else:
    print("reprobo con", promedio)



