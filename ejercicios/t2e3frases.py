#Pedir a la usuaria que introduzca una frase
frase = input("Introduce una frase: ")

#Obtenemos el número de letras de la frase
longitud = len(frase)


#Imprimimos la palabra
print(frase)

#Imprimimos la longitud (al ser un número no puede ir solo)
print("Longitud de la frase", longitud)

#Imprimir cadena en mayúsculas
print("La frase en mayúsculas es: ", frase.upper())

#Imprimis la cadena en minúsculas
print("La frase en minúsculas es: ", frase.lower())
