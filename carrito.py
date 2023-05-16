from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QApplication
import sys


class ShoppingCart(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Conectar los elementos de la GUI a los métodos de manejo de eventos
        self.add_button.clicked.connect(self.add_product)
        self.remove_button.clicked.connect(self.remove_product)

    def add_product(self):
        # Obtener el producto seleccionado
        product_name = self.product_combobox.currentText()
        product_price = self.product_prices[product_name]

        # Agregar el producto al carrito
        row_count = self.cart_table.rowCount()
        self.cart_table.insertRow(row_count)
        self.cart_table.setItem(row_count, 0, QTableWidgetItem(product_name))
        self.cart_table.setItem(row_count, 1, QTableWidgetItem(str(product_price)))

        # Actualizar el precio total
        self.total_price += product_price
        self.total_label.setText(f"Total: ${self.total_price:.2f}")

    def remove_product(self):
        # Obtener el producto seleccionado
        selected_row = self.cart_table.currentRow()
        if selected_row < 0:
            return
        product_price = float(self.cart_table.item(selected_row, 1).text())

        # Eliminar el producto del carrito
        self.cart_table.removeRow(selected_row)

        # Actualizar el precio total
        self.total_price -= product_price
        self.total_label.setText(f"Total: ${self.total_price:.2f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingCart()
    window.show()
    sys.exit(app.exec_())
