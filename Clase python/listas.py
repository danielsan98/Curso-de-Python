nombre = "Daniel"
apellido = "Santiago"
estatura = 1.70
numCuenta = 314073787
sexo = "Masculino"

lista = [nombre, apellido, estatura, numCuenta, sexo]

print(lista)
print("El tamaño de la lista es:", len(lista))
print("Y es de tipo:", type(lista))
print("el tipo del ultimo elemento es:", type(lista[len(lista)-1]))

palabra = "Chido"
lista.append(palabra)
print(lista)
print(lista.index(nombre))
print(lista.count(sexo))
lista.extend(["perro", "gato", 999, 77, "bar777"])
print(lista)



input("\n Presiona cualquier tecla para continuar")

"""count(obejto): devuelve cuantos objetos hay en las listas.
index(objeto): devuelve en que indice esta el objeto en la lista.
append(objeto): Agrega el obhjeto a la lista hasta el final
extend(secuencia): añade una lista de datos.
insert(indice, objeto): añade el objeto a la lista en el lugar que se indica.
pop(indice): devuelve el elemento del indice establecido y lo elimina de la lista.
remove(objeto): Retira de la lista el objeto indicado, se elimna el objeto localizado en la lista."""
