def notaFinal(nota):
    if (nota > 8):
        mensaje = "SOBRESALIENTE"
    elif (nota < 5):
        mensaje = "SUSPENSO"
    else:
        mensaje = "APROBADO"
    return mensaje

#PEDIMOS AL USUARIO QUE INTRODUZCA SU NOTA

nota = float(input("Introduce tu nota del examen:"))

#LLAMAMOS A NOTA FINAL PARA QUE NOS DIGA EL MENSAJE
mensaje = notaFinal(nota)
#IMPRIMIMOS EL MENSAJE CON LA NOTA FINAL
print(mensaje)