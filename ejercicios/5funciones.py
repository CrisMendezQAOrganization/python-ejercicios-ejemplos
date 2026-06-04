#Definimos una función sin parámetros
def saludar():
    print("Hola qué tal")

#Definir funciones que reciben y devuelven parámetros
def saludarConNombre(nombre):
    saludo = "Hola" + nombre
    return saludo

#Llamamos a la función
saludar()

#En primer lugar guardamos el nombre
nombre = input("Introduce tu nombre: ")
saludo = saludarConNombre(nombre)
print(saludo)

nombre2 = input("Introduce tu nombre 2: ")
saludo2 = saludarConNombre(nombre2)
print(saludo2)