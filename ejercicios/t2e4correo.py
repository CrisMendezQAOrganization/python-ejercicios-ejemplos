#Pedir a la usuaria que introduzca un email
email = input("Introduce un correo electrónico: ")

#Obtenemos el número de letras del email
longitud = len(email)

#Email en mayúsculas
emailmayusculas = email.upper()

#Email en minúsculas
emailminusculas = email.lower()

#Imprimimos la palabra
print(email)

#Imprimimos la longitud (al ser un número no puede ir solo)
print("Longitud", longitud)

#Imprimir cadena en mayúsculas
print(emailmayusculas)

#Imprimir la cadena en minúsculas
print(emailminusculas)
