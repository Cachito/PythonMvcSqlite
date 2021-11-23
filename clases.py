"""
módulo de clases.
"""
class Noticia:
    """
    clase Noticia.
    """
    def __init__(self, id, fecha, medio, seccion, titulo, cuerpo):
        self.id = id
        self.fecha = fecha
        self.medio = medio
        self.seccion = seccion
        self.titulo = titulo
        self.cuerpo = cuerpo
