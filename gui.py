import tkinter as tk
from tkinter import ttk, messagebox
import logic
from datetime import datetime

class ConcesionariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Concesionaria de Autos")
        
        # Creamos los widgets de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.tab_vehiculos = ttk.Frame(self.notebook)
        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_transacciones = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_vehiculos, text='Vehículos')
        self.notebook.add(self.tab_clientes, text='Clientes')
        self.notebook.add(self.tab_transacciones, text='Transacciones')

        # Sección de Vehículos
        ttk.Label(self.tab_vehiculos, text="Gestión de Vehículos").pack(pady=10)
        self.create_vehiculos_section()

        # Sección de Clientes
        ttk.Label(self.tab_clientes, text="Gestión de Clientes").pack(pady=10)
        self.create_clientes_section()

        # Sección de Transacciones
        ttk.Label(self.tab_transacciones, text="Gestión de Transacciones").pack(pady=10)
        self.create_transacciones_section()

    def create_vehiculos_section(self):
        frame = ttk.Frame(self.tab_vehiculos)
        frame.pack(pady=10)

        self.vehiculos_tree = ttk.Treeview(frame, columns=("ID", "Patente", "Marca", "Modelo", "Tipo", "Año", "Kilometraje", "Estado", "Precio Compra", "Precio Venta"), show='headings')
        self.vehiculos_tree.heading("ID", text="ID")
        self.vehiculos_tree.heading("Patente", text="Patente")
        self.vehiculos_tree.heading("Marca", text="Marca")
        self.vehiculos_tree.heading("Modelo", text="Modelo")
        self.vehiculos_tree.heading("Tipo", text="Tipo")
        self.vehiculos_tree.heading("Año", text="Año")
        self.vehiculos_tree.heading("Kilometraje", text="Kilometraje")
        self.vehiculos_tree.heading("Estado", text="Estado")
        self.vehiculos_tree.heading("Precio Compra", text="Precio Compra")
        self.vehiculos_tree.heading("Precio Venta", text="Precio Venta")
        self.vehiculos_tree.pack()

        self.load_vehiculos()

        frame_form = ttk.Frame(self.tab_vehiculos)
        frame_form.pack(pady=10)

        ttk.Label(frame_form, text="Patente:").pack()
        self.entry_patente = ttk.Entry(frame_form)
        self.entry_patente.pack()

        ttk.Label(frame_form, text="Marca:").pack()
        self.entry_marca = ttk.Entry(frame_form)
        self.entry_marca.pack()

        ttk.Label(frame_form, text="Modelo:").pack()
        self.entry_modelo = ttk.Entry(frame_form)
        self.entry_modelo.pack()

        ttk.Label(frame_form, text="Tipo:").pack()
        self.entry_tipo = ttk.Entry(frame_form)
        self.entry_tipo.pack()

        ttk.Label(frame_form, text="Año:").pack()
        self.entry_año = ttk.Entry(frame_form)
        self.entry_año.pack()

        ttk.Label(frame_form, text="Kilometraje:").pack()
        self.entry_kilometraje = ttk.Entry(frame_form)
        self.entry_kilometraje.pack()

        ttk.Label(frame_form, text="Precio Compra:").pack()
        self.entry_precio_compra = ttk.Entry(frame_form)
        self.entry_precio_compra.pack()

        ttk.Label(frame_form, text="Precio Venta:").pack()
        self.entry_precio_venta = ttk.Entry(frame_form)
        self.entry_precio_venta.pack()

        ttk.Label(frame_form, text="Estado:").pack()
        self.entry_estado = ttk.Entry(frame_form)
        self.entry_estado.pack()

        self.btn_add_vehiculo = ttk.Button(frame_form, text="Agregar Vehículo", command=self.add_vehiculo)
        self.btn_add_vehiculo.pack()

        self.btn_edit_vehiculo = ttk.Button(frame_form, text="Editar Vehículo", command=self.edit_vehiculo)
        self.btn_edit_vehiculo.pack()

        self.btn_delete_vehiculo = ttk.Button(frame_form, text="Eliminar Vehículo", command=self.delete_vehiculo)
        self.btn_delete_vehiculo.pack()


    def create_clientes_section(self):
        frame = ttk.Frame(self.tab_clientes)
        frame.pack(pady=10)

        self.clientes_tree = ttk.Treeview(frame, columns=("ID", "Documento", "Nombre", "Apellido", "Teléfono", "Direccion", "Mail"), show='headings')
        self.clientes_tree.heading("ID", text="ID")
        self.clientes_tree.heading("Documento", text="Documento")
        self.clientes_tree.heading("Nombre", text="Nombre")
        self.clientes_tree.heading("Apellido", text="Apellido")
        self.clientes_tree.heading("Teléfono", text="Teléfono")
        self.clientes_tree.heading("Direccion", text="Direccion")
        self.clientes_tree.heading("Mail", text="Mail")
        self.clientes_tree.pack()

        self.load_clientes()

        frame_form = ttk.Frame(self.tab_clientes)
        frame_form.pack(pady=10)

        ttk.Label(frame_form, text="DNI:").grid(row=0, column=0)
        self.entry_dni = ttk.Entry(frame_form)
        self.entry_dni.grid(row=0, column=1)

        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre = ttk.Entry(frame_form)
        self.entry_nombre.grid(row=1, column=1)

        ttk.Label(frame_form, text="Apellido:").grid(row=2, column=0)
        self.entry_apellido = ttk.Entry(frame_form)
        self.entry_apellido.grid(row=2, column=1)

        ttk.Label(frame_form, text="Teléfono:").grid(row=3, column=0)
        self.entry_telefono = ttk.Entry(frame_form)
        self.entry_telefono.grid(row=3, column=1)

        ttk.Label(frame_form, text="Direccion:").grid(row=4, column=0)
        self.entry_direccion = ttk.Entry(frame_form)
        self.entry_direccion.grid(row=4, column=1)

        ttk.Label(frame_form, text="Mail:").grid(row=5, column=0)
        self.entry_mail = ttk.Entry(frame_form)
        self.entry_mail.grid(row=5, column=1)

        self.btn_add_cliente = ttk.Button(frame_form, text="Agregar Cliente", command=self.add_cliente)
        self.btn_add_cliente.grid(row=6, columnspan=2)

        self.btn_edit_cliente = ttk.Button(frame_form, text="Editar Cliente", command=self.edit_cliente)
        self.btn_edit_cliente.grid(row=7, columnspan=2)

        self.btn_delete_cliente = ttk.Button(frame_form, text="Eliminar Cliente", command=self.delete_cliente)
        self.btn_delete_cliente.grid(row=8, columnspan=2)


    def create_transacciones_section(self):
        frame = ttk.Frame(self.tab_transacciones)
        frame.pack(pady=10)

        ttk.Label(frame, text="Tipo:").grid(row=0, column=0)
        self.entry_tipo = ttk.Combobox(frame, values=["Compra", "Venta"])
        self.entry_tipo.grid(row=0, column=1)

        ttk.Label(frame, text="Cliente ID:").grid(row=1, column=0)
        self.entry_id_cliente = ttk.Entry(frame)
        self.entry_id_cliente.grid(row=1, column=1)

        ttk.Label(frame, text="Vehículo ID:").grid(row=2, column=0)
        self.entry_id_vehiculo = ttk.Entry(frame)
        self.entry_id_vehiculo.grid(row=2, column=1)

        ttk.Label(frame, text="Fecha (YYYY-MM-DD):").grid(row=3, column=0)
        self.entry_fecha = ttk.Entry(frame)
        self.entry_fecha.grid(row=3, column=1)

        ttk.Label(frame, text="Monto:").grid(row=4, column=0)
        self.entry_monto = ttk.Entry(frame)
        self.entry_monto.grid(row=4, column=1)

        ttk.Label(frame, text="Observaciones:").grid(row=5, column=0)
        self.entry_observaciones = ttk.Entry(frame)
        self.entry_observaciones.grid(row=5, column=1)

        self.btn_add_transaccion = ttk.Button(frame, text="Registrar Transacción", command=self.add_transaccion)
        self.btn_add_transaccion.grid(row=6, columnspan=2)

    def add_vehiculo(self):
        vehiculo = {
            "id": len(logic.listar_vehiculos()) + 1,
            "patente": self.entry_patente.get(),
            "marca": self.entry_marca.get(),
            "modelo": self.entry_modelo.get(),
            "tipo": self.entry_tipo.get(),
            "año": self.entry_año.get(),
            "kilometraje": self.entry_kilometraje.get(),
            "estado": self.entry_estado.get(),
            "precio_compra": float(self.entry_precio_compra.get()),
            "precio_venta": float(self.entry_precio_venta.get())
        }
        logic.crear_vehiculo(vehiculo)
        messagebox.showinfo("Éxito", "Vehículo agregado correctamente")
        self.load_vehiculos()

    def edit_vehiculo(self):
        id_vehiculo = int(self.entry_vehiculo_id.get())
        nuevos_datos = {
            "patente": self.entry_patente.get(),
            "marca": self.entry_marca.get(),
            "modelo": self.entry_modelo.get(),
            "tipo": self.entry_tipo.get(),
            "año": self.entry_año.get(),
            "kilometraje": self.entry_kilometraje.get(),
            "estado": self.entry_estado.get(),
            "precio_compra": float(self.entry_precio_compra.get()),
            "precio_venta": float(self.entry_precio_venta.get())
        }
        logic.editar_vehiculo(id_vehiculo, nuevos_datos)
        messagebox.showinfo("Éxito", "Vehículo editado correctamente")
        self.load_vehiculos()

    def delete_vehiculo(self):
        id_vehiculo = int(self.entry_vehiculo_id.get())
        logic.eliminar_vehiculo(id_vehiculo)
        messagebox.showinfo("Éxito", "Vehículo eliminado correctamente")
        self.load_vehiculos()

    def add_cliente(self):
        cliente = {
            "id": len(logic.listar_clientes()) + 1,
            "documento": self.entry_dni.get(),
            "nombre": self.entry_nombre.get(),
            "apellido": self.entry_apellido.get(),
            "telefono": self.entry_telefono.get(),
            "Direccion": self.entry_direccion.get(),
            "Mail": self.entry_mail.get()
        }
        logic.crear_cliente(cliente)
        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        self.load_clientes()

    def edit_cliente(self):
        id_cliente = int(self.entry_cliente_id.get())
        nuevos_datos = {
            "id": len(logic.listar_clientes()) + 1,
            "documento": self.entry_dni.get(),
            "nombre": self.entry_nombre.get(),
            "apellido": self.entry_apellido.get(),
            "telefono": self.entry_telefono.get(),
            "Direccion": self.entry_direccion.get(),
            "Mail": self.entry_mail.get()
        }
        logic.editar_cliente(id_cliente, nuevos_datos)
        messagebox.showinfo("Éxito", "Cliente editado correctamente")
        self.load_clientes()

    def delete_cliente(self):
        id_cliente = int(self.entry_cliente_id.get())
        logic.eliminar_cliente(id_cliente)
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
        self.load_clientes()

    def add_transaccion(self):
        transaccion = {
            "id": len(logic.load_data('data/transacciones.json')) + 1,
            "tipo": self.entry_tipo.get(),
            "cliente_id": int(self.entry_cliente_id.get()),
            "vehiculo_id": int(self.entry_vehiculo_id.get()),
            "fecha": self.entry_fecha.get(),
            "Monto": self.entry_monto.get(),
            "observaciones": self.entry_observaciones.get()
        }
        logic.registrar_transaccion(transaccion)
        messagebox.showinfo("Éxito", "Transacción registrada correctamente")

    def load_vehiculos(self):
        for row in self.vehiculos_tree.get_children():
            self.vehiculos_tree.delete(row)
        for vehiculo in logic.listar_vehiculos():
            self.vehiculos_tree.insert('', 'end', values=(vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], vehiculo['modelo'], vehiculo['precio_compra'], vehiculo['precio_venta']))

    def load_clientes(self):
        for row in self.clientes_tree.get_children():
            self.clientes_tree.delete(row)
        for cliente in logic.listar_clientes():
            self.clientes_tree.insert('', 'end', values=(cliente['id_cliente'], cliente['documento'], cliente['nombre'], cliente['apellido'], cliente['telefono']))

if __name__ == "__main__":
    root = tk.Tk()
    app = ConcesionariaApp(root)
    root.mainloop()