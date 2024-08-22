import numpy as np

#ingresar el numero del alumno
tamano = int(input("ingresar el numero de alumnos"))

#definir edades
edades = np.zeros(tamano, dtype=int)

for i in range(tamano):
 edades[i]= int(input(f"ingrese la edad del alumno {i+1}: "))

 #mostrar las edades de los alumnos
print("las edades de los alumno son: ")
for i in range(tamano):
  print(edades[i])