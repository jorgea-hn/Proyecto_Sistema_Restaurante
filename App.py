import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi(".//Layout/Principal.ui",self)
        uic.loadUi(".//Layout/Menu_mesas.ui",self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = App()
    GUI.show()
    sys.exit(app.exec_())



# import sys
# from PyQt5 import uic
# from PyQt5.QtWidgets import QMainWindow, QApplication




# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi(".//Layout/PrincipalMesas.ui",self)
        

#         self.ui.pushButton_Mesas.clicked.connect(self.abrir_interfaz_mesas)
#         self.ui.pushButton_Productos.clicked.connect(self.abrir_interfaz_productos)


#     def abrir_interfaz_mesas(self):
#         self.hide() # oculta la interfaz actual
#         mesas = Mesas() # crea una instancia de la interfaz de mesas
#         mesas.show() # muestra la interfaz de mesas

#     def abrir_interfaz_productos(self):
#         self.hide() # oculta la interfaz actual
#         productos = Productos() # crea una instancia de la interfaz de productos
#         productos.show() # muestra la interfaz de productos


# class Productos(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi(".//Layout/PrincipalProductos.ui",self)


# class Mesas(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi(".//Layout/PrincipalMesas.ui",self)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     GUI = App()
#     GUI.show()
#     sys.exit(app.exec_())



