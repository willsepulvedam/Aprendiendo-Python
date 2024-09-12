import sympy as sp 
import math

x = sp.symbols('x')

exp_cadratica = x**3 + 7*x**2 + 10*x

exp_factorizada = sp.factor(exp_cadratica)

intervalos = sp.solve(exp_cadratica, x)

dominio_funcion = sp.solveset(exp_cadratica >= 0, x, domain=sp.S.Reals)

print(f"Factorizacion: {exp_factorizada}")
print(f"Intervalos: {intervalos}")
print(f"el dominio de la funcion es: {dominio_funcion}")

def temperatura(x):
    exp_cadratica = x**3 + 7*x**2 + 10*x
    if x in dominio_funcion:
        return math.sqrt(exp_cadratica)
    else:
        return "No se puede calcular, fuera del dominio"
    
x = float(input("ingresa el numero: "))
print(f"La temperatura del objeto conocido es: {temperatura(x)}")

