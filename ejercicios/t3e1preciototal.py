#Pedir datos a la usuaria. Mostrar cantidad, nombre, descuento y precio total con descuento
nombre_producto = input("Nombre del producto: ")
precio_unidad = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad a comprar: "))
descuento = float(input("Descuento (%): "))

#Cálculo del descuento
def calcular_descuento(precio_unidad, cantidad, descuento):
    total = precio_unidad * cantidad
    descuento = total * (descuento / 100)
    total_condesc = total - descuento
    return total_condesc

total_condesc = calcular_descuento(precio_unidad, cantidad, descuento)

print("Nombre del producto:", nombre_producto)
print("Cantidad:", cantidad)
print("Descuento:", descuento, "%")
print("Precio total con descuento:", total_condesc)

#Función que reciba una cantidad y le agregue 21%IVA
def agregar_iva(total_condesc):
    iva = total_condesc * 0.21
    total_coniva = total_condesc + iva
    return total_coniva
    

#Mostrar total con IVA aplicado
total_coniva = agregar_iva(total_condesc)

print("Total con IVA: ", total_coniva)
