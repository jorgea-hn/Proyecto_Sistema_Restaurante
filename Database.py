import contrasenas
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
def crear_tablas():
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user=contrasenas.user,
        password=contrasenas.contraseña,
        database="restaurante"
    )

    # Verificar si las tablas necesarias ya existen
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    
    tables = [table[0] for table in cursor.fetchall()]
    if 'mesas' in tables and 'productos' in tables and 'facturas' in tables and 'detalle_factura' in tables:
        print("Las tablas ya existen")
        cursor.close()
        conn.close()
        return

    # Creación de las tablas necesarias
    cursor = conn.cursor()

    # Tabla 'mesas'
    cursor.execute('''CREATE TABLE mesas
                 (id INT PRIMARY KEY AUTO_INCREMENT,
                 capacidad VARCHAR(20));''')

    # Tabla 'productos'
    cursor.execute('''CREATE TABLE productos
                 (id INT PRIMARY KEY AUTO_INCREMENT,
                 nombre VARCHAR(50),
                 precio INT);''')

    # Tabla 'facturas'
    cursor.execute('''CREATE TABLE facturas
                 (id INT PRIMARY KEY AUTO_INCREMENT,
                 mesa_id INT,
                 fecha DATE,
                 FOREIGN KEY(mesa_id) REFERENCES mesas(id));''')

    # Tabla 'detalle_factura'
    cursor.execute('''CREATE TABLE detalle_factura
                 (id INT PRIMARY KEY AUTO_INCREMENT,
                 factura_id INT,
                 producto_id INT,
                 cantidad INT,
                 FOREIGN KEY(factura_id) REFERENCES facturas(id),
                 FOREIGN KEY(producto_id) REFERENCES productos(id));''')

    # Cierre de la conexión
    cursor.close()
    conn.close()

def agregar_datos(valores, tabla):
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user=contrasenas.user,
        password=contrasenas.contraseña,
        database="restaurante"
    )

    # Insertar los datos en la tabla correspondiente
    cursor = conn.cursor()
    cursor.execute(f"DESCRIBE {tabla}")
    column_names = [column[0] for column in cursor.fetchall()]

    # Omitir el campo 'id' si existe en la tabla y es autoincremental
    if 'id' in column_names:
        column_names.remove('id')

    columns = ', '.join(column_names)

    # Si valores es un solo valor, conviértelo a una lista con un solo elemento
    if not isinstance(valores, (list, tuple, dict)):
        valores = [valores]

    placeholders = ', '.join(['%s'] * len(valores))

    query = f"INSERT INTO {tabla} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, valores)
    conn.commit()

    # Cierre de la conexión
    cursor.close()
    conn.close()

    # Mostrar un mensaje indicando que se ha agregado el registro correctamente
    return f"Se ha agregado el registro correctamente en la tabla {tabla}"




def traer_datos(table_widget, table_name):
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user=contrasenas.user,
        password=contrasenas.contraseña,
        database="restaurante"
    )

    cursor = conn.cursor()

    # Ejecutar la consulta para obtener los datos de la tabla especificada
    query = f"SELECT * FROM {table_name};"
    cursor.execute(query)
    result_set = cursor.fetchall()

    # Establecer el número de filas y columnas de la tabla
    num_rows = len(result_set)
    num_cols = len(result_set[0]) if num_rows > 0 else 0
    table_widget.setRowCount(num_rows)
    table_widget.setColumnCount(num_cols)

    # Llenar la tabla con los datos de la consulta
    for row_idx, row_data in enumerate(result_set):
        for col_idx, cell_data in enumerate(row_data):
            item = QTableWidgetItem(str(cell_data))
            table_widget.setItem(row_idx, col_idx, item)

    cursor.close()
    conn.close()

