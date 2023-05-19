import datetime
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from cliente import Cliente
class Ventana(QWidget):
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

        # Agregamos el letrero de bienvenida
        label_bienvenida = QLabel('BIENVENIDO A DISFRUTA', self)
        label_bienvenida.setStyleSheet('background-color: #B0F2C2; color: black;')
        label_bienvenida.setFont(QFont('Times New Roman', 16))
        label_bienvenida.adjustSize()

        # Colocamos el letrero en el medio de la ventana en la parte superior
        label_bienvenida.setAlignment(Qt.AlignCenter)
        label_bienvenida.setGeometry(153, 5, self.width(), 40)

        # Creamos los botones y los agregamos a la ventana
        boton_frutas = QPushButton('FRUTAS', self)
        boton_frutas.setGeometry(250, 150, 150, 120)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_frutas.setCursor(Qt.PointingHandCursor)
        boton_frutas.setStyleSheet('background-color: #FFB6AE;')

        boton_frutas.clicked.connect(self.abrir_ventana_frutas)

        boton_verduras = QPushButton('VERDURAS', self)
        boton_verduras.setGeometry(250, 300, 150, 120)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_verduras.setCursor(Qt.PointingHandCursor)
        boton_verduras.setStyleSheet('background-color: #FAFCAF;')
        boton_verduras.clicked.connect(self.abrir_ventana_verduras)

        boton_carrito = QPushButton('CARRITO', self)
        boton_carrito.setGeometry(250, 450, 150, 120)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_carrito.setCursor(Qt.PointingHandCursor)
        boton_carrito.setStyleSheet('background-color: #FFE1AE;')
        boton_carrito.clicked.connect(self.abrir_ventana_carrito)

        # Creamos el botón "Personal Autorizado"
        boton_personal = QPushButton('PERSONAL AUTORIZADO', self)
        boton_personal.setGeometry(750, 730, 230, 50)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_personal.setCursor(Qt.PointingHandCursor)
        boton_personal.setStyleSheet('background-color: #B0F2C2;')
        boton_personal.clicked.connect(self.abrir_ventana_personal)

    def abrir_ventana_frutas(self):
        self.hide()  # Ocultamos la ventana actual
        ventana_frutas = QDialog(self)
        ventana_frutas.setWindowTitle('FRUTAS')
        ventana_frutas.resize(1000, 800)
        ventana_frutas.setStyleSheet('background-color: white;')

        # Creamos un QLabel con el mensaje "Bienvenido"
        mensaje_bienvenida = QLabel('BIENVENIDO AL CATÁLOGO DE FRUTAS', ventana_frutas)
        mensaje_bienvenida.setGeometry(0, 0, 200, 20)
        mensaje_bienvenida.setStyleSheet('background-color: #B0F2C2; color: black;')
        mensaje_bienvenida.setAlignment(Qt.AlignCenter)
        mensaje_bienvenida.setFont(QFont('Times New Roman', 10))

        # CAR IMAGEN PRODUCT
        # producto fresa
        label_imagen = QLabel('', ventana_frutas)
        label_imagen.setGeometry(50, 50, 200, 200)
        pixmap = QPixmap('imagenes/fresa.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen.setPixmap(pixmap)

        nombre_producto = QLabel('Bandeja de fresa: \n$8.700', ventana_frutas)
        nombre_producto.setGeometry(50, 200, 250, 80)
        nombre_producto.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_frutas)
        b.move(50, 270)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto sandia FRUTA2
        label_imagen2 = QLabel('', ventana_frutas)
        label_imagen2.setGeometry(320, 50, 200, 200)
        pixmap = QPixmap('imagenes/fruta2.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen2.setPixmap(pixmap)

        nombre_producto2 = QLabel('Sandia 1 und: \n$13.500', ventana_frutas)
        nombre_producto2.setGeometry(320, 200, 250, 80)
        nombre_producto2.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_frutas)
        b.move(320, 270)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto piña FRUTA3
        label_imagen3= QLabel('', ventana_frutas)
        label_imagen3.setGeometry(550, 50, 200, 200)
        pixmap = QPixmap('imagenes/fruta3.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen3.setPixmap(pixmap)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox



        nombre_producto3 = QLabel('Piña 1 und: \n$6.500', ventana_frutas)
        nombre_producto3.setGeometry(550, 200, 250, 80)
        nombre_producto3.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_frutas)
        b.move(550, 270)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)


        # producto pera FRUTA4
        label_imagen4 = QLabel('', ventana_frutas)
        label_imagen4.setGeometry(800, 50, 200, 200)
        pixmap = QPixmap('imagenes/fruta4.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen4.setPixmap(pixmap)


        nombre_producto4 = QLabel('Pera 1 und: \n$1.700', ventana_frutas)
        nombre_producto4.setGeometry(800, 200, 250, 80)
        nombre_producto4.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_frutas)
        b.move(800, 270)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto uva Fruta5
        label_imagen5 = QLabel('', ventana_frutas)
        label_imagen5.setGeometry(50, 320, 200, 200)
        pixmap = QPixmap('imagenes/fruta5.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen5.setPixmap(pixmap)

        nombre_producto5 = QLabel('Bandeja de uva: \n$15.400', ventana_frutas)
        nombre_producto5.setGeometry(50, 450, 250, 80)
        nombre_producto5.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_frutas)
        b.move(50, 520)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto mango FRUTA6
        label_imagen6 = QLabel('', ventana_frutas)
        label_imagen6.setGeometry(320, 300, 200, 200)
        pixmap = QPixmap('imagenes/fruta6.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen6.setPixmap(pixmap)

        nombre_producto6 = QLabel('Mango 1 und: \n$1.800', ventana_frutas)
        nombre_producto6.setGeometry(320, 450, 250, 80)
        nombre_producto6.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_frutas)
        b.move(320, 520)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto Papaya FRUTA7
        label_imagen7 = QLabel('', ventana_frutas)
        label_imagen7.setGeometry(550, 300, 200, 200)
        pixmap = QPixmap('imagenes/fruta7.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen7.setPixmap(pixmap)

        nombre_producto7 = QLabel('Papaya 1 und: \n$4.300', ventana_frutas)
        nombre_producto7.setGeometry(550, 450, 250, 80)
        nombre_producto7.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_frutas)
        b.move(550, 520)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)


        # producto Manzana FRUTA8
        label_imagen8 = QLabel('', ventana_frutas)
        label_imagen8.setGeometry(800, 300, 200, 200)
        pixmap = QPixmap('imagenes/fruta8.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen8.setPixmap(pixmap)


        nombre_producto8 = QLabel('Manzana 1 und: \n$1.700', ventana_frutas)
        nombre_producto8.setGeometry(800, 450, 250, 80)
        nombre_producto8.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_frutas)
        b.move(800, 520)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)


        # Añadimos los QLabel a la ventana de frutas
        layout = QVBoxLayout()
        layout.addWidget(mensaje_bienvenida)
        layout.addStretch()
        layout.addStretch()
        layout.setAlignment(Qt.AlignCenter)
        ventana_frutas.setLayout(layout)

        # Creamos el botón para volver a la ventana principal
        boton_volver = QPushButton('Volver', ventana_frutas)
        boton_volver.setGeometry(110, 150, 100, 30)
        boton_volver.setStyleSheet('background-color: #FFB6AE;')
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_volver.setCursor(Qt.PointingHandCursor)
        boton_volver.move(ventana_frutas.width() - boton_volver.width() - 10,
                          ventana_frutas.height() - boton_volver.height() - 10)
        boton_volver.clicked.connect(lambda: (ventana_frutas.close(), self.show()))

        ventana_frutas.exec_()

    def abrir_ventana_verduras(self):
        self.hide()  # Ocultamos la ventana actual
        ventana_verduras = QDialog(self)
        ventana_verduras.setWindowTitle('VERDURA')
        ventana_verduras.resize(1000, 800)
        ventana_verduras.setStyleSheet('background-color: white;')

        # Creamos un QLabel con el mensaje "Bienvenido"
        mensaje_bienvenida = QLabel('BIENVENIDO AL CATÁLOGO DE VERDURAS', ventana_verduras)
        mensaje_bienvenida.setGeometry(0, 0, 200, 50)
        mensaje_bienvenida.setStyleSheet('background-color: #B0F2C2; color: black;')
        mensaje_bienvenida.setAlignment(Qt.AlignCenter)
        mensaje_bienvenida.setFont(QFont('Times New Roman', 12))

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
        b = QCheckBox("Añadir al carrito", ventana_verduras)
        b.move(50, 270)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto Cilantro verdura2
        label_imagen2 = QLabel('', ventana_verduras)
        label_imagen2.setGeometry(320, 50, 200, 200)
        pixmap = QPixmap('imagenes/verdura2.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen2.setPixmap(pixmap)

        nombre_producto2 = QLabel('Cilantro 100 GR: \n$1.000', ventana_verduras)
        nombre_producto2.setGeometry(320, 200, 250, 80)
        nombre_producto2.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_verduras)
        b.move(320, 270)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

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
        b = QCheckBox("Añadir al carrito", ventana_verduras)
        b.move(550, 270)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto Zanahoria FRUTA4
        label_imagen4 = QLabel('', ventana_verduras)
        label_imagen4.setGeometry(800, 50, 200, 200)
        pixmap = QPixmap('imagenes/verdura4.jpg.')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen4.setPixmap(pixmap)

        nombre_producto4 = QLabel('zanahoria 1000 GR: \n$4.300', ventana_verduras)
        nombre_producto4.setGeometry(800, 200, 250, 80)
        nombre_producto4.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_verduras)
        b.move(800, 270)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto Cabolla blanca verdura5
        label_imagen5 = QLabel('', ventana_verduras)
        label_imagen5.setGeometry(50, 320, 200, 200)
        pixmap = QPixmap('imagenes/verdura5.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen5.setPixmap(pixmap)

        nombre_producto5 = QLabel('Cebolla Blanca 1 und: \n$1.100', ventana_verduras)
        nombre_producto5.setGeometry(50, 450, 250, 80)
        nombre_producto5.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_verduras)
        b.move(50, 520)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto cabolla roja Verdura6
        label_imagen6 = QLabel('', ventana_verduras)
        label_imagen6.setGeometry(320, 300, 200, 200)
        pixmap = QPixmap('imagenes/verdura6.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen6.setPixmap(pixmap)

        nombre_producto6 = QLabel('Cebolla Roja 1 und: \n$700', ventana_verduras)
        nombre_producto6.setGeometry(320, 450, 250, 80)
        nombre_producto6.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_verduras)
        b.move(320, 520)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto verengena VERDURA7
        label_imagen7 = QLabel('', ventana_verduras)
        label_imagen7.setGeometry(550, 300, 200, 200)
        pixmap = QPixmap('imagenes/verdura7.jpg')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen7.setPixmap(pixmap)

        nombre_producto7 = QLabel('Verengena 1 und: \n$2.200', ventana_verduras)
        nombre_producto7.setGeometry(550, 450, 250, 80)
        nombre_producto7.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_verduras)
        b.move(550, 520)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # producto Manzana VERDURA8
        label_imagen8 = QLabel('', ventana_verduras)
        label_imagen8.setGeometry(800, 300, 200, 200)
        pixmap = QPixmap('imagenes/verdura8.png')
        pixmap = pixmap.scaledToWidth(100)  # Ajustamos el tamaño de la imagen a 100 píxeles de ancho
        label_imagen8.setPixmap(pixmap)


        nombre_producto8 = QLabel('Lechuga 1 und: \n$3.300', ventana_verduras)
        nombre_producto8.setGeometry(800, 450, 250, 80)
        nombre_producto8.setFont(QFont('Times New Roman', 10))
        b = QCheckBox("Añadir al carrito", ventana_verduras)
        b.move(800, 520)
        b.resize(320, 40)
        # Cambiar el cursor cuando el ratón pase sobre el QCheckBox
        b.setCursor(Qt.PointingHandCursor)

        # Añadimos los QLabel a la ventana de frutas
        layout = QVBoxLayout()
        layout.addWidget(mensaje_bienvenida)
        layout.addStretch()
        layout.addStretch()
        layout.setAlignment(Qt.AlignCenter)
        ventana_verduras.setLayout(layout)

        # Creamos el botón para volver a la ventana principal
        boton_volver = QPushButton('Volver', ventana_verduras)
        boton_volver.setGeometry(110, 150, 100, 30)
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_volver.setCursor(Qt.PointingHandCursor)
        boton_volver.setStyleSheet('background-color: #FAFCAF;')
        boton_volver.move(ventana_verduras.width() - boton_volver.width() - 10,
                          ventana_verduras.height() - boton_volver.height() - 10)
        boton_volver.clicked.connect(lambda: (ventana_verduras.close(), self.show()))

        ventana_verduras.exec_()

    def abrir_ventana_carrito(self):
        self.hide()  # Ocultamos la ventana actual
        ventana_carrito = QDialog(self)
        ventana_carrito.setWindowTitle('CARRITO')
        ventana_carrito.resize(1000, 800)

        # Creamos un QLabel con el mensaje "Bienvenido"
        mensaje_bienvenida = QLabel('PRODUCTOS AGREGADOS', ventana_carrito)
        mensaje_bienvenida.setGeometry(0, 0, 200, 50)
        mensaje_bienvenida.setStyleSheet('background-color: #B0F2C2; color: black;')
        mensaje_bienvenida.setAlignment(Qt.AlignCenter)
        mensaje_bienvenida.setFont(QFont('Times New Roman', 12))

        # Añadimos el QLabel a la ventana de frutas
        layout = QVBoxLayout()
        layout.addWidget(mensaje_bienvenida)
        layout.addStretch()
        ventana_carrito.setLayout(layout)

        # Creamos el botón para volver a la ventana principal
        boton_volver = QPushButton('Volver', ventana_carrito)
        boton_volver.setGeometry(110, 150, 100, 30)
        boton_volver.setStyleSheet('background-color: #FFE1AE;')
        # Cambiar el cursor al pasar el puntero por encima del botón "Volver"
        boton_volver.setCursor(Qt.PointingHandCursor)
        boton_volver.move(ventana_carrito.width() - boton_volver.width() - 10,
                          ventana_carrito.height() - boton_volver.height() - 10)

        boton_volver.clicked.connect(lambda: (ventana_carrito.close(), self.show()))

        ventana_carrito.exec_()

    def abrir_ventana_personal(self):
        self.hide()  # Ocultamos la ventana actual
        self.ventana_personal = QDialog(self)
        self.ventana_personal.setWindowTitle('PERSONAL AUTORIZADO')
        self.ventana_personal.resize(1000, 800)

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

            # Creamos un QLabel con el mensaje "Bienvenido"
            mensaje_bienvenida = QLabel('PEDIDOS', ventana_otra)
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
        ventana_informacion.setWindowTitle('INFORMACION DE REGISTRO')
        ventana_informacion.resize(1200, 600)  # Tamaño personalizado para que todos los elementos sean visibles
        ventana_informacion.setStyleSheet('background-color: white;')

        # abrimos el archivo en modo de lectura:
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacia para guardar todos los usuarios:
        self.usuarios = []

        # recorremos el archivo línea por línea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # Obtenemos del string una lista con  datos separados por ;

            lista = linea.split(";")
            # se para si ya no hay mas registros en el archivo
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

        # Ponemos un espacio después:
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
