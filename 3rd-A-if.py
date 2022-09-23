#Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
nro_1 = int(input("Ingrese nro 1: "))
nro_2 = int(input("Ingrese nro 2: "))
opt = input("Opciones disponibles: \nA para sumar, \nB para restar, \nC para multiplicar, \nD para finalizar.\nIngrese su opcion: ")
#Mostrar una suma de los dos números
if opt.capitalize() == "A":
    suma = nro_1 + nro_2
    print(f"El resultado de la suma de{nro_1} y {nro_2} es {suma}")
elif opt.capitalize() == "B":
        resta = nro_1 - nro_2 
        print(f"El resultado de la resta de{nro_1} y {nro_2} es {resta}")
#Mostrar una multiplicación de los dos números
elif opt.capitalize() == "C":
        multiplicar = nro_1 * nro_2
        print(f"El resultado de la multiplicacion de{nro_1} y {nro_2} es {multiplicar}")
#Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
elif opt.capitalize() == "D":
        print("Proceso finalizado")
#En caso de no introducir una opción válida, el programa informará de que no es correcta.
else: 
    print("Opcion ingresada incorrecta.")
