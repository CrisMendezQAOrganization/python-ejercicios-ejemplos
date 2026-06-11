#Crear lista con los 8 planetas
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

#La usuaria elige un número del 1 al 8
numero = int(input("Elige un número del 1 al 8: "))

#Mostrar el planeta correspondiente
print("El planeta es:", planetas [numero - 1])