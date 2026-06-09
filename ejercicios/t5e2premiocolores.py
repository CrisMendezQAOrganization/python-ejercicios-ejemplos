
def color(colorElegido):
    if (colorElegido == "azul"):
        mensaje = "Premio conseguido"
    else:
        mensaje = "Prueba otro color"
    return mensaje
#Pedir a usuaria 5 veces que introduzca un color
for i in range(5):
    colorElegido = input("Introduce un color ").lower()
    mensaje = color(colorElegido)
    print(mensaje)

    if colorElegido == "azul":
        break




    
