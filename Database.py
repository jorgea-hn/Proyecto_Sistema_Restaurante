import mysql.connector

def crear_tablas():
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
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
        user="root",
        password="root",
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
    placeholders = ', '.join(['%s'] * len(valores))

    query = f"INSERT INTO {tabla} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, valores)
    conn.commit()

    # Cierre de la conexión
    cursor.close()
    conn.close()

    # Mostrar un mensaje indicando que se ha agregado el registro correctamente
    print(f"Se ha agregado el registro correctamente en la tabla {tabla}")





