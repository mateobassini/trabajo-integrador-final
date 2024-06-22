import json
import os
from datetime import datetime

# Definimos las rutas a los archivos JSON
DATA_DIR = 'data'
CLIENTES_FILE = os.path.join(DATA_DIR, 'clientes.json')
VEHICULOS_FILE = os.path.join(DATA_DIR, 'vehiculos.json')
TRANSACCIONES_FILE = os.path.join(DATA_DIR, 'transacciones.json')

# Función para cargar datos desde un archivo JSON
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Función para guardar datos en un archivo JSON
def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Funciones para manejar clientes
def crear_cliente(cliente):
    clientes = load_data(CLIENTES_FILE)
    clientes.append(cliente)
    save_data(CLIENTES_FILE, clientes)

def editar_cliente(cliente_id, nuevos_datos):
    clientes = load_data(CLIENTES_FILE)
    for cliente in clientes:
        if cliente['id'] == cliente_id:
            cliente.update(nuevos_datos)
            break
    save_data(CLIENTES_FILE, clientes)

def eliminar_cliente(cliente_id):
    clientes = load_data(CLIENTES_FILE)
    clientes = [cliente for cliente in clientes if cliente['id'] != cliente_id]
    save_data(CLIENTES_FILE, clientes)

# Funciones para manejar vehículos
def crear_vehiculo(vehiculo):
    vehiculos = load_data(VEHICULOS_FILE)
    vehiculos.append(vehiculo)
    save_data(VEHICULOS_FILE, vehiculos)

def editar_vehiculo(vehiculo_id, nuevos_datos):
    vehiculos = load_data(VEHICULOS_FILE)
    for vehiculo in vehiculos:
        if vehiculo['id'] == vehiculo_id:
            vehiculo.update(nuevos_datos)
            break
    save_data(VEHICULOS_FILE, vehiculos)

def eliminar_vehiculo(vehiculo_id):
    vehiculos = load_data(VEHICULOS_FILE)
    vehiculos = [vehiculo for vehiculo in vehiculos if vehiculo['id'] != vehiculo_id]
    save_data(VEHICULOS_FILE, vehiculos)

# Funciones para manejar transacciones
def registrar_transaccion(transaccion):
    transacciones = load_data(TRANSACCIONES_FILE)
    transacciones.append(transaccion)
    save_data(TRANSACCIONES_FILE, transacciones)

def obtener_transacciones_por_cliente(cliente_id, tipo=None):
    transacciones = load_data(TRANSACCIONES_FILE)
    if tipo:
        return [t for t in transacciones if t['cliente_id'] == cliente_id and t['tipo'] == tipo]
    return [t for t in transacciones if t['cliente_id'] == cliente_id]

def obtener_transacciones_por_vehiculo(vehiculo_id, tipo=None):
    transacciones = load_data(TRANSACCIONES_FILE)
    if tipo:
        return [t for t in transacciones if t['vehiculo_id'] == vehiculo_id and t['tipo'] == tipo]
    return [t for t in transacciones if t['vehiculo_id'] == vehiculo_id]

def obtener_transacciones_por_fecha(fecha_inicio, fecha_fin, tipo=None):
    transacciones = load_data(TRANSACCIONES_FILE)
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
    if tipo:
        return [t for t in transacciones if fecha_inicio <= datetime.strptime(t['fecha'], '%Y-%m-%d') <= fecha_fin and t['tipo'] == tipo]
    return [t for t in transacciones if fecha_inicio <= datetime.strptime(t['fecha'], '%Y-%m-%d') <= fecha_fin]

# Funciones de búsqueda
def buscar_cliente_por_documento(documento):
    clientes = load_data(CLIENTES_FILE)
    return [cliente for cliente in clientes if cliente['documento'] == documento]

def buscar_vehiculo_por_patente(patente):
    vehiculos = load_data(VEHICULOS_FILE)
    return [vehiculo for vehiculo in vehiculos if vehiculo['patente'] == patente]

# Funciones de listado
def listar_clientes():
    return load_data(CLIENTES_FILE)

def listar_vehiculos():
    return load_data(VEHICULOS_FILE)




