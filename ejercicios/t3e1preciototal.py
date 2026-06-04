#Pedir datos a la usuaria
nombre_producto = input("Nombre del producto: ")
precio_unidad = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento (%): "))

#Cálculo del descuento
def calcular_descuento(precio_unidad, cantidad, descuento):
    total = precio_unidad * cantidad
    descuento = total * (descuento / 100)
    total_final = total - descuento
    return total_final

#Mostrar cantidad, nombre y desuento con precio total con descuento
nombre_producto = input("Nombre del producto: ")
precio_unidad = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad a comprar: "))
descuento = float(input("Descuento (%): "))

print("Nombreroducto:", nombre_producto)
print("Cantidad:", cantidad)
print("Descuento:", descuento, "%")
print("Precio total con descuento:", total_final)

#Función que reciba una cantidad y le agregue 21%IVA
def agregar_iva(total):
    iva = total * 0,21
    return total + iva

