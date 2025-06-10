#Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación. 

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
