#5.Calcular el valor de 2 elevado a la potencia n usando ciclos for.
n=int(input("ingrese un numero entero : "))
potencia = 1
for i in range (1,n+1):
    potencia*=2
print (potencia)

