# entrada de datos

edad = int (input("ingrese su edad: "))
genero = str (input("ingrese su genero (M o F: )")).upper()

#condicional
if edad <12:
    print("categoria: niño")
elif 12 <=edad <=17:
    print("categoria: adolecente")
else:
    if genero == "M":
        print("categoria: Hombre")
    elif genero =="F":
        print("Categoria: mujer")
    else:
        print("otro")