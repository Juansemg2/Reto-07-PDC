#4.Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
n=int(input("ingrese un numero entero : "))
factorial=1
for i in range (1,n+1):
    factorial*=i
print (factorial)
