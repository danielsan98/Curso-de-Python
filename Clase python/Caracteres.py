miCadena = input("Dame un a palabra:")
primeraL = miCadena[0]
ultimaL = miCadena[len(miCadena)-1]

print("\n")
print("La primera letra de tu cadena es:", primeraL)
print("\n")
print("La ultima letra de tu cadena es:", ultimaL)

print("\n")
print("La longitud de la cadena es:", len(miCadena))
print("\n")


print("----------------------------------")
var = input("Dame otra palabra: ")
print("Tu palabra es:", var)

var2 = int(input("Escribe el indice del caracter que quieras ver:"))
print("\nEl caracter es:", var[var2])

input("\n Presiona cualquier tecla para continuar")
