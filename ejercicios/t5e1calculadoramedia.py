#Pedir a usuaria cuántas notas desea introducir
def calcular_media():
    cantidad = int(input("¿Cuántas notas deseas introducir?: "))
    suma = 0

    for i in range(cantidad):
        nota = float(input(f"Introduce la nota {i + 1}: "))
        suma += nota
    
    media = suma / cantidad
    return media


# Llamar a la función
nota_media = calcular_media()

# Imprimir resultado
print("La nota media es:", nota_media)