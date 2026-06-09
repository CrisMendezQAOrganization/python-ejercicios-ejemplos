#Crea función que reciba el número y devuelva mensaje de victoria si acierta y derrota si falla. El ganador es el 4 
def comprobarNumero(numeroElegido):
    if (numeroElegido == 4):
        mensaje = "Victoria"
    else:
        mensaje = "Derrota"
    return mensaje
    

#Pedir número del 1 al 10
numero = int(input("Número del 1 al 10:"))

#Comprobar rango
if 1 <= numero <= 10:
    resultado = comprobarNumero(numero)
    print("Número elegido:", numero)
    print("Resultado:", resultado)
else:
    print("Error: el número debe estar entre 1 y 10:")
