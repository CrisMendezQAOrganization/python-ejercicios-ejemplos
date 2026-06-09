#Pedir a la usuaria que introduzca un email
email = input("Introduce un correo electrónico: ")

#Obtenemos el número de letras del email
longitud = len(email)

#Imprimimos la palabra
print(email)

#Imprimimos la longitud (al ser un número no puede ir solo)
print("Longitud", longitud)

#Imprimir cadena en mayúsculas
print("Correo en mayúsculas:", email.upper())

#Imprimir la cadena en minúsculas
print("Correo en minúsculas:", email.lower())
