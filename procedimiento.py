#entrada de datos
N1 = int(input("ingrese numero1: "))
N2 = int(input("ingrese numero2: "))

#definir metodos
def suma(N1, N2):
    suma = N1+N2
    print("la suma es " ,suma)

def resta(N1, N2):
    resta = N1-N2
    print("la resta es " ,resta)

def multiplicacion(N1, N2):
    multiplicacion= N1*N2
    print("la multiplicacion es " ,multiplicacion)

def division(N1, N2):
    division= N1/N2
    print("la division es " ,division)

#llamar metodos
suma(N1, N2)
resta(N1, N2)
multiplicacion(N1, N2)
division(N1, N2)