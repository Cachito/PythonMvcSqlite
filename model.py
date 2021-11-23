"""
Módulo model.py
"""
import re
import sqlite3

class Model:
    """
    Clase Model
    Obtiene y guarda en base de datos.
    """
    def get_all(self):
        """
        devuelve todos los registros
        de la tabla noticias
        ordenados por fecha
        """
        db_cacho = sqlite3.connect('carro_maier.db')

        csr_cacho = db_cacho.cursor()
        sql_get = """
            SELECT
                Id
                , Fecha
                , Medio
                , Seccion
                , Titulo
                , Cuerpo
            FROM Noticias
            ORDER BY Fecha DESC
            """

        csr_cacho.execute(sql_get)
        resultado = csr_cacho.fetchall()

        db_cacho.close()

        return resultado

    def create_data(self):
        """
        crea la base de datos carro_maier
        """
        try:
            db_cacho = sqlite3.connect('carro_maier.db')

        except Exception as e:
            raise Exception(f'Error al crear base de datos carro_maier: {str(e)}')

        finally:
            db_cacho.close()

    def create_table(self):
        """
        crea la tabla noticias
        si existe, la elimina
        """
        try:
            db_cacho = sqlite3.connect('carro_maier.db')

            csr_cacho = db_cacho.cursor()

            sql_drop = "DROP TABLE IF EXISTS `Noticias`"
            sql_create = """
                CREATE TABLE `Noticias`(
                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Fecha DATE,
                    Medio VARCHAR(128) COLLATE NOCASE NOT NULL,
                    Seccion VARCHAR(128) COLLATE NOCASE NOT NULL,
                    Titulo VARCHAR(128) COLLATE NOCASE NOT NULL,
                    Cuerpo TEXT COLLATE NOCASE NOT NULL
                    )
                """
            csr_cacho.execute(sql_drop)
            csr_cacho.execute(sql_create)
            db_cacho.commit()

        except Exception as e:
            db_cacho.rollback()
            raise Exception(f"error al crear tabla `Noticias`: {str(e)}")

        finally:
            db_cacho.close()

    def save_data(self, noticia):
        """
        guarda una noticia
        """
        try:
            db_cacho = sqlite3.connect('carro_maier.db')

            csr_cacho = db_cacho.cursor()

            medio = re.sub("[\"']", r"", noticia.medio)
            seccion = re.sub("[\"']", r"", noticia.seccion)
            titulo = re.sub("[\"']", r"", noticia.titulo)
            cuerpo = re.sub("[\"']", r"", noticia.cuerpo)

            if noticia.id == "0":
                sql_insert = """
                    INSERT INTO Noticias (Fecha, Medio, Seccion, Titulo, Cuerpo)
                        VALUES (?, ?, ?, ?, ?)
                    """
                datos = (noticia.fecha, medio, seccion, titulo, cuerpo)

                csr_cacho.execute(sql_insert, datos)
            else:
                sql_update = f"""
                    UPDATE Noticias SET
                        Fecha = '{noticia.fecha}',
                        Medio = '{medio}',
                        Seccion = '{seccion}',
                        Titulo = '{titulo}',
                        Cuerpo = '{cuerpo}'
                    WHERE Id = {noticia.id}
                    """
                csr_cacho.execute(sql_update)

            db_cacho.commit()

        except Exception as e:
            db_cacho.rollback()
            raise Exception(f"error al {'insertar' if noticia.id == '0' else 'actualizar'} registro en tabla Noticias: {str(e)}")

        finally:
            db_cacho.close()

    def get_datos(self, search_id):
        """
        devuelve un registro según search_id
        si lo encuentra
        """
        try:
            db_cacho = sqlite3.connect('carro_maier.db')

            csr_cacho = db_cacho.cursor()
            sql_get = f"""
                SELECT
                    Id
                    , Fecha
                    , Medio
                    , Seccion
                    , Titulo
                    , Cuerpo
                FROM Noticias
                WHERE Id = {search_id}
                """

            csr_cacho.execute(sql_get)
            resultado = csr_cacho.fetchone()

            return resultado

        except Exception as e:
            raise Exception(f"error al leer registros en tabla Noticias: {str(e)}")

        finally:
            db_cacho.close()


    def delete_data(self, search_id):
        """
        elimina un registro según search_id
        si lo encuentra
        """
        try:
            db_cacho = sqlite3.connect('carro_maier.db')

            csr_cacho = db_cacho.cursor()
            sql_delete = f"""
                DELETE FROM Noticias
                WHERE Id = {search_id}
                """
            csr_cacho.execute(sql_delete)
            db_cacho.commit()

        except Exception as e:
            db_cacho.rollback()
            raise Exception(f"error al eliminar registro en tabla Noticias: {str(e)}")

        finally:
            db_cacho.close()
