costo_cmcuadrado = 0.02
costopieza_fijo = 0.10

def calcular_costo(lado_cm):
    area = lado_cm **2
    costo_total = (area * costo_cmcuadrado) + costopieza_fijo
    return costo_total

lado_4_cm = 4
costo_pieza_4_cm = calcular_costo(lado_4_cm)
print(f"El costo de fabricación de una pieza con lado de {lado_4_cm} cm es: ${costo_pieza_4_cm:.2f}")

for lado in range(1, 1001):
    costo = calcular_costo(lado)
    print(f"Lado: {lado} cm - Costo: ${costo:.2f}")