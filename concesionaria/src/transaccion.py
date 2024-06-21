import json
from datetime import datetime

class Transaccion:
    def __init__(self, datafile='data/transacciones.json'):
        self.datafile = datafile
        self.transacciones = self.load_data()

    def load_data(self):
        try:
            with open(self.datafile, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.datafile, 'w', encoding='utf-8') as file:
            json.dump(self.transacciones, file, indent=4)

    def registrar_transaccion(self, transaccion):
        transaccion['id'] = len(self.transacciones) + 1
        transaccion['fecha'] = datetime.now().isoformat()
        self.transacciones.append(transaccion)
        self.save_data()

    def listar_transacciones_por_cliente(self, id_cliente):
        return [t for t in self.transacciones if t['id_cliente'] == id_cliente]

    def listar_transacciones_por_vehiculo(self, id_vehiculo):
        return [t for t in self.transacciones if t['id_vehiculo'] == id_vehiculo]

    def listar_transacciones_por_rango_fechas(self, fecha_inicio, fecha_fin):
        fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        return [t for t in self.transacciones if fecha_inicio <= datetime.fromisoformat(t['fecha']) <= fecha_fin]
