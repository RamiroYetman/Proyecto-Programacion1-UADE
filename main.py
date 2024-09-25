import crudStock
import crudCliente
import validaciones as v
#Programa Principal
electrodomesticos=[ 
    [1,"heladera",110000, 9],
    [2,"horno",95000,8],
    [3,"microondas",56000, 2],
    [4,"lavarropas",136000, 15],
    [5,"horno electrico",110000,12],
    [6,"secadora",123000,10]
]
clientes = {
    "37647543": {"nombre": "Juan Perez", "email": "jperez@gmail.com", "telefono": "344-657689"},
    "28453789": {"nombre": "Maria Lopez", "email": "mlopez@hotmail.com", "telefono": "341-765432"},
    "32987654": {"nombre": "Carlos Garcia", "email": "cgarcia@yahoo.com", "telefono": "342-987654"},
    "23456789": {"nombre": "Ana Martinez", "email": "amartinez@gmail.com", "telefono": "343-876543"},
    "39654321": {"nombre": "Luis Rodriguez", "email": "lrodriguez@outlook.com", "telefono": "344-234567"},
    "25678432": {"nombre": "Sofia Gonzalez", "email": "sgonzalez@hotmail.com", "telefono": "345-345678"},
}



historial_compra = []
semaforo = True
while semaforo == True:
    ingreso = int(input("1-Gestion de electrodomesticos\n2-Gestion de clientes y compras\n(-1 para salir): "))  # Administrar datos
    if ingreso == -1:
        print("Finalizando Programa...")
        semaforo = False  # Termina el programa si el usuario ingresa -1
    
    if ingreso == 1:  # Gestión de datos (stock de electrodomésticos)
        if input("contraseña: ") == "admin":  # Control de acceso
            if semaforo == True:
                # C.R.U.D de stock
                print("\n1-Ingresar un nuevo electrodomestico")
                print("2-Imprimir matriz")
                print("3-Actualizar precio")
                print("4-Eliminar electrodomestico")
                print("5-Ordenar por precio")
                print("-1 Volver al menú principal")
                opcion = int(input("Seleccione una opción: "))

                if opcion == -1:
                    semaforo = False  # Volver al menú principal
                if opcion == 1:
                    print("heladera | horno | microondas | lavarropas | horno electrico | secadora (1-6) ")
                    crudStock.crear(electrodomesticos)
                if opcion == 2:
                    crudStock.leer(electrodomesticos)
                if opcion == 3:
                    print("heladera | horno | microondas | lavarropas | horno electrico | secadora (1-6) ")
                    crudStock.actualizar_precio(electrodomesticos)
                if opcion == 4:
                    print("heladera | horno | microondas | lavarropas | horno electrico | secadora (1-6) ")
                    electrodomesticos = crudStock.eliminar(electrodomesticos)
                if opcion == 5:
                    crudStock.ordenar(electrodomesticos)
                if opcion >=6:
                    print("Opción inválida. Intente nuevamente.")

        else:
            print("Contraseña incorrecta")
            

    if ingreso == 2:  # Gestión de clientes
        while semaforo == True:
            # C.R.U.D de Clientes
            print("\n1-Nuevo cliente")
            print("2-Imprimir matriz clientes")
            print("3-Actualizar email-telefono")
            print("4-Eliminar cliente")
            print("5-Comprar producto")
            print("-1 Volver al menú principal")
            opcion_cliente = int(input("Seleccione una opción: "))

            if opcion_cliente == -1:
                semaforo = False  # Volver al menú principal
            if opcion_cliente == 1:
                crudCliente.crear(clientes)
            if opcion_cliente == 2:
                crudCliente.leer(clientes)
            if opcion_cliente == 3:
                crudCliente.actualizar_cliente(clientes)
            if opcion_cliente == 4:
                cliente = crudCliente.eliminar(clientes)
            if opcion_cliente == 5:
                dni = input("DNI (XX.XXX.XXX): ")
                while not v.validar_dni(dni):
                    dni = input("Ingrese un dni válido (XX.XXX.XXX): ")
                compra = int(input("heladera | horno | microondas | lavarropas | horno electrico | secadora (1-6): "))
                if 1 <= compra <= 6:
                    historial_compra.append([dni, compra])
            if opcion_cliente >= 6:
                print("Opción inválida. Intente nuevamente.")
        else:
            print("Opción inválida. Intente nuevamente.")




