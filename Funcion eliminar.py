import mysql.connector

def eliminar():
    # Establecer la conexión a la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Ropa')

    # Verificar si la conexión está establecida
    if cnx and cnx.is_connected():
        try:
            # Obtener detalles de la eliminación del usuario
            print("Introduce el nombre de la tabla")
            Tabla = input()

            print("Introduce el Product id")
            Product_id = input()

            # Crear y ejecutar la consulta SQL para eliminar el registro
            query = f"DELETE FROM {Tabla} WHERE Product_id = {Product_id};"
            with cnx.cursor() as cursor:
                cursor.execute(query)

            # Confirmar los cambios realizados
            cnx.commit()
            print("Eliminación exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar la conexión
            cnx.close()

    else:
        print("Could not connect")

def actualizar():
    # Establecer la conexión a la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Ropa')

    # Verificar si la conexión está establecida
    if cnx and cnx.is_connected():
        try:
            # Obtener detalles de la actualización del usuario
            print("Introduce el nombre de la tabla")
            Tabla = input()

            print("Introduce el Product id")
            Product_id = input()

            print("Introduce la columna a cambiar")
            Column = input()

            print("Introduce el Nuevo valor")
            Nuevo_valor = input()

            # Crear y ejecutar la consulta SQL usando placeholders
            query = f"UPDATE {Tabla} SET {Column} = %s WHERE Product_id = %s;"
            with cnx.cursor() as cursor:
                cursor.execute(query, (Nuevo_valor, Product_id))

            # Confirmar los cambios realizados
            cnx.commit()
            print("Actualización exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar la conexión
            cnx.close()

    else:
        print("Could not connect")

def insertar():
    # Establecer la conexión a la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Ropa')

    # Verificar si la conexión está establecida
    if cnx and cnx.is_connected():
        try:
            # Obtener detalles de la actualización del usuario
            print("Introduce el nombre de la tabla")
            Tabla = input()

            print("Introduce el Product id")
            Product_id = None
            res1 = None
            value1 = True
            while value1:
                try:
                    respuesta1 = input()
                    Product_id = int(respuesta1)
                    if isinstance(Product_id, int):
                        value1 = False
                except ValueError:
                    print("Ingresa un número entero")


            print("Introduce la talla (Número entero)")
            talla = None
            res2 = None
            value2 = True
            while value2:
                try:
                    respuesta2 = input()
                    talla = int(respuesta2)
                    if isinstance(talla, int):
                        value2 = False
                except ValueError:
                    print("Ingresa un número entero")
            

            print("Introduce el color (Número entero)")
            color = None
            res3 = None
            value3 = True
            while value3:
                try:
                    respuesta3 = input()
                    color = int(respuesta3)
                    if isinstance(color, int):
                        value3 = False
                except ValueError:
                    print("Ingresa un número entero")
            
            print("Introduce la sexo (Número entero)")
            sexo = None
            res4 = None
            value4 = True
            while value4:
                try:
                    respuesta4 = input()
                    sexo = int(respuesta4)
                    if isinstance(sexo, int):
                        value4 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el temp_id (Número entero)")
            temp = None
            res5 = None
            value5 = True
            while value5:
                try:
                    respuesta5 = input()
                    temp = int(respuesta5)
                    if isinstance(temp, int):
                        value5 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el Pais (Número entero)")
            pais = None
            res6 = None
            value6 = True
            while value6:
                try:
                    respuesta6 = input()
                    pais = int(respuesta6)
                    if isinstance(pais, int):
                        value6 = False
                except ValueError:
            print("Ingresa un número entero")
             print("Introduce el id de la sucursal (Número entero)")
            suc = None
            res7 = None
            value7 = True
            while value7:
                try:
                    respuesta7 = input()
                    suc = int(respuesta7)
                    if isinstance(suc, int):
                        value7 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id de la rec (Número entero)")
            rec = None
            res8 = None
            value8 = True
            while value8:
                try:
                    respuesta8 = input()
                    rec = int(respuesta8)
                    if isinstance(rec, int):
                        value8 = False
                except ValueError:
                    print("Ingresa un número entero")


            print("Introduce el id del departamento (Número entero)")
            dep = None
            res9 = None
            value9 = True
            while value9:
                try:
                    respuesta9 = input()
                    dep = int(respuesta9)
                    if isinstance(dep, int):
                        value9 = False
                except ValueError:
                    print("Ingresa un número entero")
            
            print("Introduce el id del com (Número entero)")
            Com = None
            res10 = None
            value10 = True
            while value10:
                try:
                    respuesta10 = input()
                    Com = int(respuesta10)
                    if isinstance(Com, int):
                        value10 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del Mat (Número entero)")
            Mat = None
            res11 = None
            value11 = True
            while value11:
                try:
                    respuesta11 = input()
                    Mat = int(respuesta11)
                    if isinstance(Mat, int):
                        value11 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del desc (Número entero)")
            desc = None
            res12 = None
            value12 = True
            while value12:
                try:
                    respuesta12 = input()
                    desc = int(respuesta12)
                    if isinstance(desc, int):
                        value12 = False
                except ValueError:
                    print("Ingresa un número entero")
            
            print("Introduce el id del MS (Número entero)")
            ms = None
            res13 = None
            value13 = True
            while value13:
                try:
                    respuesta13 = input()
                    ms = int(respuesta13)
                    if isinstance(ms, int):
                        value13 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el precio (Número decimal)")
            precio = None
            res14 = None
            value14 = True
            while value14:
                try:
                    respuesta14 = input()
                    precio = float(respuesta13)
                    if isinstance(precio, float):
                        value14 = False
                except ValueError:
                    print("Ingresa un número entero")
            print("Introduce la fecha")
            fecha = input()
            print("Introduce el id de Acepta DEV (Número entero)")
            dev = None
            res15 = None
            value15 = True
            while value15:
                try:
                    respuesta15 = input()
                    dev = int(respuesta15)
                    if isinstance(dev, int):
                        value15 = False
                except ValueError:
                    print("Ingresa un número entero")


            # Crear y ejecutar la consulta SQL usando placeholders´
            query = f"INSERT INTO {Tabla} VALUES ({Product_id}, {talla}, {color}, {sexo}, {temp}, {pais}, {suc}, {rec}, {dep}, {Com}, {Mat}, {desc}, {ms}, {precio}, {fecha}, {dev} )"
            with cnx.cursor() as cursor:
                cursor.execute(query, (Nuevo_valor, Product_id))

            # Confirmar los cambios realizados
            cnx.commit()
            print("Actualización exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar la conexión
            cnx.close()

    else:
        print("Could not connect")


value = True
filt = None
while value:
    print("Qué deseas hacer?")
    print("1.-Eliminar un elemento de la tabla")
    print("2.-Actualizar un elemento de la tabla")
    print("3.-Ingresar un valor a la tabla")
    try:
        respuesta = input()
        filt = int(respuesta)
        if isinstance(filt, int) and (filt > 0 and filt < 4):
            value = False
            print("opción válida.")
        else:
            print("Ingresa una opción válida.")

    except ValueError:
        print("Ingresa una opción válida.")

if filt == 1:
    eliminar()
elif filt == 2:
    actualizar()
else:
    insertar()


