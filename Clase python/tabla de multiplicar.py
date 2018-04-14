tabla = int(input("Que tabla quieres usar?:"))
limite = int(input("Hasta qué numero quieres multiplicar?:"))


for x in range(0, limite):
    print(tabla, "X", x+1, "=", (x+1)*tabla)


input("\n Presiona cualquier tecla para continuar")
