


class Cliente:

    def __init__(self, nombre_completo,cedula,codigo_ingresado,datetime
                 ):
        self.codigo_ingresado = codigo_ingresado
        self.nombre_completo = nombre_completo
        self.cedula = cedula
        self.datetime = datetime

    def __str__(self):
        return f"Nombre: {self.nombre_completo} Documento: {self.cedula}"
