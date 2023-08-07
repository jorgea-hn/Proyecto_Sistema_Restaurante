import re 
from PyQt5 import QtWidgets, uic

#iniciar app
app = QtWidgets.QApplication([])

#cargar archivos .ui


principal=uic.loadUi("Layout\\Principal.ui")
login=uic.loadUi("Layout\\Login.ui")
mesas = uic.loadUi("Layout\\PrincipalMesas.ui")
productos = uic.loadUi("Layout\\PrincipalProductos.ui")
menu_m=uic.loadUi("Layout\\Menu_mesas.ui")
menu_p=uic.loadUi("Layout\\Menu_Productos.ui")


def Obtener_InfoMenuP():

    precio=menu_p.lineEdit_precioProducto.text()
    nombre=menu_p.lineEdit_nombreProducto.text()
    
    patron=r'^[a-zA-Z\s]+$'
    
    if len(precio)>0 and len(nombre)>0:
        
        if re.match(patron, nombre) and not nombre[0].isspace() and precio.isdigit() :
            print(nombre)
            print(precio)
        
        if nombre[0].isspace() or not re.match(patron, nombre):
            menu_p.label_Nombre.setText("Nombre no valido") 

        else:
            menu_p.label_Nombre.setText("")


        if precio.isdigit()==False:
            menu_p.label_Precio.setText("Valor no valido")
        
        else:
            menu_p.label_Precio.setText("")


def Obtener_InfoMenuM():
    cantidad=menu_m.comboBox.currentText()
    print(cantidad)


def Principal_Login():
    principal.hide()
    login.show()


def Login_Mesas():
    name=login.lineEdit.text()
    password=login.lineEdit_2.text()

    if name=="admin" and password=="admin1234":
        login.hide()
        mesas.show()

    else:
        login.label.setText("Usuario o contraseña incorecctos")


def Productos_Mesas():
    productos.hide()
    mesas.show()

def Productos_MenuP():
    
    menu_p.show()
    

def Mesas_Productos():
    mesas.hide()
    productos.show()

def Mesas_MenuM():
    
    menu_m.show()
    


#botones 

principal.pushButton_Principal.clicked.connect(Principal_Login)

login.pushButton.clicked.connect(Login_Mesas)

mesas.pushButton_Productos.clicked.connect(Mesas_Productos)
mesas.pushButton_AgregarMesa.clicked.connect(Mesas_MenuM)

menu_m.pushButton.clicked.connect(Obtener_InfoMenuM)


productos.pushButton_Mesas.clicked.connect(Productos_Mesas)
productos.pushButton_AgregarProducto.clicked.connect(Productos_MenuP)


menu_p.pushButton_Guardar.clicked.connect(Obtener_InfoMenuP)




#ejecutar 

principal.show()
app.exec()






