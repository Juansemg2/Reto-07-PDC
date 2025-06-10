Reto 7 PDC

Juan Sebastian Martinez Garcia

En el siguiente reto se encontraran los codigos de solucion a los siguientes problemas algoritmicos:

1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

    range(100)
    for num in range(100):
        cuadrado=num**2
        num+=1
        print(num, cuadrado)

2.Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

    print("Lista de numero impares:")
    for num in range(1,1000,2): print(num)
    print("Lista de numero pares:")
    for num in range(2,1001,2): print(num)

3.Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

    n=int(input("ingrese un numero entero mayor a 2: "))
    for i in range (2,n+1,2):
        print(i)

4.Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

    n=int(input("ingrese un numero entero : "))
    factorial=1
    for i in range (1,n+1):
        factorial*=i
    print (factorial)

5.Calcular el valor de 2 elevado a la potencia n usando ciclos for.

    n=int(input("ingrese un numero entero : "))
    potencia = 1
    for i in range (1,n+1):
        potencia*=2
    print (potencia)

6.Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

    n = int(input("Ingrese un número natural (exponente): "))
    base = float(input("Ingrese un número real (base): "))
    resultado = 1
    for i in range(n):
        resultado *= base  
    print(base, "elevado a", n, "es igual a: ", resultado)

7.Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

    print("Tabla del 1")
    for i in range (1,10):
        resultado=i*1
        print(i, "* 1 = ", resultado )
    print("Tabla del 2")
    for i in range (1,10):
        resultado=i*2
        print(i, "* 2 = ", resultado )
    print("Tabla del 3")
    for i in range (1,10):
        resultado=i*3
        print(i, "* 3 = ", resultado )
    print("Tabla del 4")
    for i in range (1,10):
        resultado=i*4
        print(i, "* 4 = ", resultado )
    print("Tabla del 5")
    for i in range (1,10):
        resultado=i*5
        print(i, "* 5 = ", resultado )
    print("Tabla del 6")
    for i in range (1,10):
        resultado=i*6
        print(i, "* 6 = ", resultado )
    print("Tabla del 7")
    for i in range (1,10):
        resultado=i*7
        print(i, "* 7 = ", resultado )
    print("Tabla del 8")
    for i in range (1,10):
        resultado=i*8
        print(i, "* 8 = ", resultado )
    print("Tabla del 9")
    for i in range (1,10):
        resultado=i*9
        print(i, "* 9 = ", resultado )

8.Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

    def aproximar_exponencial(x, n):
        aproximacion = 0
        for i in range(n + 1):
            termino = (x ** i) / math.factorial(i)
            aproximacion += termino 
        valor_real = math.exp(x)
        error = abs(valor_real - aproximacion)
        print(f"Aproximación de e^{x} usando {n} términos: {aproximacion}")
        print(f"Valor real usando math.exp({x}): {valor_real}")
        print(f"Diferencia (error): {error}")
    x = float(input("Ingrese el valor de x: "))
    n = int(input("Ingrese el número de términos de la serie: "))
    aproximar_exponencial(x, n)

9.Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

    import math
    def aproximar_seno(x, n):
        aproximacion = 0
        for i in range(n + 1):  
            signo = (-1) ** i  
            numerador = x ** (2 * i + 1)
            denominador = math.factorial(2 * i + 1)
            termino = signo * (numerador / denominador)
            aproximacion += termino  
        valor_real = math.sin(x)
        error = abs(valor_real - aproximacion)
        print(f"Aproximación de sin({x}) usando {n} términos: {aproximacion}")
        print(f"Valor real usando math.sin({x}): {valor_real}")
        print(f"Diferencia (error absoluto): {error}")
    x = float(input("Ingrese el valor de x (en radianes): "))
    n = int(input("Ingrese el número de términos de la serie: "))
    aproximar_seno(x, n)
