#Guardamos la ciudad del usuario
ciudad = input("Introduce tu ciudad: ")

bienvenida = "Bienvenidos a " + ciudad

#Obtenemos el número de letras de la cadena
longitud = len(bienvenida)

#Poner la cadena en mayúsculas
bienvenidamayusculas = bienvenida.upper()

#Poner la cadena en minúsculas
bienvenidaminusculas = bienvenida.lower()

#IMPRIMIR CADENAS

#Imprimimos la palabra
print(bienvenida)

#Imprimimos la longitud (al ser un número no puede ir solo)
print("Longitud", longitud)

#Imprimir cadena en mayúsculas
print(bienvenidamayusculas)

#Imprimis la cadena en minúsculas
print(bienvenidaminusculas)
