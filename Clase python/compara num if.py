numero1 = int(input("Dame un numero: "))
numero2 = int(input("Dame otro numero: "))

if numero1 == numero2:
    print("Son iguales!")

elif numero1 != numero2:
    print("Son diferentes!")

if numero1 > numero2:
    print(numero1, "es mayor que", numero2)

elif numero2 > numero1:
    print(numero2, "es mayor que", numero1) 


input("\nPresiona cualquier tecla para continuar")
