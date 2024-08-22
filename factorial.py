#definir metodo factorial
def factorial(num):
    f=1
    for i in range (1,num):
        f=f*i
    return f

n = int(input("ingrese el valor de  n: "))
m = int(input("tamano del grupo a crear: "))
nf = factorial(n)
mf = factorial(m)
nmf = factorial(n-m)

c = nf/(nf*nmf)
print(f"la cantidad de combinacion es{c} ",)