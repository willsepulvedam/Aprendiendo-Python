# SymPy es una Biblioteca de Python para cálculos simbólicos.
# Math es una Biblioteca estándar de Python para funciones matemáticas (raíz cuadrada, trigonometría, etc.).
import sympy as sp 
import math

# Aquí se declara una variable simbólica x, que se utilizará para manejar expresiones algebraicas en SymPy. 
# En lugar de tratar a x como un valor numérico específico, SymPy permite trabajar con x como una incógnita algebraica.
x = sp.symbols('x')

# Se define una expresión algebraica cúbica
exp_cubica = x**3 + 7*x**2 + 10*x

# Se realiza la factorización de la expresión cúbica usando sp.factor. 
# Este método descompone la expresión en factores, en lugar de trabajar con la expresión en su forma expandida.
exp_factorizada = sp.factor(exp_cubica)

#Aquí, sp.solve se utiliza para resolver la ecuación cúbica y obtener los valores de x que satisfacen la ecuación 
# (es decir, los ceros o raíces).
intervalos = sp.solve(exp_cubica, x)

# Aquí se define el dominio de la función, es decir, los valores de x donde la expresión cúbica es mayor o igual a cero. 
# sp.solveset resuelve la desigualdad  en el dominio de los números reales (sp.S.Reals).
dominio_funcion = sp.solveset(exp_cubica >= 0, x, domain=sp.S.Reals)

# Esta parte del código imprime los resultados:
print(f"Factorizacion: {exp_factorizada}")
print(f"Intervalos: {intervalos}")
print(f"el dominio de la funcion es: {dominio_funcion}")

# Aquí se define una función llamada temperatura(x) 
def temperatura(x):
    # Vuelve a calcular la expresión cúbica con el valor de x.
    exp_cubica = x**3 + 7*x**2 + 10*x
    # Si el valor de x está dentro del dominio donde la expresión cúbica es mayor o igual a cero, 
    # se calcula la raíz cuadrada de la expresión usando math.sqrt.
    if x in dominio_funcion:
        return math.sqrt(exp_cubica)
    # Si el valor de x no está dentro del dominio, devuelve un mensaje indicando que no se puede calcular.
    else:
        return "No se puede calcular, fuera del dominio"

# Finalmente, el programa solicita al usuario que ingrese un número (x), 
# luego llama a la función temperatura(x) para calcular el resultado basado en la expresión cúbica. 
# El resultado es impreso en la pantalla.   
x = float(input("ingresa el numero: "))
print(f"La temperatura del objeto conocido es: {temperatura(x)}")

