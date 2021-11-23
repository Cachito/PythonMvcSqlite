"""
Módulo controller.py
"""
import datetime

class Controller:
    """
    Clase Controller
    Intermediario entre la vista y el modelo.
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def refresh(self):
        """
        actualiza el connido del treeview
        """
        try:
            self.view.clean_tree()
            resultado = self.model.get_all()
            self.view.load_tree(resultado)
        except Exception as e:
            self.view.salta_violeta("Error Carro-Maier", f"error al intentar obtener noticias: {str(e)}")

    def create_data(self):
        """
        crea la base de datos carro_maier
        """
        try:
            self.model.create_data()
            self.view.salta_violeta("Carro-Maier", "Base de datos carro_meier creada con éxito")
        except Exception as e:
            self.view.salta_violeta("Error Carro-Maier", str(e))

    def create_table(self):
        """
        crea la tabla noticias
        """
        try:
            self.model.create_table()
            self.view.salta_violeta("Carro-Maier", "Tabla `Noticias` creada con éxito")

        except Exception as e:
            self.view.salta_violeta("Error Carro-Maier", str(e))

    def save_data(self, noticia):
        """
        recibe un objeto Noticia
        valida los datos en el objeto recibido
        invoca al modelo para guardar
        actualiza la vista
        limpia los campso de carga
        """
        try:
            if self.valida(noticia):
                self.model.save_data(noticia)
                self.view.salta_violeta("Carro-Maier", f"registro {'insertado' if noticia.id == '0' else f'{noticia.id} actualizado'} con éxito")
                self.refresh()
                self.view.clear_data()

        except Exception as e:
            self.view.salta_violeta("Error Carro-Maier", str(e))

    def delete_data(self, search_id):
        """
        recibe un entero
        comprueba el valor
        invoca eliminación
        actualiza la vista
        limpa lso campos
        """
        if not search_id:
            self.view.salta_violeta("Carro-Maier", "Debe seleccionar algo")
            return

        try:
            self.model.delete_data(search_id)
            self.view.salta_violeta("Carro-Maier", f"Registro id:{search_id} eliminado")
            self.refresh()
            self.view.clear_data()

        except Exception as e:
            self.view.salta_violeta("Error Carro-Maier", str(e))

    def get_datos(self, search_id):
        """
        Args:
            search_id (entero): is de la noticia a buscar
        Returns:
            Noticia: La noticia completa según el search_id recibido
        """
        if not search_id:
            self.view.salta_violeta("Carro-Maier", "Debe seleccionar algo")
            return

        try:
            return self.model.get_datos(search_id)
        except Exception as e:
            self.view.salta_violeta("Error Carro-Maier", str(e))

    def valida(self, noticia):
        """
        Args:
            noticia (Noticia): Objeto noticia a validar
        Returns:
            bool: True si todo está bien
        """
        msj_error = ""

        if not noticia.fecha:
            msj_error = " fecha "
        else:
            try:
                datetime.datetime.strptime(noticia.fecha, '%Y-%m-%d')
            except ValueError:
                msj_error = " el formato de la fecha debe ser YYYY-MM-dd"

        if not noticia.medio:
            msj_error = f"{msj_error} medio "

        if not noticia.seccion:
            msj_error = f"{msj_error} seccion "

        if not noticia.titulo:
            msj_error = f"{msj_error} título "

        if not noticia.cuerpo:
            msj_error = f"{msj_error} cuerpo "

        if msj_error:
            self.view.salta_violeta("Carro-Maier", f"debe ingresar: {msj_error}")
            return False
        else:
            return True