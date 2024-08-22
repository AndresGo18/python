contador_positivos = 0
numero = int(input("ingresar un numero (numero negativo para terminar) "))
while numero >= 0:
    contador_positivos+=1
    numero = int(input("ingrese otro numero(numero negativo para terminar)"))

    print(f"has ingresado{contador_positivos} numero postivo")