#6.Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
n = int(input("Ingrese un número natural (exponente): "))
base = float(input("Ingrese un número real (base): "))

resultado = 1

for i in range(n):
    resultado *= base  

print(base, "elevado a", n, "es igual a: ", resultado)
