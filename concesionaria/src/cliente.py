import json

class Cliente:
    def __init__(self, datafile='data/clientes.json'):
        self.datafile = datafile
        self.clientes = self.load_data()

    def load_data(self):
        try:
            with open(self.datafile, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.datafile, 'w', encoding='utf-8') as file:
            json.dump(self.clientes, file, indent=4)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.save_data()

    def eliminar_cliente(self, id_cliente):
        self.clientes = [c for c in self.clientes if c['id'] != id_cliente]
        self.save_data()

    def buscar_cliente_por_id(self, id_cliente):
        for cliente in self.clientes:
            if cliente['id'] == id_cliente:
                return cliente
        return None

    def buscar_clientes_por_parametros(self, **kwargs):
        resultados = []
        for cliente in self.clientes:
            match = all(cliente.get(key) == value for key, value in kwargs.items())
            if match:
                resultados.append(cliente)
        return resultados
