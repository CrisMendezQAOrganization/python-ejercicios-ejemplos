#Lista de notas que son números
notas = [4, 6, 8, 10]
#Lista de nombres que son texto
nombres = ["Juan", "María", "Antonio"]

#Agregar un nuevo nombre a la lista
nombre = input("Introduce un nombre: ")
nombres.append(nombre)

#Agrega directamente el nombre de María
nombres.append("María")

notas.append(11)

#Eliminar un elemento de la lista
notaAeliminar = float (input("Introduce la nota que desea eliminar:"))
notas.remove(notaAeliminar)
nombreAeliminar = input("Introduzca el nombre que desea eliminar:")
nombres.remove(nombreAeliminar)


#Imprimir la lista
print(notas)
print(nombres)

#Mostrar el segundo alumno de la lista
print("Alumno en la posición 2", nombres[1])
