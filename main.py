import cx_Oracle

connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

cursor = connection.cursor()
try:

    dp = input("Número de departamento:")
    nombre = input("Nombre departamento:")
    localidad = input("localidad:")

    cursor.callproc("InsertarDEPT", (dp, nombre, localidad))
# call procedure le pasamos insertDEPT y una tupla con los valores de entrada,
 # no tienen que ser los mismos nombres que los de Oarcle
    if cursor.rowcount > 0:
        print("Registro insertado satisfactoriamente")
    else:
        print("Dato no encontrado")



except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()
