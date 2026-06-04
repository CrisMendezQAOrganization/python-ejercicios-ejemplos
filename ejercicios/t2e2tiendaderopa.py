#Precios
precio_camiseta = 10
precio_sudadera = 20.5
precio_gorra = 5.5

#Pedir cantidad de cada artículo
total_camisetas = int(input("Número de camisetas: "))
total_sudaderas = int(input("Número de sudaderas: "))
total_gorras = int(input("Número de gorras: "))

#Calcular el total de la compra
total_compra = (precio_camiseta * total_camisetas) + (precio_sudadera * total_sudaderas) + (precio_gorra * total_gorras)

#Añade el 21% de IVA al total (calcular el 0.21)
iva = total_compra * 0.21

#Precio final
precio_final = iva + total_compra

# Mostrar resultados
print("Total sin IVA: ", total_compra)
print("IVA: ", iva)
print("Precio final: ", precio_final)