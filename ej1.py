import pandas as pd

def fnc1(x):
    return 3*x+1

def fnc2(x):
    return 4*x**2+2*x+1

def fnc3(x):
    if x >= 5:
        return 8*x-2
    else:
        return x**2+2*x
    
valores = [-1, 1, 3, 8]

data = {
    "x": valores,
    "fnc1(x)": [fnc1(x) for x in valores],
    "fnc2(x)": [fnc2(x) for x in valores],
    "fnc3(x)": [fnc3(x) for x in valores],
}

df = pd.DataFrame(data)

print(df)


