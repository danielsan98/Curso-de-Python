nombreU = input("Dame tu nombre: ")
edadU = input("Dame tu edad: ")
pesoU = input("Dame tu peso: ")


print("\n 0. Comparación de números")
print("\n 1. Suma")
print("\n 2. Resta")
print("\n 3. Division")
print("\n 4. Imprimir tus datos")
print("\n 5. Multiplicación")
print("\n 6. Tabla de multiplicar")
print("\n 7. Salir")

selec = input("\nSelecciona un numero para la opción que desees realizar: ")


if selec=='0':
    numero1 = int(input("Dame un numero: "))
    numero2 = int(input("Dame otro numero: "))
    numero3 = int(input("Dame un numero: "))

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

    input("\nPresiona cualquier tecla para salir")

if selec=='1':
    numero1 = int(input("Dame un numero: "))
    numero2 = int(input("Dame otro numero: "))

    resultadoSum = numero1 - numero2
    print("El resultado de la suma es: ", resultadoSum)
    input("\nPresiona cualquier tecla para salir")


if selec=='2':
    numero1 = int(input("Dame un numero: "))
    numero2 = int(input("Dame otro numero: "))

    resultadoResta = numero1 - numero2
    print("El resultado de la resta es: ", resultadoResta)
    input("\nPresiona cualquier tecla para salir")

if selec=='3':
    numero1 = int(input("Dame el dividendo: "))
    numero2 = int(input("Dame el divisor: "))

    resultadoDiv = numero1 - numero2
    print("El resultado de la división es: ", resultadoDiv)
    input("\nPresiona cualquier tecla para salir")

if selec=='4':
    print("Tus datos son:", nombreU, edadU, pesoU)
    input("\nPresiona cualquier tecla para salir")

if selec=='5':
    numero1 = int(input("Dame un factor: "))
    numero2 = int(input("Dame otro factor: "))

    resultadoMul = numero1 - numero2
    print("El resultado de la Multiplicación es: ", resultadoMul)
    input("\nPresiona cualquier tecla para salir")

if selec=='6':
    tabla = int(input("Que tabla quieres usar?:"))
    limite = int(input("Hasta qué numero quieres multiplicar?:"))


    for x in range(0, limite):
        print(tabla, "X", x+1, "=", (x+1)*tabla)

    input("\nPresiona cualquier tecla para salir")


if selec=='7':
    print("Saliendo...")
    input("\nPresiona cualquier tecla para salir")
