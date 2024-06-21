from vehiculo import Vehiculo
from cliente import Cliente
from transaccion import Transaccion

vehiculo_manager = Vehiculo()
cliente_manager = Cliente()
transaccion_manager = Transaccion()

def mostrar_menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestionar Vehículos")
        print("2. Gestionar Clientes")
        print("3. Registrar Transacción")
        print("4. Listados")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_gestion_vehiculos()
        elif opcion == '2':
            menu_gestion_clientes()
        elif opcion == '3':
            menu_registrar_transaccion()
        elif opcion == '4':
            menu_listados()
        elif opcion == '5':
            print("Gracias por usar el sistema de gestión de concesionaria.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_gestion_vehiculos():
    while True:
        print("\n--- MENÚ GESTIÓN DE VEHÍCULOS ---")
        print("1. Agregar Vehículo")
        print("2. Eliminar Vehículo")
        print("3. Buscar Vehículo por ID")
        print("4. Buscar Vehículos por Parámetros")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_vehiculo()
        elif opcion == '2':
            eliminar_vehiculo()
        elif opcion == '3':
            buscar_vehiculo_por_id()
        elif opcion == '4':
            buscar_vehiculos_por_parametros()
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def agregar_vehiculo():
    print("\n--- AGREGAR VEHÍCULO ---")
    id_vehiculo = int(input("ID del Vehículo: "))
    patente = input("Patente: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    tipo = input("Tipo (Sedán, Hatchback, SUV, etc.): ")
    anio = int(input("Año: "))
    kilometraje = int(input("Kilometraje: "))
    precio_compra = float(input("Precio de Compra: "))
    precio_venta = float(input("Precio de Venta: "))
    estado = input("Estado (Disponible, Reservado, Vendido): ")

    vehiculo = {
        'id': id_vehiculo,
        'patente': patente,
        'marca': marca,
        'modelo': modelo,
        'tipo': tipo,
        'anio': anio,
        'kilometraje': kilometraje,
        'precio_compra': precio_compra,
        'precio_venta': precio_venta,
        'estado': estado
    }

    vehiculo_manager.agregar_vehiculo(vehiculo)
    print(f"Vehículo {marca} {modelo} agregado correctamente.")

def eliminar_vehiculo():
    print("\n--- ELIMINAR VEHÍCULO ---")
    id_vehiculo = int(input("ID del Vehículo a eliminar: "))

    vehiculo = vehiculo_manager.buscar_vehiculo_por_id(id_vehiculo)
    if vehiculo:
        vehiculo_manager.eliminar_vehiculo(id_vehiculo)
        print(f"Vehículo {vehiculo['marca']} {vehiculo['modelo']} eliminado correctamente.")
    else:
        print("Vehículo no encontrado.")

def buscar_vehiculo_por_id():
    print("\n--- BUSCAR VEHÍCULO POR ID ---")
    id_vehiculo = int(input("ID del Vehículo a buscar: "))

    vehiculo = vehiculo_manager.buscar_vehiculo_por_id(id_vehiculo)
    if vehiculo:
        print("Datos del Vehículo:")
        print(f"ID: {vehiculo['id']}")
        print(f"Patente: {vehiculo['patente']}")
        print(f"Marca: {vehiculo['marca']}")
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Tipo: {vehiculo['tipo']}")
        print(f"Año: {vehiculo['anio']}")
        print(f"Kilometraje: {vehiculo['kilometraje']}")
        print(f"Precio de Compra: {vehiculo['precio_compra']}")
        print(f"Precio de Venta: {vehiculo['precio_venta']}")
        print(f"Estado: {vehiculo['estado']}")
    else:
        print("Vehículo no encontrado.")

def buscar_vehiculos_por_parametros():
    print("\n--- BUSCAR VEHÍCULOS POR PARÁMETROS ---")
    parametros = {}
    parametros['marca'] = input("Marca del Vehículo: ")
    parametros['modelo'] = input("Modelo del Vehículo: ")

    resultados = vehiculo_manager.buscar_vehiculos_por_parametros(**parametros)
    if resultados:
        print("Resultados encontrados:")
        for vehiculo in resultados:
            print(f"ID: {vehiculo['id']} - Marca: {vehiculo['marca']} - Modelo: {vehiculo['modelo']}")
    else:
        print("No se encontraron vehículos con los parámetros especificados.")

def menu_gestion_clientes():
    while True:
        print("\n--- MENÚ GESTIÓN DE CLIENTES ---")
        print("1. Agregar Cliente")
        print("2. Eliminar Cliente")
        print("3. Buscar Cliente por ID")
        print("4. Buscar Clientes por Parámetros")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_cliente()
        elif opcion == '2':
            eliminar_cliente()
        elif opcion == '3':
            buscar_cliente_por_id()
        elif opcion == '4':
            buscar_clientes_por_parametros()
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def agregar_cliente():
    print("\n--- AGREGAR CLIENTE ---")
    id_cliente = int(input("ID del Cliente: "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo Electrónico: ")

    cliente = {
        'id': id_cliente,
        'nombre': nombre,
        'apellido': apellido,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo
    }

    cliente_manager.agregar_cliente(cliente)
    print(f"Cliente {nombre} {apellido} agregado correctamente.")

def eliminar_cliente():
    print("\n--- ELIMINAR CLIENTE ---")
    id_cliente = int(input("ID del Cliente a eliminar: "))

    cliente = cliente_manager.buscar_cliente_por_id(id_cliente)
    if cliente:
        cliente_manager.eliminar_cliente(id_cliente)
        print(f"Cliente {cliente['nombre']} {cliente['apellido']} eliminado correctamente.")
    else:
        print("Cliente no encontrado.")

def buscar_cliente_por_id():
    print("\n--- BUSCAR CLIENTE POR ID ---")
    id_cliente = int(input("ID del Cliente a buscar: "))

    cliente = cliente_manager.buscar_cliente_por_id(id_cliente)
    if cliente:
        print("Datos del Cliente:")
        print(f"ID: {cliente['id']}")
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Correo Electrónico: {cliente['correo']}")
    else:
        print("Cliente no encontrado.")

def buscar_clientes_por_parametros():
    print("\n--- BUSCAR CLIENTES POR PARÁMETROS ---")
    parametros = {}
    parametros['nombre'] = input("Nombre del Cliente: ")
    parametros['apellido'] = input("Apellido del Cliente: ")

    resultados = cliente_manager.buscar_clientes_por_parametros(**parametros)
    if resultados:
        print("Resultados encontrados:")
        for cliente in resultados:
            print(f"ID: {cliente['id']} - Nombre: {cliente['nombre']} {cliente['apellido']}")
    else:
        print("No se encontraron clientes con los parámetros especificados.")

def menu_registrar_transaccion():
    print("\n--- REGISTRAR TRANSACCIÓN ---")
    id_transaccion = len(transaccion_manager.transacciones) + 1
    id_vehiculo = int(input("ID del Vehículo involucrado en la transacción: "))
    id_cliente = int(input("ID del Cliente involucrado en la transacción: "))
    tipo = input("Tipo de Transacción (Compra/Venta): ").lower()
    monto = float(input("Monto de la Transacción: "))
    observaciones = input("Observaciones: ")

    transaccion = {
        'id': id_transaccion,
        'id_vehiculo': id_vehiculo,
        'id_cliente': id_cliente,
        'tipo': tipo,
        'monto': monto,
        'observaciones': observaciones
    }

    transaccion_manager.registrar_transaccion(transaccion)
    print("Transacción registrada correctamente.")

def menu_listados():
    while True:
        print("\n--- MENÚ LISTADOS ---")
        print("1. Listado de Compras por Cliente")
        print("2. Listado de Ventas por Cliente")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listado_compras_por_cliente()
        elif opcion == '2':
            listado_ventas_por_cliente()
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def listado_compras_por_cliente():
    print("\n--- LISTADO DE COMPRAS POR CLIENTE ---")
    id_cliente = int(input("ID del Cliente para el listado: "))

    transacciones = transaccion_manager.listar_transacciones_por_cliente(id_cliente)
    if transacciones:
        total_compras = sum(t['monto'] for t in transacciones if t['tipo'] == 'compra')
        print(f"Total de compras realizadas por el cliente: ${total_compras}")
        print("Detalle de las compras:")
        for transaccion in transacciones:
            if transaccion['tipo'] == 'compra':
                print(f"Fecha: {transaccion['fecha']} - Monto: ${transaccion['monto']} - Observaciones: {transaccion['observaciones']}")
    else:
        print("No se encontraron compras para el cliente especificado.")

def listado_ventas_por_cliente():
    print("\n--- LISTADO DE VENTAS POR CLIENTE ---")
    id_cliente = int(input("ID del Cliente para el listado: "))

    transacciones = transaccion_manager.listar_transacciones_por_cliente(id_cliente)
    if transacciones:
        total_ventas = sum(t['monto'] for t in transacciones if t['tipo'] == 'venta')
        print(f"Total de ventas realizadas por el cliente: ${total_ventas}")
        print("Detalle de las ventas:")
        for transaccion in transacciones:
            if transaccion['tipo'] == 'venta':
                print(f"Fecha: {transaccion['fecha']} - Monto: ${transaccion['monto']} - Observaciones: {transaccion['observaciones']}")
    else:
        print("No se encontraron ventas para el cliente especificado.")

if __name__ == "__main__":
    mostrar_menu_principal()
