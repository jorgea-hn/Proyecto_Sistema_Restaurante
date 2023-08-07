import re
from PyQt5 import QtWidgets, uic
import Database

#iniciar app
app = QtWidgets.QApplication([])

#cargar archivos .ui


principal=uic.loadUi("./Layout/Principal.ui")
login=uic.loadUi("./Layout/Login.ui")
mesas = uic.loadUi("./Layout/PrincipalMesas.ui")
productos = uic.loadUi("./Layout/PrincipalProductos.ui")
menu_m=uic.loadUi("./Layout/Menu_mesas.ui")
menu_p=uic.loadUi("./Layout/Menu_Productos.ui")


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


def Productos_Login():
    productos.hide()
    login.show()

def agregar_mesa():
    # Obtener los valores de los campos del formulario
    capacidad = menu_m.comboBox_Capacidad.currentText()
    print(capacidad)
    # Insertar la nueva mesa en la tabla 'mesas'
    Database.agregar_datos((capacidad), 'mesas')


def agregar_producto():
    # Obtener los valores de los campos del formulario
    precio=menu_p.lineEdit_precioProducto.text()
    nombre=menu_p.lineEdit_nombreProducto.text()
    
    patron=r'^[a-zA-Z\s]+$'
    
    if len(precio)>0 and len(nombre)>0:
        
        if re.match(patron, nombre) and not nombre[0].isspace() and precio.isdigit() :
            nombre=nombre
            precio=precio
            # Insertar el nuevo producto en la tabla 'productos'
            mensaje=Database.agregar_datos((nombre, int(precio)), 'productos')
            productos.tableWidget.update()
            menu_p.label_Mensaje.setText(mensaje)
            menu_p.lineEdit_nombreProducto.setText("")
            menu_p.lineEdit_precioProducto.setText("")

            
        
        
        if nombre[0].isspace() or not re.match(patron, nombre):
            menu_p.label_Nombre.setText("Nombre no valido") 
            menu_p.label_Mensaje.setText("")

        else:
            menu_p.label_Nombre.setText("")
            


        if precio.isdigit()==False:
            menu_p.label_Precio.setText("Valor no valido")
            menu_p.label_Mensaje.setText("")
        
        else:
            menu_p.label_Precio.setText("")
    
    





def total_Productos():
    # Mostrar la ventana de productos
    productos.show()

    # Cargar los datos de la tabla 'productos' en el QTableWidget
    Database.traer_datos(productos.tableWidget, 'productos')

#botones 

principal.pushButton_Principal.clicked.connect(Principal_Login)

login.pushButton.clicked.connect(Login_Mesas)

mesas.pushButton_Productos.clicked.connect(Mesas_Productos)
mesas.pushButton_AgregarMesa.clicked.connect(Mesas_MenuM)

productos.pushButton_Mesas.clicked.connect(Productos_Mesas)
productos.pushButton_AgregarProducto.clicked.connect(Productos_MenuP)
productos.pushButton_Salir.clicked.connect(Productos_Login)

menu_p.pushButton_Guardar.clicked.connect(agregar_producto)
menu_m.pushButton_Guardar.clicked.connect(agregar_mesa)



productos.showEvent = lambda event: total_Productos()

# Crear tablas y agregar datos por defecto
Database.crear_tablas()


#ejecutar 

productos.show()
app.exec()

