#Crear función que reciba un color y devuelva un mensaje según el color elegido
def color(colorelegido):
    if (colorelegido == "rojo"):
        mensaje = "Pasión y energía"
    elif (colorelegido == "verde"):
        mensaje = "Esperanza y crecimiento"
    elif (colorelegido == "azul"):
        mensaje = "Calma y serenidad"
    elif (colorelegido == "amarillo"):
        mensaje = "Felicidad y optimismo"
    elif (colorelegido == "morado"):
        mensaje = "Sabiduría y creatividad"
    return mensaje


#Pedir a la usuaria que elija un color
colorelegido = input("Elige un color (rojo, verde, azul, amarillo, morado):").lower()
#LLAMAMOS A COLOR PARA QUE NOS DIGA EL MENSAJE
mensaje = color(colorelegido)
#IMPRIMIMOS EL MENSAJE CON LA NOTA FINAL
print(mensaje)

