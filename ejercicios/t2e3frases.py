#Pedir a la usuaria que introduzca una frase
frase = input("Introduce una frase: ")

#Obtenemos el número de letras de la frase
longitud = len(frase)

#Frase en mayúsculas
frasemayusculas = frase.upper()

#Frase en minúsculas
fraseminusculas = frase.lower()

#Imprimimos la palabra
print(frase)

#Imprimimos la longitud (al ser un número no puede ir solo)
print("Longitud", longitud)

#Imprimir cadena en mayúsculas
print(frasemayusculas)

#Imprimis la cadena en minúsculas
print(fraseminusculas)
