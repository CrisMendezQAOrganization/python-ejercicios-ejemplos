#FUNCIONES SIEMPRE PONER ARRIBA POR SI ACASO
#Cálculo del descuento
def calcular_descuento(precio_unidad, cantidad, descuento):
    total = precio_unidad * cantidad
    total_desc= (total * descuento) / 100
    return total - total_desc
    
def agregar_iva(precio_unidad):
    iva = precio_unidad * 0.21
    return precio_unidad + iva


#Pedir datos a la usuaria. Mostrar cantidad, nombre, descuento y precio total con descuento
nombre_producto = input("Nombre del producto: ")
precio_unidad = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad a comprar: "))
descuento = float(input("Descuento (%): "))


precio_final = calcular_descuento(precio_unidad, cantidad, descuento)

print("Nombre del producto:", nombre_producto)
print("Cantidad:", cantidad)
print("Descuento:", descuento, "%")
print("Precio total con descuento:", precio_final)



#Mostrar total con IVA aplicado
total_coniva = agregar_iva(precio_final)
print("Total con IVA: ", total_coniva)
