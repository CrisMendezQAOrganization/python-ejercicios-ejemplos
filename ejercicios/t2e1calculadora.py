#Pedir al usuario que introduzca 2 números 
#Convertimos a número. Int enteros Float decimales
numero1 = float(input("Introduzca un número: "))
numero2 = float(input("Introduzca otro número: "))

#Hacemos las operaciones

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division= numero1 / numero2
media = (numero1 + numero2) / 2

#Imprimimos los resultados
print("Suma", suma)
print("Resta", resta)
print("Multiplicación", multiplicacion)
print("División", division)
print("Media", media)