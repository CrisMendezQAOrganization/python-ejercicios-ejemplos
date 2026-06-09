#Pedir una cantidad en euros
euros = float(input("Cantidad en euros:"))

#Función recibir euros y devolver en dólares (1 euros = 1.1 dólares)
def euros_a_dolares(euros):
    dolares = euros * 1.1
    return dolares

#Función recibir euros y devolver libras (1 euro = 0.87 libras)
def euros_a_libras(euros):
    libras = euros * 0.87
    return libras

#Muestra la cantidad en euros, dólares y libras
dolares = euros_a_dolares(euros)
libras = euros_a_libras(euros)

print("Euros:", euros)
print("Dólares:", dolares)
print("Libras:", libras)
    