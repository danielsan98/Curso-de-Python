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


input("\nPresione cualquier tecla para continuar")
