def prod_calcomanias(x_calcomanias):
    if x_calcomanias < 10000:
        precio_calcomanias = 0.15 - 0.000002*x_calcomanias
        costo_total = 0.095 *x_calcomanias - 0.0000005*x_calcomanias**2
    else:
        precio_calcomanias = 0.14
        costo_total = 0.1 * x_calcomanias
        
    ingreso_total = precio_calcomanias * x_calcomanias
    utilidad = ingreso_total - costo_total
    return utilidad
    
n1_calcomanias = 800
n2_calcomanias = 86700
costo1 = prod_calcomanias(n1_calcomanias)
costo2 = prod_calcomanias(n2_calcomanias)

    
print(f"N* de calcomanias: {n1_calcomanias} cm - Costo: ${costo1:.2f}")
print(f"N* de calcomanias: {n2_calcomanias} cm - Costo: ${costo2:.2f}")