import sympy as sp
import math

x = sp.symbols('x')
exp_cubica = x**3 + 7*x**2 + 10*x

exp_factorizada = sp.factor(exp_cubica)

intervalos = sp.solve(exp_cubica, x)

dominio_funcion = sp.solveset(exp_cubica >= 0, x, domain=sp.S.Reals)

def format_interval(interval):
    if isinstance(interval, sp.Interval):
        left = '-∞' if interval.start == -sp.oo else interval.start
        right = '+∞' if interval.end == sp.oo else interval.end
        return f"[{left}, {right}]"
    return str(interval)

if isinstance(dominio_funcion, sp.Union):
    formatted_domain = ' ∪ '.join([format_interval(interval) for interval in dominio_funcion.args])
else:
    formatted_domain = format_interval(dominio_funcion)

print(f"Factorizacion: {exp_factorizada}")
print(f"Intervalos: {intervalos}")
print(f"El dominio de la funcion es: {formatted_domain}")

def temperatura(x):
    if x in dominio_funcion:
        return math.sqrt(float(x**3 + 7*x**2 + 10*x))
    else:
        return "No se puede calcular, fuera del dominio"

x = float(input("Ingresa el número: "))
print(f"La temperatura del objeto conocido es: {temperatura(x)}")

