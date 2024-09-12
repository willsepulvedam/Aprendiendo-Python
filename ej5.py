import pandas as pd

def costo_mensual(x):
    tarifa_base = 6
    if x <= 300:
        costo_total = tarifa_base + 0.10 * x
    else:
        costo_total = tarifa_base + 0.10 * 300 + 0.06 * (x - 300)
    return costo_total

valores_x = [0, 150, 200, 350, 1000]

data = {
    "kWh recorridos": valores_x,
    "costo mensual": [costo_mensual(x) for x in valores_x],
}

df = pd.DataFrame(data)

df['costo mensual'] = df['costo mensual'].apply(lambda x: f"${x:.2f}")
df['kWh recorridos'] = df['kWh recorridos'].apply(lambda x: f"{x}kWh")

print(df)