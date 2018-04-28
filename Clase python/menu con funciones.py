def comparacion(numero1,numero2,numero3):

    if numero1 == numero2  and numero2 == numero3:
        print("Son iguales")
    elif numero1 > numero2 > numero3 or numero1>numero3>numero2:
        print(numero1, " es el mayor")
    elif numero2 > numero1 > numero3 or numero2>numero3>numero1:
        print(numero2, " es el mayor")
    elif numero3 > numero1 > numero or numero3 > numero2 > numero3:
        print(numero3, " es el mayor")

    else:
        print("Son diferentes!")

def suma(numero1,numero2):

    resultadoSum = numero1 + numero2
    print("El resultado de la suma es: ", resultadoSum)

def resta(numero1,numero2):
    resultadoResta = numero1 - numero2
    print("El resultado de la resta es: ", resultadoResta)

def division(numero1,numero2):
    resultadoDiv = numero1 - numero2
    print("El resultado de la división es: ", resultadoDiv)

def multiplicacion(numero1,numero2):
    resultadoMul = numero1 * numero2
    print("El resultado de la Multiplicación es: ", resultadoMul)

def iva(fIVA,fCantidad):

    fResultadoIva = fIVA*fCantidad

    print("El IVA es:", fIVA)
    print("La cantidad es: $", fCantidad)
    print("El IVA de la cantidad es: ", fResultadoIva)

def tablas(tabla,limite):

    for x in range(0, limite):
        print(tabla, "X", x+1, "=", (x+1)*tabla)

def datos(nombreU,edadU,pesoU):
    print("Tus datos son:", nombreU, edadU, pesoU)
    



print("\n 0. Comparación de números")
print("\n 1. Suma")
print("\n 2. Resta")
print("\n 3. Division")
print("\n 4. Imprimir tus datos")
print("\n 5. Multiplicación")
print("\n 6. Tabla de multiplicar")
print("\n 7. Salir")

bandera = bool(True)

while(bandera):
    selec = input("\nSelecciona un numero para la opción que desees realizar: ")

    if selec=='0':
        numero1 = int(input("Dame un numero: "))
        numero2 = int(input("Dame otro numero: "))
        numero3 = int(input("Dame un numero: "))

        comparacion(numero1,numero2,numero3)

        input("\nPresiona cualquier tecla para salir")

    if selec=='1':
        numero1 = int(input("Dame un numero: "))
        numero2 = int(input("Dame otro numero: "))

        suma(numero1,numero2)

        input("\nPresiona cualquier tecla para salir")


    if selec=='2':
        numero1 = int(input("Dame un numero: "))
        numero2 = int(input("Dame otro numero: "))

        resta(numero1,numero2)
        input("\nPresiona cualquier tecla para salir")

    if selec=='3':
        numero1 = int(input("Dame el dividendo: "))
        numero2 = int(input("Dame el divisor: "))

        division(numero1,numero2)
        input("\nPresiona cualquier tecla para salir")

    if selec=='4':
        nombreU = input("Dame tu nombre: ")
        edadU = input("Dame tu edad: ")
        pesoU = input("Dame tu peso: ")
        datos(nombreU,edadU,pesoU)
        input("\nPresiona cualquier tecla para salir")

    if selec=='5':
        numero1 = int(input("Dame un factor: "))
        numero2 = int(input("Dame otro factor: "))

        multiplicacion(numero1,numero2)
        input("\nPresiona cualquier tecla para salir")

    if selec=='6':
        tabla = int(input("Que tabla quieres usar?:"))
        limite = int(input("Hasta qué numero quieres multiplicar?:"))


        tablas(tabla,limite)
        input("\nPresiona cualquier tecla para salir")


    if selec=='7':
        print("Saliendo...")
        bandera=bool(False)
        input("\nPresiona cualquier tecla para salir")
