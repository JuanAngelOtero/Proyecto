import datetime
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from cliente import Cliente
from pedidos import Pedidos
from PyQt5 import QtCore


class Ventana(QMainWindow):
    saldo = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DISFRUTA')
        self.resize(1000, 800)

        # Agregamos un fondo de color verde claro a la ventana
        self.setStyleSheet('background-color: #E0F2F1;')

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/Logo - DisFruta.jpg'))

        # Agregamos la imagen a la ventana
        label_imagen = QLabel(self)
        pixmap = QPixmap('imagenes/Logo - DisFruta.jpg')
        pixmap = pixmap.scaledToWidth(150)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen.setPixmap(pixmap)
        label_imagen.move(5, 5)

        # Dentro del método donde creas la ventana existente
        self.background_image = QPixmap("imagenes/disfrutaPPIfonts.png")
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.background_image)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setScaledContents(True)


        # Agregamos el letrero de bienvenida
        label_bienvenida = QLabel('BIENVENIDO A DISFRUTA', self)
        label_bienvenida.setStyleSheet('background-color: #B0F2C2; color: black;')
        label_bienvenida.setFont(QFont('Times New Roman', 16))
        label_bienvenida.adjustSize()

        # Colocamos el letrero en el medio de la ventana en la parte superior
        label_bienvenida.setAlignment(Qt.AlignCenter)
        label_bienvenida.setGeometry(140, 0, self.width(), 50)

        # ----- BOTONES PRINCIPALES ------


        #  Botón VERDURA
        boton_verduras = QPushButton('FRUTAS Y VERDURAS', self)
        boton_verduras.setGeometry(250, 300, 250, 100)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_verduras.setCursor(Qt.PointingHandCursor)
        boton_verduras.setStyleSheet('background-color: #FAFCAF;')
        boton_verduras.clicked.connect(self.abrir_ventana_verduras)

        # botón CARRITO
        boton_carrito = QPushButton('CARRITO', self)
        boton_carrito.setGeometry(600, 300, 250, 100)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_carrito.setCursor(Qt.PointingHandCursor)
        boton_carrito.setStyleSheet('background-color: #FFE1AE;')
        boton_carrito.clicked.connect(self.abrir_ventana_carrito)

        # ---- BOTON---- "Personal Autorizado"
        boton_personal = QPushButton('PERSONAL AUTORIZADO', self)
        boton_personal.setGeometry(750, 730, 230, 50)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_personal.setCursor(Qt.PointingHandCursor)
        boton_personal.setStyleSheet('background-color: #B0F2C2;')
        boton_personal.clicked.connect(self.abrir_ventana_personal)


    def abrir_ventana_verduras(self):
        self.hide()  # Ocultamos la ventana actual
        ventana_verduras = QDialog(self)
        ventana_verduras.setWindowTitle('VERDURA')
        ventana_verduras.resize(1400, 800)
        ventana_verduras.setStyleSheet('background-color: white;')

        # Creamos un QLabel con el mensaje "Bienvenido"
        mensaje_bienvenida = QLabel('BIENVENIDO AL CATÁLOGO DE FRUTAS Y VERDURAS', ventana_verduras)
        mensaje_bienvenida.setGeometry(0, 0, 200, 50)
        mensaje_bienvenida.setStyleSheet('background-color: #B0F2C2; color: black;')
        mensaje_bienvenida.setAlignment(Qt.AlignCenter)
        mensaje_bienvenida.setFont(QFont('Times New Roman', 12))

        def __init__(self):
            self.productos_seleccionados = []  # Lista para almacenar los productos seleccionados

        # CAR IMAGEN PRODUCT
        # producto APIO
        label_imagen = QLabel('', ventana_verduras)
        label_imagen.setGeometry(50, 50, 200, 200)
        pixmap = QPixmap('imagenes/verdura1.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen.setPixmap(pixmap)

        nombre_producto = QLabel('Apio 700 GR: \n$4.100', ventana_verduras)
        nombre_producto.setGeometry(50, 200, 250, 80)
        nombre_producto.setFont(QFont('Times New Roman', 10))
        self.check_apio = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_apio.move(50, 270)
        self.check_apio.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_apio.setCursor(Qt.PointingHandCursor)
        self.valor_apio = 4100
        #self.check_apio.toggled.connect(self.mostrar_nombre_precios_apio)
        self.check_apio.toggled.connect(self.agregar_al_carrito_apio)

        # producto Cilantro verdura2
        label_imagen2 = QLabel('', ventana_verduras)
        label_imagen2.setGeometry(320, 50, 200, 200)
        pixmap = QPixmap('imagenes/verdura2.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen2.setPixmap(pixmap)

        nombre_producto2 = QLabel('Cilantro 100 GR: \n$1.000', ventana_verduras)
        nombre_producto2.setGeometry(320, 200, 250, 80)
        nombre_producto2.setFont(QFont('Times New Roman', 10))
        self.check_cilantro = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_cilantro.move(320, 270)
        self.check_cilantro.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_cilantro.setCursor(Qt.PointingHandCursor)
        self.valor_cilantro = 1000
        #self.check_cilantro.toggled.connect(self.mostrar_nombre_precios_cilantro)
        self.check_cilantro.toggled.connect(self.agregar_al_carrito_cilantro)

        # producto CEBOLLA JUNCA VERDURA3
        label_imagen3 = QLabel('', ventana_verduras)
        label_imagen3.setGeometry(550, 50, 200, 200)
        pixmap = QPixmap('imagenes/verdura3.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen3.setPixmap(pixmap)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox

        nombre_producto3 = QLabel('Cebolla Junca 500 GR: \n$5.100', ventana_verduras)
        nombre_producto3.setGeometry(550, 200, 250, 80)
        nombre_producto3.setFont(QFont('Times New Roman', 10))
        self.check_cebolla = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_cebolla.move(550, 270)
        self.check_cebolla.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_cebolla.setCursor(Qt.PointingHandCursor)
        self.valor_cebolla = 5100
        #self.check_cebolla.toggled.connect(self.mostrar_nombre_precios_cebolla)
        self.check_cebolla.toggled.connect(self.agregar_al_carrito_cebolla)

        label_imagen4 = QLabel('', ventana_verduras)
        label_imagen4.setGeometry(800, 50, 200, 200)
        pixmap = QPixmap('imagenes/fruta4.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen4.setPixmap(pixmap)

        nombre_producto4 = QLabel('Pera 1 und: \n$1.700', ventana_verduras)
        nombre_producto4.setGeometry(800, 200, 250, 80)
        nombre_producto4.setFont(QFont('Times New Roman', 10))
        self.check_pera = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_pera.move(800, 270)
        self.check_pera.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_pera.setCursor(Qt.PointingHandCursor)
        self.valor_pera = 1700
        #self.check_pera.toggled.connect(self.mostrar_nombre_precios_pera)
        self.check_pera.toggled.connect(self.agregar_al_carrito_pera)

        # producto Cabolla blanca verdura5
        label_imagen5 = QLabel('', ventana_verduras)
        label_imagen5.setGeometry(50, 320, 200, 200)
        pixmap = QPixmap('imagenes/verdura5.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen5.setPixmap(pixmap)

        nombre_producto5 = QLabel('Cebolla Blanca 1 und: \n$1.100', ventana_verduras)
        nombre_producto5.setGeometry(50, 450, 250, 80)
        nombre_producto5.setFont(QFont('Times New Roman', 10))
        self.check_ceboBlanca = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_ceboBlanca.move(50, 520)
        self.check_ceboBlanca.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_ceboBlanca.setCursor(Qt.PointingHandCursor)
        self.valor_ceboBlanca = 1100
        #self.check_ceboBlanca.toggled.connect(self.mostrar_nombre_precios_cebollaBlanca)
        self.check_ceboBlanca.toggled.connect(self.agregar_al_carrito_ceboBlanca)

        # producto cabolla roja Verdura6
        label_imagen6 = QLabel('', ventana_verduras)
        label_imagen6.setGeometry(320, 300, 200, 200)
        pixmap = QPixmap('imagenes/verdura6.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen6.setPixmap(pixmap)

        nombre_producto6 = QLabel('Cebolla Roja 1 und: \n$700', ventana_verduras)
        nombre_producto6.setGeometry(320, 450, 250, 80)
        nombre_producto6.setFont(QFont('Times New Roman', 10))
        self.check_ceboRoja = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_ceboRoja.move(320, 520)
        self.check_ceboRoja.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_ceboRoja.setCursor(Qt.PointingHandCursor)
        self.valor_ceboRoja = 700
        #self.check_ceboRoja.toggled.connect(self.mostrar_nombre_precios_cebollaRoja)
        self.check_ceboRoja.toggled.connect(self.agregar_al_carrito_ceboRoja)

        # producto verengena VERDURA7
        label_imagen7 = QLabel('', ventana_verduras)
        label_imagen7.setGeometry(550, 300, 200, 200)
        pixmap = QPixmap('imagenes/verdura7.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen7.setPixmap(pixmap)

        nombre_producto7 = QLabel('Berenjena 1 und: \n$2.200', ventana_verduras)
        nombre_producto7.setGeometry(550, 450, 250, 80)
        nombre_producto7.setFont(QFont('Times New Roman', 10))
        self.check_verengena = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_verengena.move(550, 520)
        self.check_verengena.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_verengena.setCursor(Qt.PointingHandCursor)
        self.valor_veregena = 2200
        #self.check_verengena.toggled.connect(self.mostrar_nombre_precios_verengena)
        self.check_verengena.toggled.connect(self.agregar_al_carrito_verengena)

        # producto Manzana FRUTA8
        label_imagen8 = QLabel('', ventana_verduras)
        label_imagen8.setGeometry(800, 300, 200, 200)
        pixmap = QPixmap('imagenes/fruta8.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen8.setPixmap(pixmap)

        nombre_producto8 = QLabel('Manzana 1 und: \n$1.700', ventana_verduras)
        nombre_producto8.setGeometry(800, 450, 250, 80)
        nombre_producto8.setFont(QFont('Times New Roman', 10))
        self.check_manzana = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_manzana.move(800, 520)
        self.check_manzana.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_manzana.setCursor(Qt.PointingHandCursor)
        self.valor_manzana = 1700
       # self.check_manzana.toggled.connect(self.mostrar_nombre_precios_manzana)
        self.check_manzana.toggled.connect(self.agregar_al_carrito_manzana)

        # producto sandia fruta 9
        label_imagen9 = QLabel('', ventana_verduras)
        label_imagen9.setGeometry(1000, 300, 250, 200)
        pixmap = QPixmap('imagenes/fruta2.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen9.setPixmap(pixmap)

        nombre_producto9 = QLabel('Sandia 1 und: \n$13.500', ventana_verduras)
        nombre_producto9.setGeometry(1000, 450, 250, 80)
        nombre_producto9.setFont(QFont('Times New Roman', 10))
        self.check_sandia = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_sandia.move(1000, 520)
        self.check_sandia.resize(1000, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_sandia.setCursor(Qt.PointingHandCursor)
        self.valor_sandia = 13500


        #self.check_sandia.toggled.connect(self.mostrar_nombre_precios_sandia)
        self.check_sandia.toggled.connect(self.agregar_al_carrito_sandia)

        # producto Papaya FRUTA7
        label_imagen10 = QLabel('', ventana_verduras)
        label_imagen10.setGeometry(1000, 100, 300, 80)
        pixmap = QPixmap('imagenes/fruta7.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen10.setPixmap(pixmap)

        nombre_producto10 = QLabel('Papaya 1 und: \n$4.300', ventana_verduras)
        nombre_producto10.setGeometry(1000, 200, 300, 80)
        nombre_producto10.setFont(QFont('Times New Roman', 10))
        self.check_papaya = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_papaya.move(1000, 270)
        self.check_papaya.resize(1000, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_papaya.setCursor(Qt.PointingHandCursor)
        self.valor_papaya = 4300

        #self.check_papaya.toggled.connect(self.mostrar_nombre_precios_papaya)
        self.check_papaya.toggled.connect(self.agregar_al_carrito_papaya)

        # producto piña FRUTA 11
        label_imagen11 = QLabel('', ventana_verduras)
        label_imagen11.setGeometry(1200, 50, 200, 200)
        pixmap = QPixmap('imagenes/fruta3.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen11.setPixmap(pixmap)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox

        nombre_producto11 = QLabel('Piña 1 und: \n$6.500', ventana_verduras)
        nombre_producto11.setGeometry(1200, 200, 250, 80)
        nombre_producto11.setFont(QFont('Times New Roman', 10))
        self.check_pina = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_pina.move(1200, 270)
        self.check_pina.resize(1200, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_pina.setCursor(Qt.PointingHandCursor)
        self.valor_pina = 6500
        #self.check_pina.toggled.connect(self.mostrar_nombre_precios_pina)
        self.check_pina.toggled.connect(self.agregar_al_carrito_pina)

        # producto mango FRUTA6
        label_imagen6 = QLabel('', ventana_verduras)
        label_imagen6.setGeometry(1200, 300, 200, 200)
        pixmap = QPixmap('imagenes/fruta6.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen6.setPixmap(pixmap)

        nombre_producto6 = QLabel('Mango 1 und: \n$1.800', ventana_verduras)
        nombre_producto6.setGeometry(1200, 450, 250, 80)
        nombre_producto6.setFont(QFont('Times New Roman', 10))
        self.check_mango = QCheckBox("Añadir al carrito", ventana_verduras)
        self.check_mango.move(1200, 520)
        self.check_mango.resize(1200, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        self.check_mango.setCursor(Qt.PointingHandCursor)
        self.valor_mango = 1800
        #self.check_mango.toggled.connect(self.mostrar_nombre_precios_mango)
        self.check_mango.toggled.connect(self.agregar_al_carrito_mango)




        # Añadimos los QLabel a la ventana de frutas
        layout = QVBoxLayout()
        layout.addWidget(mensaje_bienvenida)
        layout.addStretch()
        layout.addStretch()
        layout.setAlignment(Qt.AlignCenter)
        ventana_verduras.setLayout(layout)

        self.nombre1 = ("")
        self.nombre2 = ("")
        self.nombre3 = ("")
        self.nombre4 = ("")
        self.nombre5 = ("")
        self.nombre6 = ("")
        self.nombre7 = ("")
        self.nombre8 = ("")
        self.nombre9 = ("")
        self.nombre10 = ("")
        self.nombre11 = ("")
        self.nombre12 = ("")



        self.boton_enviar_carrito = QPushButton("Enviar al carrito", ventana_verduras)
        self.boton_enviar_carrito.setGeometry(10, 750, 200, 40)
        self.boton_enviar_carrito.setStyleSheet('background-color: #FAFCAF;')
        self.boton_enviar_carrito.clicked.connect(self.enviar_al_carrito)

        # Creamos el botón para volver a la ventana principal
        boton_volver = QPushButton('Volver', ventana_verduras)
        boton_volver.setGeometry(110, 150, 100, 30)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_volver.setCursor(Qt.PointingHandCursor)
        boton_volver.setStyleSheet('background-color: #FAFCAF;')
        boton_volver.move(ventana_verduras.width() - boton_volver.width() - 10,
                          ventana_verduras.height() - boton_volver.height() - 10)
        boton_volver.clicked.connect(lambda: (ventana_verduras.close(), self.show()))
        '''
        self.mensaje_precio9 = QLabel('', ventana_verduras)
        self.mensaje_precio9.setGeometry(1100, 50, 200, 50)
        self.mensaje_precio9.setFont(QFont('Times New Roman', 10))

        self.mensaje_precio10 = QLabel('', ventana_verduras)
        self.mensaje_precio10.setGeometry(1100, 90, 200, 50)
        self.mensaje_precio10.setFont(QFont('Times New Roman', 10))

        self.mensaje_precio11 = QLabel('', ventana_verduras)
        self.mensaje_precio11.setGeometry(1100, 130, 300, 50)
        self.mensaje_precio11.setFont(QFont('Times New Roman', 10))

        self.mensaje_precio12 = QLabel('', ventana_verduras)
        self.mensaje_precio12.setGeometry(1100, 170, 300, 50)
        self.mensaje_precio12.setFont(QFont('Times New Roman', 10))

        self.mensaje_precio13 = QLabel('', ventana_verduras)
        self.mensaje_precio13.setGeometry(1100, 210, 300, 50)
        self.mensaje_precio13.setFont(QFont('Times New Roman', 10))

        self.mensaje_precio14 = QLabel('', ventana_verduras)
        self.mensaje_precio14.setGeometry(1100, 250, 300, 50)
        self.mensaje_precio14.setFont(QFont('Times New Roman', 10))

        self.mensaje_precio15 = QLabel('', ventana_verduras)
        self.mensaje_precio15.setGeometry(1100, 290, 300, 50)
        self.mensaje_precio15.setFont(QFont('Times New Roman', 10))

        self.mensaje_precio16 = QLabel('', ventana_verduras)
        self.mensaje_precio16.setGeometry(1100, 330, 300, 50)
        self.mensaje_precio16.setFont(QFont('Times New Roman', 10))
        '''

        self.labeltitulo = QLabel("saldo: " + str(self.saldo), ventana_verduras)
        self.labeltitulo.setGeometry(5, 700, 400, 30)
        self.labeltitulo.setAlignment(Qt.AlignCenter)
        self.labeltitulo.setFont(QFont('Times New Roman', 12))

        ventana_verduras.exec_()

    def abrir_ventana_carrito(self):

        self.hide()  # Ocultamos la ventana actual
        self.ventana_carrito = QDialog(self)
        self.ventana_carrito.setWindowTitle('CARRITO')
        self.ventana_carrito.resize(1000, 800)
        self.ventana_carrito.setStyleSheet('background-color: #FFF8DC;')  # Establece el color de fondo café con leche

        # Dentro del método donde creas la ventana existente
        # Crear una etiqueta para el fondo



        # Creamos un QLabel con el mensaje "Bienvenido"
        mensaje_bienvenida = QLabel('PRODUCTOS AGREGADOS', self.ventana_carrito)
        mensaje_bienvenida.setGeometry(0, 0, 200, 50)
        mensaje_bienvenida.setStyleSheet('background-color: #B0F2C2; color: black;')
        mensaje_bienvenida.setAlignment(Qt.AlignCenter)
        mensaje_bienvenida.setFont(QFont('Times New Roman', 12))



        # Añadimos el QLabel a la ventana de frutas
        layout = QVBoxLayout()
        layout.addWidget(mensaje_bienvenida)
        layout.addStretch()
        self.ventana_carrito.setLayout(layout)



        # Creamos el botón para volver a la ventana principal
        boton_volver = QPushButton('Volver', self.ventana_carrito)
        boton_volver.setGeometry(110, 150, 100, 30)
        boton_volver.setStyleSheet('background-color: #FFE1AE;')
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_volver.setCursor(Qt.PointingHandCursor)
        boton_volver.move(self.ventana_carrito.width() - boton_volver.width() - 10,
                          self.ventana_carrito.height() - boton_volver.height() - 10)

        boton_volver.clicked.connect(lambda: (self.ventana_carrito.close(), self.show()))



        # abrimos el archivo  en modo binario
        self.file = open('datos/pedidos.txt', 'rb')

        # creamos una lista vacia
        pedidos = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            pd = Pedidos(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
                lista[11],
                lista[12],
            )
            # Metemos el objeto en la lista usuario
            pedidos.append(pd)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        for pd in pedidos:

            mensaje_nombre1 = QLabel(pd.nombre1, self.ventana_carrito)
            mensaje_nombre1.setGeometry(300, 100, 200, 50)
            mensaje_nombre1.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre1.setFixedWidth(400)
            mensaje_nombre1.setFont(QFont('Times New Roman', 12))

            mensaje_nombre2 = QLabel(pd.nombre2, self.ventana_carrito)
            mensaje_nombre2.setGeometry(300, 150, 200, 50)
            mensaje_nombre2.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre2.setFixedWidth(400)
            mensaje_nombre2.setFont(QFont('Times New Roman', 12))

            mensaje_nombre3 = QLabel(pd.nombre3, self.ventana_carrito)
            mensaje_nombre3.setGeometry(300, 200, 200, 50)
            mensaje_nombre3.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre3.setFixedWidth(400)
            mensaje_nombre3.setFont(QFont('Times New Roman', 12))

            mensaje_nombre4 = QLabel(pd.nombre4, self.ventana_carrito)
            mensaje_nombre4.setGeometry(300, 250, 200, 50)
            mensaje_nombre4.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre4.setFixedWidth(400)
            mensaje_nombre4.setFont(QFont('Times New Roman', 12))

            mensaje_nombre5 = QLabel(pd.nombre5, self.ventana_carrito)
            mensaje_nombre5.setGeometry(300, 300, 200, 50)
            mensaje_nombre5.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre5.setFixedWidth(400)
            mensaje_nombre5.setFont(QFont('Times New Roman', 12))

            mensaje_nombre6 = QLabel(pd.nombre6, self.ventana_carrito)
            mensaje_nombre6.setGeometry(300, 350, 200, 50)
            mensaje_nombre6.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre6.setFixedWidth(400)
            mensaje_nombre6.setFont(QFont('Times New Roman', 12))

            mensaje_nombre7 = QLabel(pd.nombre7, self.ventana_carrito)
            mensaje_nombre7.setGeometry(300, 400, 200, 50)
            mensaje_nombre7.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre7.setFixedWidth(400)
            mensaje_nombre7.setFont(QFont('Times New Roman', 12))

            mensaje_nombre8 = QLabel(pd.nombre8, self.ventana_carrito)
            mensaje_nombre8.setGeometry(300, 450, 200, 50)
            mensaje_nombre8.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre8.setFixedWidth(400)
            mensaje_nombre8.setFont(QFont('Times New Roman', 12))

            mensaje_nombre9 = QLabel(pd.nombre9, self.ventana_carrito)
            mensaje_nombre9.setGeometry(300, 500, 200, 50)
            mensaje_nombre9.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre9.setFixedWidth(400)
            mensaje_nombre9.setFont(QFont('Times New Roman', 12))

            mensaje_nombre10 = QLabel(pd.nombre10, self.ventana_carrito)
            mensaje_nombre10.setGeometry(300, 550, 200, 50)
            mensaje_nombre10.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre10.setFixedWidth(400)
            mensaje_nombre10.setFont(QFont('Times New Roman', 12))

            mensaje_nombre11 = QLabel(pd.nombre11, self.ventana_carrito)
            mensaje_nombre11.setGeometry(300, 600, 200, 50)
            mensaje_nombre11.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre11.setFixedWidth(400)
            mensaje_nombre11.setFont(QFont('Times New Roman', 12))

            mensaje_nombre12 = QLabel(pd.nombre12, self.ventana_carrito)
            mensaje_nombre12.setGeometry(300, 650, 200, 50)
            mensaje_nombre12.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_nombre12.setFixedWidth(400)
            mensaje_nombre12.setFont(QFont('Times New Roman', 12))

            mensaje_saldo = QLabel(pd.saldo, self.ventana_carrito)
            mensaje_saldo.setGeometry(300, 700, 200, 50)
            mensaje_saldo.setStyleSheet('background-color: #FFFFFF; color: black;')
            mensaje_saldo.setFixedWidth(400)
            mensaje_saldo.setFont(QFont('Times New Roman', 12))

        self.ventana_carrito.exec_()






    # --- METODOS DE LAS FRUTAS ------
    def abrir_ventana_personal(self):
        self.hide()  # Ocultamos la ventana actual
        self.ventana_personal = QDialog(self)
        self.ventana_personal.setWindowTitle('PERSONAL AUTORIZADO')
        self.ventana_personal.resize(1000, 800)

        # Cargar la imagen de fondo
        background_image = QPixmap("imagenes/fondo personal.png")

        # Crear una etiqueta para mostrar la imagen de fondo
        background_label = QLabel(self.ventana_personal)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 1000, 800)
        background_label.lower()

        # Creamos los campos de texto para ingresar el nombre completo y la cédula
        nombre_label = QLabel('NOMBRE COMPLETO*: ', self.ventana_personal)
        nombre_label.setGeometry(110, 100, 250, 30)

        nombre_texto = QLineEdit(self.ventana_personal)
        nombre_texto.setGeometry(280, 100, 150, 30)

        cedula_label = QLabel('CÉDULA*: ', self.ventana_personal)
        cedula_label.setGeometry(110, 145, 250, 30)

        cedula_texto = QLineEdit(self.ventana_personal)
        cedula_texto.setGeometry(280, 145, 150, 30)

        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(500)

        # Le escribimos el texto
        self.letrero2.setText("Por favor, si eres personal autorizado."
                              "\nIngresa correctamente tu nombre, cédula y código."
                              "\n\nLos campos marcados con asterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de texto y margenes:
        self.letrero2.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Añadimos los QLabel a la ventana de frutas
        layout = QVBoxLayout()
        layout.addWidget(self.letrero2)
        layout.addWidget(nombre_label)
        layout.addWidget(nombre_texto)
        layout.addWidget(cedula_label)
        layout.addWidget(cedula_texto)
        layout.addStretch()
        layout.addStretch()
        layout.setAlignment(Qt.AlignCenter)

        self.ventana_personal.setLayout(layout)

        # Creamos el campo de texto para ingresar el código
        codigo_label = QLabel('INGRESÉ EL CÓDIGO*: ', self.ventana_personal)
        codigo_label.setGeometry(20, 320, 250, 30)

        codigo_texto = QLineEdit(self.ventana_personal)
        codigo_texto.setGeometry(18, 350, 150, 30)
        codigo_texto.setEchoMode(QLineEdit.Password)

        # Creamos el botón para verificar el código y abrir la otra ventana
        boton_verificar = QPushButton('INGRESAR', self.ventana_personal)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_verificar.setCursor(Qt.PointingHandCursor)
        boton_verificar.setGeometry(400, 370, 100, 30)
        boton_verificar.setStyleSheet('background-color:  #B0F2C2;')

        # Creamos el botón para verificar el código y abrir la otra ventana
        boton_informacion = QPushButton('INFORMACIÓN', self.ventana_personal)
        boton_informacion.setGeometry(5, 760, 150, 30)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_informacion.setCursor(Qt.PointingHandCursor)
        boton_informacion.setStyleSheet('background-color: #B0F2C2;')
        boton_informacion.clicked.connect(self.abrir_ventaInformacion)


        def abrir_ventana_otra():
            ventana_otra = QDialog(self)
            ventana_otra.setWindowTitle('PERSONAL AUTORIZADO')
            ventana_otra.resize(1000, 800)
            ventana_otra.setStyleSheet('background-color: #FFFFE0;')  # Establece un color de fondo amarillo muy claro

            # Creamos un QLabel con el mensaje "Bienvenido"
            mensaje_bienvenida = QLabel('PEDIDO DEL CLIENTE', ventana_otra)
            mensaje_bienvenida.setGeometry(0, 0, 200, 50)
            mensaje_bienvenida.setStyleSheet('background-color: #B0F2C2; color: black;')
            mensaje_bienvenida.setAlignment(Qt.AlignCenter)
            mensaje_bienvenida.setFont(QFont('Times New Roman', 12))

            # Añadimos los QLabel a la ventana de frutas
            layout = QVBoxLayout()
            layout.addWidget(mensaje_bienvenida)
            layout.addStretch()
            layout.addStretch()
            layout.setAlignment(Qt.AlignCenter)
            ventana_otra.setLayout(layout)

            # Creamos el botón para volver a la ventana principal
            boton_volver = QPushButton('Volver', ventana_otra)
            boton_volver.setGeometry(110, 150, 80, 30)
            # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
            boton_volver.setCursor(Qt.PointingHandCursor)
            boton_volver.setStyleSheet('background-color: #FFE1AE;')
            boton_volver.move(ventana_otra.width() - boton_volver.width() - 10,
                              ventana_otra.height() - boton_volver.height() - 10)

            boton_volver.clicked.connect(lambda: (ventana_otra.close(), self.show()))

            # abrimos el archivo  en modo binario
            self.file = open('datos/pedidos.txt', 'rb')

            # creamos una lista vacia
            pedidos = []

            while self.file:
                # lea el archivo y traiga los datos
                linea = self.file.readline().decode('UTF-8')

                # elimine el ; y ponga en una posicion
                lista = linea.split(";")

                # se para si ya no hay mas registros
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                pd = Pedidos(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                    lista[11],
                    lista[12],
                )
                # Metemos el objeto en la lista usuario
                pedidos.append(pd)

            self.file.close()

            # En este punto tenemos la lista de usuario con todos los usuarios

            for pd in pedidos:
                mensaje_nombre1 = QLabel(pd.nombre1,ventana_otra)
                mensaje_nombre1.setGeometry(300, 100, 200, 50)
                mensaje_nombre1.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre1.setFixedWidth(400)
                mensaje_nombre1.setFont(QFont('Times New Roman', 12))

                mensaje_nombre2 = QLabel(pd.nombre2,ventana_otra)
                mensaje_nombre2.setGeometry(300, 150, 200, 50)
                mensaje_nombre2.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre2.setFixedWidth(400)
                mensaje_nombre2.setFont(QFont('Times New Roman', 12))

                mensaje_nombre3 = QLabel(pd.nombre3,ventana_otra)
                mensaje_nombre3.setGeometry(300, 200, 200, 50)
                mensaje_nombre3.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre3.setFixedWidth(400)
                mensaje_nombre3.setFont(QFont('Times New Roman', 12))

                mensaje_nombre4 = QLabel(pd.nombre4,ventana_otra)
                mensaje_nombre4.setGeometry(300, 250, 200, 50)
                mensaje_nombre4.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre4.setFixedWidth(400)
                mensaje_nombre4.setFont(QFont('Times New Roman', 12))

                mensaje_nombre5 = QLabel(pd.nombre5,ventana_otra)
                mensaje_nombre5.setGeometry(300, 300, 200, 50)
                mensaje_nombre5.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre5.setFixedWidth(400)
                mensaje_nombre5.setFont(QFont('Times New Roman', 12))

                mensaje_nombre6 = QLabel(pd.nombre6,ventana_otra)
                mensaje_nombre6.setGeometry(300, 350, 200, 50)
                mensaje_nombre6.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre6.setFixedWidth(400)
                mensaje_nombre6.setFont(QFont('Times New Roman', 12))

                mensaje_nombre7 = QLabel(pd.nombre7,ventana_otra)
                mensaje_nombre7.setGeometry(300, 400, 200, 50)
                mensaje_nombre7.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre7.setFixedWidth(400)
                mensaje_nombre7.setFont(QFont('Times New Roman', 12))

                mensaje_nombre8 = QLabel(pd.nombre8,ventana_otra)
                mensaje_nombre8.setGeometry(300, 450, 200, 50)
                mensaje_nombre8.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre8.setFixedWidth(400)
                mensaje_nombre8.setFont(QFont('Times New Roman', 12))

                mensaje_nombre9 = QLabel(pd.nombre9,ventana_otra)
                mensaje_nombre9.setGeometry(300, 500, 200, 50)
                mensaje_nombre9.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre9.setFixedWidth(400)
                mensaje_nombre9.setFont(QFont('Times New Roman', 12))

                mensaje_nombre10 = QLabel(pd.nombre10,ventana_otra)
                mensaje_nombre10.setGeometry(300, 550, 200, 50)
                mensaje_nombre10.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre10.setFixedWidth(400)
                mensaje_nombre10.setFont(QFont('Times New Roman', 12))

                mensaje_nombre11 = QLabel(pd.nombre11,ventana_otra)
                mensaje_nombre11.setGeometry(300, 600, 200, 50)
                mensaje_nombre11.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre11.setFixedWidth(400)
                mensaje_nombre11.setFont(QFont('Times New Roman', 12))

                mensaje_nombre12 = QLabel(pd.nombre12,ventana_otra)
                mensaje_nombre12.setGeometry(300, 650, 200, 50)
                mensaje_nombre12.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_nombre12.setFixedWidth(400)
                mensaje_nombre12.setFont(QFont('Times New Roman', 12))

                mensaje_saldo = QLabel(pd.saldo,ventana_otra)
                mensaje_saldo.setGeometry(300, 700, 200, 50)
                mensaje_saldo.setStyleSheet('background-color: #B0F2C2; color: black;')
                mensaje_saldo.setFixedWidth(400)
                mensaje_saldo.setFont(QFont('Times New Roman', 12))

            ventana_otra.exec_()

        def verificar_codigo():
            codigo_ingresado = codigo_texto.text()
            nombre_completo = nombre_texto.text()
            cedula = cedula_texto.text()

            # Variable de control de datos correctos
            datos_correctos = True

            # Verificar que todos los campos estén completos
            if not codigo_ingresado or not nombre_completo or not cedula:
                QMessageBox.warning(self.ventana_personal, 'Error', 'Por favor, ingrese todos los campos.')
                datos_correctos = False

            # Verificar que la cédula sea un número
            if not cedula.isnumeric():
                QMessageBox.warning(self.ventana_personal, 'Error',
                                    'Por favor, ingrese solo números en el campo de la cédula.')
                datos_correctos = False

            if datos_correctos:
                if codigo_ingresado == 'disfrutappi':
                    abrir_ventana_otra()
                    self.ventana_personal.close()
                    self.show()
                else:
                    QMessageBox.warning(self.ventana_personal, 'Error', 'Código incorrecto')
                    datos_correctos = False

            # si los datos están correctos:
            if datos_correctos:
                # Abrimos el archivo en modo agregar escribiendo datos en binario.
                file = open('datos/clientes.txt', 'ab')

                # Obtener la fecha actual del sistema
                fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')

                # Traer el texto de los QLineEdit() y los agrega concatenándonos.
                # Para escribirlos en el archivo en formato binario utf-8
                file.write(bytes(nombre_completo + ";" + cedula + ";" + codigo_ingresado + ";" + fecha_actual + "\n",
                                 encoding='UTF-8'))

                # Cerramos el archivo:
                file.close()

                # Abrimos en modo lectura en formato bytes
                file = open('datos/clientes.txt', 'rb')
                # Recorrer el archivo línea por línea:
                for linea in file:
                    linea_decodificada = linea.decode('UTF-8')
                    print(linea_decodificada)
                file.close()

            else:
                QMessageBox.warning(self.ventana_personal, 'Error', 'Por favor, corrija los datos ingresados.')

        boton_verificar.clicked.connect(verificar_codigo)


        # Creamos el botón para volver a la ventana principal
        boton_volver = QPushButton('Volver', self.ventana_personal)
        boton_volver.setGeometry(110, 150, 80, 30)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_volver.setCursor(Qt.PointingHandCursor)
        boton_volver.setStyleSheet('background-color:  #B0F2C2;')
        boton_volver.move(self.ventana_personal.width() - boton_volver.width() - 10,
                          self.ventana_personal.height() - boton_volver.height() - 10)

        boton_volver.clicked.connect(lambda: (self.ventana_personal.close(), self.show()))


        self.ventana_personal.exec_()

    def abrir_ventaInformacion(self):
        # Ocultamos la ventana actual
        self.ventana_personal.close()



        ventana_informacion = QDialog(self)
        ventana_informacion.setWindowTitle('INFORMACIÓN DE REGISTRO')
        ventana_informacion.resize(1500, 700)  # Tamaño personalizado para que todos los elementos sean visibles
        ventana_informacion.setStyleSheet('background-color: white;')

        # abrimos el archivo en modo de lectura:
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacia para guardar todos los usuarios:
        self.usuarios = []

        # recorremos el archivo línea por línea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # Obtenemos del string una lista con datos separados por ;

            lista = linea.split(";")
            # se para sí ya no hay más registros en el archivo
            if linea == '':
                break
            # Creamos un objeto de tipo cliente llamdo u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],

            )
            # Metemos el objeto en la lista de ususarios:
            self.usuarios.append(u)

        # Cerramos el archivo:
        self.file.close()

        # En este punto ya tenmos la lista usuarios con todos los ususarios:

        # obtenemos el número de ususarios registrados:
        # consultamos el tamaño de la lista usuarios:
        self.numeroUsuarios = len(self.usuarios)


        # contador de elementos para controlar los usuarios en la lista usuarios.
        self.contador = 0

        # Establecemos la distribución de los elementos en layout vertical:
        self.vertical = QVBoxLayout()

        # ---- CONSTRUIR EL MENÚ TOOLBAR ---
        toolbar = QToolBar('Main toolbar')
        toolbar.setIconSize(QSize(64, 64))
        self.addToolBar(toolbar)

        # Agrega los botones al menú de la barra de herramientas
        # Ejemplo de botón de eliminación
        delete = QAction(QIcon('imagenes/delete.jpeg'), '&Delete', self)
        delete.triggered.connect(self.accion_delete)
        toolbar.addAction(delete)

        # Ejemplo de botón de adición
        add = QAction(QIcon('imagenes/add.jpeg'), '&Add', self)
        add.triggered.connect(self.accion_add)
        toolbar.addAction(add)

        # Ejemplo de botón de inserción
        insert = QAction(QIcon('imagenes/edit.jpeg'), '&Insert', self)
        insert.triggered.connect(self.accion_insert)
        toolbar.addAction(insert)
        # ----FIN MENÚ TOOLBAR -----

        self.vertical.addWidget(toolbar)


        # Establecemos la distribución de los elementos en layout vertical:
        layout = QVBoxLayout()

        # Hacemos el letrero:
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("PERSONAL AUTORIZADO QUE HA INGRESADO")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Times New Roman", 20))

        # le ponemos color de texto y margenes:
        self.letrero1.setStyleSheet("color: #000080")

        # Agregamos el letrero en la primera fila:
        self.vertical.addWidget(self.letrero1)

        # Ponemos un espacio después:
        self.vertical.addStretch()

        # Creamos un scroll:
        self.scrollArea = QScrollArea()

        # Hacemos que el scroll se adapte a diferentes tamaños:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una tabla:
        self.tabla = QTableWidget()

        # Definimos el número de columnas que tendrá la tabla:
        self.tabla.setColumnCount(4)

        # Definimos el ancho de cada columna:
        self.tabla.setColumnWidth(0, 300)
        self.tabla.setColumnWidth(1, 300)
        self.tabla.setColumnWidth(2, 300)
        self.tabla.setColumnWidth(3, 300)

        # Definimos el texto de la cabecera de la tabla:
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Documento',
                                              'Codigo',
                                              'Fecha', ])

        # Establecemos el número de filas:
        self.tabla.setRowCount(self.numeroUsuarios)

        # Llenamos la tabla:
        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombre_completo))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.cedula))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.codigo_ingresado))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.datetime))
            self.contador += 1

        # Metemos la tabla en el scroll:
        self.scrollArea.setWidget(self.tabla)

        # Métodos en el layout vertical el scroll:
        self.vertical.addWidget(self.scrollArea)

        # ponemos un espacio despues:
        self.vertical.addStretch()

        # Creamos el botón para volver a la ventana principal
        boton_volver = QPushButton('Volver', ventana_informacion)
        boton_volver.setGeometry(110, 150, 80, 30)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_volver.setCursor(Qt.PointingHandCursor)
        boton_volver.setStyleSheet('background-color:  #B0F2C2;')
        boton_volver.move(ventana_informacion.width() - boton_volver.width() - 10,
                          ventana_informacion.height() - boton_volver.height() - 10)

        boton_volver.clicked.connect(lambda: (ventana_informacion.close(), self.show()))

        # Establecemos el layout vertical como el layout principal de la ventana:
        ventana_informacion.setLayout(self.vertical)

        ventana_informacion.exec_()

    def agregar_al_carrito(self):
        if self.check_fresa.isChecked():
            self.saldo = self.saldo + self.valor_fresa
        else:
            self.saldo = self.saldo - self.valor_fresa
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))
    def agregar_al_carrito_sandia(self):
        if self.check_sandia.isChecked():
            self.saldo = self.saldo + self.valor_sandia
            self.nombre11 = ("Sandia 1 und: $13.500")
        else:
            self.nombre11 = ("")
            self.saldo = self.saldo - self.valor_sandia
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_pina(self):
        if self.check_pina.isChecked():
            self.saldo = self.saldo + self.valor_pina
            self.nombre5 = ("Piña 1 und: $6.500")
        else:
            self.nombre5 = ("")
            self.saldo = self.saldo - self.valor_pina
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_pera(self):
        if self.check_pera.isChecked():
            self.saldo = self.saldo + self.valor_pera
            self.nombre3 = ("Pera 1 und: $1.700")
        else:
            self.nombre3 = ("")
            self.saldo = self.saldo - self.valor_pera
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    # Metodos Frutas
    def agregar_al_carrito_uva(self):
        if self.check_uva.isChecked():
            self.saldo = self.saldo + self.valor_uva
        else:
            self.saldo = self.saldo - self.valor_uva
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_mango(self):
        if self.check_mango.isChecked():
            self.saldo = self.saldo + self.valor_mango
            self.nombre12 = ("Mango 1 und: $1.800")
        else:
            self.nombre12 = ("")
            self.saldo = self.saldo - self.valor_mango
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))


    def agregar_al_carrito_papaya(self):
        if self.check_papaya.isChecked():
            self.saldo = self.saldo + self.valor_papaya
            self.nombre4 = ("Papaya 1 und: $4.300")
        else:
            self.nombre4 = ("")
            self.saldo = self.saldo - self.valor_papaya
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_manzana(self):
        if self.check_manzana.isChecked():
            self.saldo = self.saldo + self.valor_manzana
            self.nombre10 = ("Manzana 1 und: $1.700")
        else:
            self.nombre10 = ("")
            self.saldo = self.saldo - self.valor_manzana
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    #---- MEETODOS DE LAS VERDURAS ------
    def agregar_al_carrito_apio(self):
        if self.check_apio.isChecked():
            self.saldo = self.saldo + self.valor_apio
            self.nombre1 = ("Apio 700 GR: $4.100")
        else:
            self.nombre1 = ("")
            self.saldo = self.saldo - self.valor_apio
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_cilantro(self):
        if self.check_cilantro.isChecked():
            self.saldo = self.saldo + self.valor_cilantro
        else:
            self.saldo = self.saldo - self.valor_cilantro
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_cebolla(self):
        if self.check_cebolla.isChecked():
            self.saldo = self.saldo + self.valor_cebolla
            self.nombre2 = ("Cebolla Junca 500 GR: $5.100")
        else:
            self.nombre2 = ("")
            self.saldo = self.saldo - self.valor_cebolla
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_zanahoria(self):
        if self.check_zanhoria.isChecked():
            self.saldo = self.saldo + self.valor_zanahoria
        else:
            self.saldo = self.saldo - self.valor_zanahoria
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_ceboBlanca(self):
        if self.check_ceboBlanca.isChecked():
            self.saldo = self.saldo + self.valor_ceboBlanca
            self.nombre7 = ("Cebolla Blanca 1 und: $1.100")
        else:
            self.saldo = self.saldo - self.valor_ceboBlanca
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_ceboRoja(self):
        if self.check_ceboRoja.isChecked():
            self.saldo = self.saldo + self.valor_ceboRoja
            self.nombre8 = ("Cebolla Roja 1 und: $700")
        else:
            self.saldo = self.saldo - self.valor_ceboRoja
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

    def agregar_al_carrito_verengena(self):

        if self.check_verengena.isChecked():
            self.saldo = self.saldo + self.valor_veregena
            self.nombre9 = ("Berenjena 1 und: $2.200")
        else:
            self.nombre9 = ("")
            self.saldo = self.saldo - self.valor_veregena
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))


    def agregar_al_carrito_lechuga(self):
        if self.check_lechuga.isChecked():
            self.saldo = self.saldo + self.valor_lechuga
        else:
            self.saldo = self.saldo - self.valor_lechuga
        texto = "saldo: " + str(self.saldo)
        self.labeltitulo.setText(texto)
        print("valor de la compra: " + str(self.saldo))

        ''''
    def mostrar_nombre_precio_fresa(self, checked1):
        if checked1:
            nombre_producto = "Bandeja de fresa"
            precio_producto = self.valor_fresa
            mensaje = f"{nombre_producto}: ${precio_producto}"
            self.mensaje_precio.setText(mensaje)
        else:
            self.mensaje_precio.clear()

        
    def mostrar_nombre_precios_sandia(self, checked2):
        if checked2:
            nombre_producto2 = "Sandia 1 und"
            precio_producto2 = self.valor_sandia
            mensaje2 = f"{nombre_producto2}: ${precio_producto2}"
            self.mensaje_precio2.setText(mensaje2)
        else:
            self.mensaje_precio2.clear()

    def mostrar_nombre_precios_pina(self, checked3):
        if checked3:
            nombre_producto3 = "Piña 1 und"
            precio_producto3 = self.valor_pina
            mensaje3 = f"{nombre_producto3}: ${precio_producto3}"
            self.mensaje_precio3.setText(mensaje3)
        else:
            self.mensaje_precio3.clear()

        def mostrar_nombre_precios_pera(self, checked4):
        if checked4:
            nombre_producto4 = "Pera 1 und"
            precio_producto4 = self.valor_pera
            mensaje4 = f"{nombre_producto4}: ${precio_producto4}"
            self.mensaje_precio4.setText(mensaje4)
        else:
            self.mensaje_precio4.clear()

    def mostrar_nombre_precios_uva(self, checked5):
        if checked5:
            nombre_producto5 = "Bandeja de uva"
            precio_producto5 = self.valor_uva
            mensaje5 = f"{nombre_producto5}: ${precio_producto5}"
            self.mensaje_precio5.setText(mensaje5)
        else:
            self.mensaje_precio5.clear()

    def mostrar_nombre_precios_mango(self, checked6):
        if checked6:
            nombre_producto6 = "Mango 1 und"
            precio_producto6 = self.valor_mango
            mensaje6 = f"{nombre_producto6}: ${precio_producto6}"
            self.mensaje_precio6.setText(mensaje6)
        else:
            self.mensaje_precio6.clear()
            
    def mostrar_nombre_precios_papaya(self, checked7):
        if checked7:
            nombre_producto7 = "Papaya 1 und"
            precio_producto7 = self.valor_papaya
            mensaje7 = f"{nombre_producto7}: ${precio_producto7}"
            self.mensaje_precio7.setText(mensaje7)
        else:
            self.mensaje_precio7.clear()

        
    def mostrar_nombre_precios_manzana(self, checked8):
        if checked8:
            nombre_producto8 = "Manzana 1 und"
            precio_producto8 = self.valor_manzana
            mensaje8 = f"{nombre_producto8}: ${precio_producto8}"
            self.mensaje_precio8.setText(mensaje8)
        else:
            self.mensaje_precio8.clear()
        
   

    
     
    def mostrar_nombre_precios_apio(self, checked9):
        if checked9:
            nombre_producto9 = "Apio 700 GR"
            precio_producto9 = self.valor_apio
            mensaje8 = f"{nombre_producto9}: ${precio_producto9}"
            self.mensaje_precio9.setText(mensaje8)
        else:
            self.mensaje_precio9.clear()

    def mostrar_nombre_precios_cilantro(self, checked10):
        if checked10:
            nombre_producto10 = "Cilantro 100 GR"

            precio_producto10 = self.valor_cilantro
            mensaje10 = f"{nombre_producto10}: ${precio_producto10}"
            self.mensaje_precio10.setText(mensaje10)
        else:
            self.mensaje_precio10.clear()

    def mostrar_nombre_precios_cebolla(self, checked11):
        if checked11:
            nombre_producto11 = "Cebolla Junca 500 GR"

            precio_producto11 = self.valor_cebolla
            mensaje11 = f"{nombre_producto11}: ${precio_producto11}"
            self.mensaje_precio11.setText(mensaje11)
        else:
            self.mensaje_precio11.clear()

    def mostrar_nombre_precios_zanahoria(self, checked12):
        if checked12:
            nombre_producto12 = "Zanahoria 1000 GR"

            precio_producto12 = self.valor_zanahoria
            mensaje12 = f"{nombre_producto12}: ${precio_producto12}"
            self.mensaje_precio12.setText(mensaje12)
        else:
            self.mensaje_precio12.clear()

    def mostrar_nombre_precios_cebollaBlanca(self, checked13):
        if checked13:
            nombre_producto13 = "Cebolla Blanca 1 und"

            precio_producto13 = self.valor_ceboBlanca
            mensaje13 = f"{nombre_producto13}: ${precio_producto13}"
            self.mensaje_precio13.setText(mensaje13)
        else:
            self.mensaje_precio13.clear()

    def mostrar_nombre_precios_cebollaRoja(self, checked14):
        if checked14:
            nombre_producto14 = "Cebolla Roja 1 und"

            precio_producto14 = self.valor_ceboRoja
            mensaje14 = f"{nombre_producto14}: ${precio_producto14}"
            self.mensaje_precio14.setText(mensaje14)
        else:
            self.mensaje_precio14.clear()

    def mostrar_nombre_precios_verengena(self, checked15):
        if checked15:
            nombre_producto15 = "Berenjena 1 und"

            precio_producto15 = self.valor_veregena
            mensaje15 = f"{nombre_producto15}: ${precio_producto15}"
            self.mensaje_precio15.setText(mensaje15)
        else:
            self.mensaje_precio15.clear()

    def mostrar_nombre_precios_lechuga(self, checked16):
        if checked16:
            nombre_producto16 = "Lechuga 1 und"

            precio_producto16 = self.valor_lechuga
            mensaje16 = f"{nombre_producto16}: ${precio_producto16}"
            self.mensaje_precio16.setText(mensaje16)
        else:
            self.mensaje_precio16.clear()'''


    def enviar_al_carrito(self):

        # abrimos el archivo en modo agregar
        self.file = open('datos/pedidos.txt', 'ab')

        # Traer el texto de los Qline y los concatena con ;
        self.file.write(bytes(
            # Cajas de texto de la pestaña
            self.nombre1 + ";" +
            self.nombre2 + ";" +
            self.nombre3 + ";" +
            self.nombre4 + ";" +
            self.nombre5 + ";" +
            self.nombre6 + ";" +
            self.nombre7 + ";" +
            self.nombre8 + ";" +
            self.nombre9 + ";" +
            self.nombre10 + ";" +
            self.nombre11 + ";" +
            self.nombre12 + ";" +
            self.labeltitulo.text() + "\n", encoding='UTF-8'))
        self.file.close()

        # abrimos en modo lectura en formato bite
        self.file = open('datos/pedidos.txt', 'rb')

        # recorrer el archivo linea x linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            if linea == '':
                break

        self.file.close()


    # ---- METODOS DE ADD,EDIT Y DELETE ---------
    def accion_delete(self):

        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self,
                                       'Warning',
                                       'Para borrar, debe seleccionar un registro')

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Estas Segura de que quieres borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No

        )
        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != ''

            ):
                # abrimos el archivo en modo de lectura:
                self.file = open('datos/clientes.txt', 'rb')

                # Lista vacia para guardar todos los usuarios:
                self.usuarios = []

                # recorremos el archivo línea por línea:
                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    # Obtenemos del string una lista con datos separados por;
                    lista = linea.split(";")
                    # se para sí ya no hay más registros en el archivo
                    if linea == '':
                        break
                    # Creamos un objeto de tipo cliente llamdo u
                    u = Cliente(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],

                    )
                    # Metemos el objeto en la lista de ususarios:
                    self.usuarios.append(u)

                # Cerramos el archivo:
                self.file.close()
                # En este punto ya tenmos la lista usuarios con todos los ususarios:

                # Recoremos la lista de usuarios:
                for u in self.usuarios:
                    # buscamos el usuario por el documento:
                    if (
                            u.cedula == self.tabla.item(filaActual, 2).text()
                    ):
                        # Removemos el usuario d ela lista de usuarios:
                        self.usuarios.remove(u)

                        # Paramos el for
                        break
                # abrimos los archivos en modo escritura para reeescribir los datos sin el usuario borrado.
                self.file = open('datos/clientes.txt', 'wb')

                # Recorremos la lista de usuarios por usuarios en el archivo.
                for u in self.usuarios:
                    self.file.write(bytes(u.nombre_completo + ";"
                                          + u.cedula + ";"
                                          + u.codigo_ingresado + ";"
                                          + u.datetime, encoding='UTF-8'))

                # Cerrar el archivo:
                self.file.close()

                # Hacemos que en la tabla no se vea el registro:
                self.tabla.removeRow(filaActual)

                return QMessageBox.question(
                    self,
                    'confirmation',
                    'El registro ha sido eliminado exitosamente.',
                    QMessageBox.StandardButton.Ok
                )
            else:

                # Hacemos que en la tabla no se vea el registro en caso de tratarse de una fila vacia:
                self.tabla.removeRow(filaActual)

    def accion_add(self):
        # obtenemos el número de filas que tiene la tabla.
        ultimaFila = self.tabla.rowCount()

        # Insertamos una fila nueva despues de la ultima fila:
        self.tabla.insertRow(ultimaFila)

        # Llenamos cada celda de la nueva fila con un string vacio '':
        self.tabla.setItem(ultimaFila, 0, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 1, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 2, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 3, QTableWidgetItem(''))

    def accion_insert(self):
        filaActual = self.tabla.currentRow()
        if filaActual < 0:
            return QMessageBox.warning(self,
                                       'Warning',
                                       'Para ingresar, debe seleccionar un registro')
        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Estas Segura de que quieres ingresar este nuevo  registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No

        )
        # Variable para controlar que se hayan ingresado todos los datos:
        datosVacios = True

        if boton == QMessageBox.StandardButton.Yes:

            # validamos que se hayan ingresado los datos
            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != ''
            ):
                # Actualiza mos varible para indicar que se ingresaron todos los datos:
                datosVacios = False

                # Abrimos el archivo en modo lectura
                self.file = open('datos/clientes.txt', 'rb')

                # Lista vacia para guardar todos los usuarios:
                self.usuarios = []

                # recorremos el archivo línea por línea:
                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    # Obtenemos del string una lista con datos separados por ;

                    lista = linea.split(";")
                    # se para sí ya no hay más registros en el archivo
                    if linea == '':
                        break
                    # Creamos un objeto de tipo cliente llamdo u
                    u = Cliente(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],

                    )
                    # Metemos el objeto en la lista de ususarios:
                    self.usuarios.append(u)

                # Cerramos el archivo:
                self.file.close()
                # En este punto ya tenmos la lista usuarios con todos los ususarios.
                # variable para controlar que ya existe el registro:
                existeRegistro = False
                # variable para controlar si ya es un registro que ya existe y se va a editar:
                existeDocumento = False
                # Recorremos la lista de Usuarios:
                for u in self.usuarios:

                    # comparamos que todos los datos de registro ingresado:
                    if (
                            u.nombre_completo == self.tabla.item(filaActual, 0).text() and
                            u.cedula == self.tabla.item(filaActual, 1).text() and
                            u.codigo_ingresado == self.tabla.item(filaActual, 2).text() and
                            u.datetime == self.tabla.item(filaActual, 3).text()

                    ):
                        # Indicamos que encontramos el documento:
                        existeRegistro = True

                        return QMessageBox.warning(self, 'Warning', 'Resgistro duplicado, no se puede registrar')

                        # paramos el  for:
                        break
                    # si los datos son diferentes a los que existen:
                    if not existeRegistro:

                        # Recorremos la lista de usuarios
                        for u in self.usuarios:
                            # comparamos todos los datos del registro ingresado con el documento:
                            if (
                                    u.cedula == self.tabla.item(filaActual, 2).text()

                            ):
                                # Indicamos que encontramos el documento:
                                existeDocumento = True

                                u.nombre_completo = self.tabla.item(filaActual, 0).text()
                                u.cedula = self.tabla.item(filaActual, 1).text()
                                u.codigo_ingresado = self.tabla.item(filaActual, 2).text()
                                u.datetime = self.tabla.item(filaActual, 3).text()

                                # abrimos los archivos en modo escritura para reeescribir los datos sin el usuario borrado.
                                self.file = open('datos/clientes.txt', 'wb')

                                # Recorremos la lista de usuarios por usuarios en el archivo.
                                for u in self.usuarios:
                                    self.file.write(bytes(u.nombre_completo + ";"
                                                          + u.cedula + ";"
                                                          + u.codigo_ingresado + ";"
                                                          + u.datetime, encoding='UTF-8'))

                                self.file.seek(0, 2)
                                self.file.close()

                            return QMessageBox.question(
                                self,
                                'confirmation',
                                'Los datos del registro se han editado exitosamente.',
                                QMessageBox.StandardButton.Ok
                            )
                    if datosVacios:
                        return QMessageBox.warning(self, 'Warning', 'Debe ingresar todos los datos en el registro')







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
