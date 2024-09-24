def eliminar (diccionario):
    cont = 0
    for claves in diccionario.keys():
        diccionario.pop(claves)
        cont += 1
    return diccionario,cont
cliente = {"nombre" : "Ramiro", "apellido" : "Yetman", "edad": "22"}
resultado, contado = eliminar(cliente)
print (resultado, contado)