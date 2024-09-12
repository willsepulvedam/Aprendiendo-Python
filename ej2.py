velocidad_maxima = 65
velocidad_minima = 40
costo_por_milla = 15

def calcular_multa(velocidad):
    if velocidad < velocidad_minima:
        multa = (velocidad_minima - velocidad) * costo_por_milla
        return f"Infracción por baja velocidad. Multa: ${multa}"
    elif velocidad > velocidad_maxima:
        multa = (velocidad - velocidad_maxima) * costo_por_milla
        return f"Infracción por alta velocidad. Multa: ${multa}"
    else:
        return "No hay infracción."


velocidades = [30, 25, 70, 55, 65, 40]

for velocidad in velocidades:
    resultado = calcular_multa(velocidad)
    print(f"Velocidad: {velocidad} mi/h - {resultado}")