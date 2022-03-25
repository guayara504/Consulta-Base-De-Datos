import mysql.connector as sql
import Consultas
import msvcrt

totalJuzgados = 571
consulta = Consultas.consultas
conexion = sql.connect(
            host = "192.168.0.19", 
            user = "jfsarmiento", 
            passwd = "Jfs_red07$14",
            database = "zortekv3")

try:
    print("-"*15)
    print("Unificada")
    cursor = conexion.cursor()
    cursor.execute(consulta.unificada)
    consultasBD  = [item for item in cursor.fetchall()]
    if len(consultasBD) == 1:
        print("Total: 0")
    else:
        for consultaBD in consultasBD[1:]:
            print(consultaBD,"\n")
    print("-"*15)

    print("Total Juzgados")
    cursor.execute(consulta.juzgadoscount)
    cantidadJuzgados  =int(len(list(cursor.fetchall())))

    if cantidadJuzgados != totalJuzgados:
        cursor.execute(consulta.juzgados)
        consultasBD  = [item[0] for item in cursor.fetchall()]
        for consultaBD in consultasBD[totalJuzgados-1:]:
            print(consultaBD,"\n")
    else:
        print("Total: 0")
    print("-"*15)

    print("Ciudades")
    cursor.execute(consulta.ciudades)
    consultasBD  = [item[0] for item in cursor.fetchall()]
    if len(consultasBD) == 0:
        print("Total: 0")
    else:
        for consultaBD in consultasBD:
            print(consultaBD,"\n")
    print("-"*15)

    print("--Consulta hecha con exito--")
    print("-"*15)
    print("--Presione una tecla para cerrar--")
    msvcrt.getch()
except:
    print("\nNo Hubo conexion con la base de datos...")
    msvcrt.getch()