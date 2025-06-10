#1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
range(100)
for num in range(100):
    cuadrado=num**2
    num+=1
    print(num, cuadrado)