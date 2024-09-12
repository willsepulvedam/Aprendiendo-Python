import math

class CoeficienteCuadraticoCero(Exception):
    pass 

class DiscriminanteNegativo(Exception):
    pass


def resolver_ecuacion_cuadratica(a, b, c):
    if a == 0:
        raise CoeficienteCuadraticoCero("El coeficiente cuadrático no puede ser igual a cero.")
    

    discriminante = b**2 - 4*a*c
    
    
    if discriminante < 0:
        raise DiscriminanteNegativo("El discriminante es negativo, lo que resulta en raíces complejas.")
    

    raiz_discriminante = math.sqrt(discriminante)
    
    x1 = (-b + raiz_discriminante) / (2*a)
    x2 = (-b - raiz_discriminante) / (2*a)
    
    return x1, x2

try:
    a = float(input("Ingrese el coeficiente cuadrático (a): "))
    b = float(input("Ingrese el coeficiente lineal (b): "))
    c = float(input("Ingrese el coeficiente constante (c): "))
    
    raiz1, raiz2 = resolver_ecuacion_cuadratica(a, b, c)
    
    print(f"Las soluciones son: x1 = {raiz1}, x2 = {raiz2}")
    

except CoeficienteCuadraticoCero as e:
    print(e)
except DiscriminanteNegativo as e:
    print(e)
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
