import validaciones

def crear(diccionario):
    '''
    pre: recibe diccionario por parametro pide 4 datos y los valida
    pos: devuelve diccionario con nuevo cliente agregado
        '''
    conjunto_clientes = set(diccionario.keys())
    dni = input("DNI (XXXXXXXX): ")
    while not validaciones.validar_dni(dni) or dni in conjunto_clientes:
        if dni in conjunto_clientes:
            dni = input("DNI ya existente, ingrese un DNI distinto: ")
        else:
            dni = input("Ingrese el formato correcto(XXXXXXXX)")
    nombre = input("Nombre: ")
    email = input("Email: ")
    while not validaciones.validar_email(email):
        email = input("Ingrese un email valido")
    telefono = input("Teléfono (XXX-XXXXXX): ")
    while not validaciones.validar_telefono(telefono):
        telefono = input("Ingrese un telefono valido (XXX-XXXXXX)")
    diccionario[dni] = {"nombre": nombre, "email": email, "telefono": telefono}
    return diccionario

def leer(diccionario):
    '''
    pre: recibe diccionario por parametro, itera sobre los pares del diccionario con clave,valor
    pos: imprime el diccionario de manera centrada
    '''
    print(f'{"DNI":^12} {"Nombre":^20} {"Email":^25} {"Teléfono":^15}')
    for dni, valor in diccionario.items():
        print(f'{dni:^12} {valor["nombre"]:^15} {valor["email"]:^20} {valor["telefono"]:^15}')

def actualizar_cliente(diccionario):
    '''
    pre: pide clave DNI, si la encuentra pide otros datos
    pos: devuelve diccionario con datos actualizados
    '''
    dni = input("DNI: ")
    if dni in diccionario:
        email = input("Nuevo Email: ")
        telefono = input("Nuevo Teléfono: ")
        diccionario[dni]["email"] = email
        diccionario[dni]["telefono"] = telefono
    else:
        print("No se encontro el cliente")
    return diccionario

def eliminar(diccionario):
    '''
    pre: pide clave DNI, si la encuentra borra la linea clave-valor
    pos: devuelve diccionario actualizado
    '''
    dni = input("DNI: ")
    if dni in diccionario:
        del diccionario[dni]
        print("Cliente eliminado")
    else:
        print("No se encontro el cliente")
    return diccionario
