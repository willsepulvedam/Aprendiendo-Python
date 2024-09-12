import random

def generar_lista_aleatoria(tamañó, rango):
    return [random.randint(1, rango) for i in range(tamañó)]

def verificar_numero_en_lista(lista, numero):
    return numero in lista

def proceso():
    tamaño = 10
    rango = 100
    
    lista = generar_lista_aleatoria(tamaño, rango)
    
    print(f"Lista generada: {lista}")
    
    while True:
        try:
            numero = int(input("Ingrese un número para verificar si está en la lista: "))
            if verificar_numero_en_lista(lista, numero):
                print(f"El número {numero} está en la lista.")
                break
            else:
                print(f"El número {numero} no está en la lista.")
        except ValueError:
            print("Error: Ingrese un número entero.")
if __name__ == "__main__":
    proceso()