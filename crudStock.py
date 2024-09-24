import validaciones
def crear(matriz):
    '''
    pre: recibe matriz,id de electrodomestico
    pos: devuelve matriz actualizada con el stock incrementado en 1
    '''
    id = int(input("Ingrese el ID del producto:")) 
    while not validaciones.validar_id(id):
        id = int(input("Ingrese un numero valido (1-6)"))
    for i in range(len(matriz)):        
        for j in range(len(matriz[0])):
            if id == matriz[i][j]:
                matriz[i][3] += 1
                print("Producto agregado")
    return matriz

def leer(matriz):
    '''
    pre: recibe matriz y crea una lista por comprension con nombre recortado
    pos: imprime la matriz con el texto centrado en campos
    '''
    lista = [[id,nombre[:5],precio,stock] for id,nombre,precio,stock in matriz]
    print(f'{"ID":^4} {"Nombre" :^6} {"Precio" :^8} {"stock" :^3} ')
    for id,nombre,precio,stock in lista:
        print(f'{id:^4} {nombre :^6} {precio :^8} {stock :^3} ')

def actualizar_precio(matriz):
    '''
    pre: recibe matriz por parametro pide id hasta encontrarlo
    pos: devuelve matriz con el precio actualizado
    '''
    id = int(input())
    while not validaciones.validar_id(id):
        id = int(input("Ingrese un numero valido (1-6)"))
    for i in range(len(matriz)):        
        for j in range(len(matriz[0])):
            if id == matriz[i][j]:
                matriz[i][2] = int(input("Ingrese nuevo precio: "))
                print("precio actualizado")
                return matriz
    return matriz

def eliminar(matriz):
    '''
    pre: recibe matriz por parametro pide id hasta encontrarlo
    pos: devuelve matriz con el stock decrementado en 1
    '''
    id = int(input())
    while not validaciones.validar_id(id):
        id = int(input("Ingrese un numero valido (1-6)"))
    for i in range(len(matriz)):        
        for j in range(len(matriz[0])):
            if id == matriz[i][j]:
                matriz[i][3] -= 1
                print("Producto eliminado")
    return matriz

def ordenar(matriz):
    '''
    pre: recibe matriz por parametro y crea una nueva matriz ordenada por columna 3 (precio) de manera descendente(reverse=True)
    pos: llama a la funcion leer pasandole como argumento la nueva matriz
    '''
    matriz_ordenada = sorted(matriz, key=lambda x:(x[2]),reverse=True)
    leer(matriz_ordenada)
