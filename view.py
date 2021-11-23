"""
Módulo view.py
"""
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from clases import Noticia

class View(ttk.Frame):
    """
    Clase View
    Interfaz de usuario.
    Interactúa con Controller.
    """
    def __init__(self, parent):
        super().__init__(parent)

        # Defino variables por defecto
        self.id = tk.StringVar()
        self.fecha = tk.StringVar()
        self.medio = tk.StringVar()
        self.seccion = tk.StringVar()
        self.titulo = tk.StringVar()
        self.cuerpo = tk.StringVar()
        #self.archivo = tk.StringVar()
        self.busqueda = tk.StringVar()

        self.my_parent = parent
        self.my_parent.geometry("500x600")
        self.my_parent.title("Carga de Noticias")
        self.my_parent.iconbitmap("./imagenes/noticias.ico")

        self.frm_contenedor = ttk.Frame(self.my_parent, height=600, borderwidth=1)

        # controles: guardar
        self.frm_controles = ttk.Frame(master=self.frm_contenedor, height=40, borderwidth=1, relief=tk.RAISED)

        self.img_db = tk.PhotoImage(file = r"./imagenes/iconDb.png")
        self.btn_db = tk.Button(master=self.frm_controles, text="Base de Detos", image=self.img_db, width=30, command=self.create_data)
        self.btn_db.place(x=15, y=2)

        self.img_table = tk.PhotoImage(file=r"./imagenes/iconTable.png")
        self.btn_table = tk.Button(master=self.frm_controles, text="Tabla", image=self.img_table, width=30, command=self.create_table)
        self.btn_table.place(x=50, y=2)

        self.img_nuevo = tk.PhotoImage(file=r"./imagenes/iconNew.png")
        self.btn_nuevo = tk.Button(master=self.frm_controles, text="Nuevo", image=self.img_nuevo, width=30, command=self.clear_data)
        self.btn_nuevo.place(x=85, y=2)

        self.img_guardar = tk.PhotoImage(file=r"./imagenes/iconSave.png")
        self.btn_guardar = tk.Button(master=self.frm_controles, text="Guardar", image=self.img_guardar, width=30, command=self.save_data)
        self.btn_guardar.place(x=120, y=2)

        self.img_borrar = tk.PhotoImage(file = r"./imagenes/iconDelete.png")
        self.btn_borrar = tk.Button(master=self.frm_controles, text="Eliminar", image=self.img_borrar, width=30, command=self.delete_data)
        self.btn_borrar.place(x=155, y=2)

        self.img_refresh = tk.PhotoImage(file=r"./imagenes/iconRefresh.png")
        self.btn_refresh = ttk.Button(master=self.frm_controles, text="Actualizar", image=self.img_refresh, width=30, command=self.refresh)
        self.btn_refresh.place(x=190, y=2)

        self.ent_busqueda = tk.Entry(master=self.frm_controles, textvariable=self.busqueda, width=3)
        self.ent_busqueda.place(x=235, y=7)

        self.img_buscar = tk.PhotoImage(file=r"./imagenes/iconSearch.png")
        self.btn_buscar = tk.Button(master=self.frm_controles, text="Buscar", image=self.img_buscar, width=30, command=self.buscar)
        self.btn_buscar.place(x=260, y=2)

        self.frm_controles.pack(side=tk.TOP, expand=tk.NO, fill=tk.X) #place(x=5,y=400)

        self.frm_datos = tk.Frame(master=self.frm_contenedor, height=300, borderwidth=1, relief=tk.SOLID)

        self.lbl_fecha=tk.Label(master=self.frm_datos, text="Fecha", width=50, anchor=tk.W)
        self.lbl_fecha.place(x=5, y=5)
        self.ent_fecha=tk.Entry(master=self.frm_datos, textvariable=self.fecha, width=50)
        self.ent_fecha.place(x=60, y=5)

        self.lbl_medio=tk.Label(master=self.frm_datos, text="Medio", width=50, anchor=tk.W)
        self.lbl_medio.place(x=5, y=35)
        self.ent_medio=tk.Entry(master=self.frm_datos, textvariable=self.medio, width=50)
        self.ent_medio.place(x=60, y=35)

        self.lbl_seccion=tk.Label(master=self.frm_datos, text="Sección", width=50, anchor=tk.W)
        self.lbl_seccion.place(x=5, y=65)
        self.ent_seccion=tk.Entry(master=self.frm_datos, textvariable=self.seccion, width=50)
        self.ent_seccion.place(x=60, y=65)

        self.lbl_titulo=tk.Label(master=self.frm_datos, text="Título", width=50, anchor=tk.W)
        self.lbl_titulo.place(x=5, y=95)
        self.ent_titulo=tk.Entry(master=self.frm_datos, textvariable=self.titulo, width=50)
        self.ent_titulo.place(x=60, y=95)

        self.lbl_cuerpo=tk.Label(master=self.frm_datos, text="Cuerpo", width=50, anchor=tk.W)
        self.lbl_cuerpo.place(x=5, y=125)
        self.ent_cuerpo=tk.Text(master=self.frm_datos, width=50, height=10)
        self.ent_cuerpo.place(x=60, y=125)

        self.frm_datos.pack(side=tk.TOP, expand=tk.NO, fill=tk.X) #place(x=5,y=400)

        self.frm_grilla = ttk.Frame(master=self.frm_contenedor, height=100, borderwidth=1, relief=tk.RAISED)
        self.tree = ttk.Treeview(master=self.frm_grilla)
        self.tree["columns"] = ("Fecha", "Medio", "Seccion", "Titulo")
        self.tree.column("#0", width=50, minwidth=50, anchor=tk.W)
        self.tree.column("Fecha", width=80, minwidth=80)
        self.tree.column("Medio", width=80, minwidth=80)
        self.tree.column("Seccion", width=80, minwidth=80)
        self.tree.column("Titulo", width=100, minwidth=100)
        self.tree.heading('#0', text='', anchor=tk.CENTER)
        self.tree.heading('Fecha', text='Fecha', anchor=tk.CENTER)
        self.tree.heading('Medio', text='Medio', anchor=tk.CENTER)
        self.tree.heading('Seccion', text='Sección', anchor=tk.CENTER)
        self.tree.heading('Titulo', text='Título', anchor=tk.CENTER)
        self.tree.place(x=5, y=5)
        self.tree.bind("<Double-1>", self.on_double_click)

        self.frm_grilla.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH) #place(x=5,y=400)

        self.frm_contenedor.pack(expand=tk.YES, fill=tk.BOTH)

        self.menu_bar = tk.Menu(parent)
        self.menu_archivo = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Acerca de..", command=self.about)
        self.menu_archivo.add_command(label="Salir", command=self.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.menu_archivo)

        parent.config(menu=self.menu_bar)

        self.controller = None

    def about(self):
        """
        dialogo about
        """
        self.salta_violeta("Patrón MVC", "Cargador de Noticias\n\nGrupo:\n- Luis Carro\n- Cristian Maier")

    def set_controller(self, controller):
        """
        Establece la referencia al controller
        """
        self.controller = controller

    def clean_tree(self):
        """
        vacía el treeview
        """
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

    def load_tree(self, resultado):
        """
        carga el treeview
        """
        for fila in resultado:
            self.tree.insert('', 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))

    def on_double_click(self, event):
        """
        evento doble click en treeview
        """
        if self.controller:
            cur_item = self.tree.item(self.tree.focus())
            noti = self.controller.get_datos(cur_item["text"])
            self.clear_data()

            if noti is None:
                self.salta_violeta("Carro-Maier", f"registro com id {cur_item} no encontrado")
            else:
                self.id = noti[0]
                self.fecha = noti[1]
                self.medio = noti[2]
                self.seccion = noti[3]
                self.titulo = noti[4]

                self.ent_fecha.insert(0, noti[1])
                self.ent_medio.insert(0, noti[2])
                self.ent_seccion.insert(0, noti[3])
                self.ent_titulo.insert(0, noti[4])
                self.ent_cuerpo.insert("1.0", noti[5])

    def refresh(self):
        """
        botón refresh evento click
        """
        if self.controller:
            self.controller.refresh()

    def create_data(self):
        """
        botón crear base evento click
        """
        if self.controller:
            self.controller.create_data()

    def create_table(self):
        """
        botón crear tabla evento click
        """
        if self.controller:
            self.controller.create_table()

    def clear_data(self):
        """
        limpia los controles en la vista
        """
        self.id = "0"
        self.fecha = ""
        self.medio = ""
        self.seccion = ""
        self.titulo = ""
        self.cuerpo = ""
        #self.archivo = ""
        self.cuerpo = ""
        self.busqueda = ""

        self.ent_fecha.delete(0, tk.END)
        self.ent_medio.delete(0, tk.END)
        self.ent_seccion.delete(0, tk.END)
        self.ent_titulo.delete(0, tk.END)
        #self.ent_archivo.delete(0, tk.END)
        self.ent_cuerpo.delete("1.0", tk.END)
        self.ent_fecha.delete(0, tk.END)
        self.ent_busqueda.delete(0, tk.END)

    def save_data(self):
        """
        guarda un registro
        """
        if self.controller:
            noti = Noticia(self.id, self.ent_fecha.get(), self.ent_medio.get(), self.ent_seccion.get(), self.ent_titulo.get(), self.ent_cuerpo.get("1.0", tk.END))
            self.controller.save_data(noti)

    def delete_data(self):
        """
        elimina un registro
        """
        if self.controller:
            self.controller.delete_data(self.id)

    def buscar(self):
        """
        busca según id
        """
        if self.controller:
            search_id = self.ent_busqueda.get()
            noti = self.controller.get_datos(search_id)
            self.clear_data()

            if noti is None:
                self.salta_violeta("Carro-Maier", f"registro com id {search_id} no encontrado")
            else:
                self.id = noti[0]
                self.fecha = noti[1]
                self.medio = noti[2]
                self.seccion = noti[3]
                self.titulo = noti[4]

                self.ent_fecha.insert(0, noti[1])
                self.ent_medio.insert(0, noti[2])
                self.ent_seccion.insert(0, noti[3])
                self.ent_titulo.insert(0, noti[4])
                self.ent_cuerpo.insert("1.0", noti[5])

    def salta_violeta(self, titulo, texto):
        """
        muestra un diálogo
        """
        msg.showinfo(titulo, texto)
