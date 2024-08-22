def calculadora():
    def suma(a, b):
     return a + b
    print("seleccione su nivel de formacion")
    print("1 Tecnico")
    print("2 tecnologo")
    print("3 profesional")

   
    opcion = int(input("ingresar su opcion (1/2/3): "))
    num1 = float(input("ingrese primera nota: "))
    num2 = float(input("ingrese segunda nota: "))
    promedio = (num1+num2)/2
     
    if opcion ==1: 
      print("NIVEL: tecnico MINIMO DE APROBACION: 3.0")
      print("el resultado es: ", promedio)
      if promedio>=3.0: print("aprobaste")
      else: print("reprobaste")
      

    elif opcion == 2: 
    
      print ("NIVEL: tecnologo MINIMO DE APORBACION: 3.5")
      print('El resultado es:', promedio)
      if promedio>=3.5: print("aprobaste")
      else: print("reprobaste")
    
    elif opcion == 3: 
      print ("NIVEL: profesional MINIMO DE APORBACION: 4.0")
      print('El resultado es:', promedio)
      if promedio>=4.0: print("aprobaste")
      else: print("reprobaste")
      
       
calculadora()
