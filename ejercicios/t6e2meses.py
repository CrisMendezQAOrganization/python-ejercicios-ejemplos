#Si el mes es JUNIO se musetra mensaje EL MEJOR MES
def mesGanador(mes):
    if (mes == "Junio"):
        print ("EL MEJOR MES")

#Crear lista 12 meses del año
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

#Pedir a usuaria un número del 1 al 12
numero = int(input("Elige un número del 1 al 12: "))

#Mostrar el mes correspondiente
if 1 <= numero <= 12:
    mes = meses[numero - 1]
    print("El mes es:", mes)
    mesGanador(mes)

