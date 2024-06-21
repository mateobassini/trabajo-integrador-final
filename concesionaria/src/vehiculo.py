import json

class Vehiculo:
    def __init__(self, datafile='data/vehiculos.json'):
        self.datafile = datafile
        self.vehiculos = self.load_data()

    def load_data(self):
        try:
            with open(self.datafile, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.datafile, 'w', encoding='utf-8') as file:
            json.dump(self.vehiculos, file, indent=4)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        self.save_data()

    def eliminar_vehiculo(self, id_vehiculo):
        self.vehiculos = [v for v in self.vehiculos if v['id'] != id_vehiculo]
        self.save_data()

    def buscar_vehiculo_por_id(self, id_vehiculo):
        for vehiculo in self.vehiculos:
            if vehiculo['id'] == id_vehiculo:
                return vehiculo
        return None

    def buscar_vehiculos_por_parametros(self, **kwargs):
        resultados = []
        for vehiculo in self.vehiculos:
            match = all(vehiculo.get(key) == value for key, value in kwargs.items())
            if match:
                resultados.append(vehiculo)
        return resultados
