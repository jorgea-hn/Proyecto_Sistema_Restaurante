from PyQt5 import QtWidgets, uic

#iniciar app
app = QtWidgets.QApplication([])

#cargar archivos .ui


principal=uic.loadUi("Principal.ui")
login=uic.loadUi("Login.ui")
mesas = uic.loadUi("PrincipalMesas.ui")
productos = uic.loadUi("PrincipalProductos.ui")
menu_m=uic.loadUi("Menu_mesas.ui")
menu_p=uic.loadUi("Menu_Productos.ui")

def Principal_Login():
    principal.hide()
    login.show()


def Login_Mesas():
    name=login.lineEdit.text()
    password=login.lineEdit_2.text()

    if name=="admin" and password=="admin1234":
        login.hide()
        mesas.show()

    # else:
    #     login.label.setText("Usuario o contraseña incorecctos")


def Productos_Mesas():
    productos.hide()
    mesas.show()

def Productos_MenuP():
    productos.hide()
    menu_p.show()
    

def Mesas_Productos():
    
    productos.show()

def Mesas_MenuM():
    
    menu_m.show()
    






    
#botones 

principal.pushButton_Principal.clicked.connect(Principal_Login)

login.pushButton.clicked.connect(Login_Mesas)

mesas.pushButton_Productos.clicked.connect(Mesas_Productos)
mesas.pushButton_AgregarMesa.clicked.connect(Mesas_MenuM)

productos.pushButton_Mesas.clicked.connect(Productos_Mesas)
productos.pushButton_AgregarProducto.clicked.connect(Productos_MenuP)







#ejecutar 

principal.show()
app.exec()






# import sys
# from PyQt5 import uic
# from PyQt5.QtWidgets import QMainWindow,QApplication

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("inicio.ui",self)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     GUI = App()
#     GUI.show()
#     sys.exit(app.exec_())
