#8.Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación
import math

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
