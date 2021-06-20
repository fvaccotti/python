import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chufa110309!',
    database='prueba'
)

#el cursor nos permite interacturar con la bd
cursor = mydb.cursor()

cursor.execute('select * from Usuario')

resultado = cursor.fetchall() #para traernos todas las instancias de los elementos que encontro en ese query.
#resultado = cursor.fetchone() #traera el primero que encuentre
print(resultado)

#####Inserts########
#cursor.execute('show create table Usuario') #para ver los campos de la tabla
#sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
#values = ('uncorreo@correo.co.nz', 'NZUser', 34)
#cursor.execute(sql, values) #query con primer parametro, valores con el segundo
#mydb.commit()
#print(cursor.rowcount)

#####Update########
#sql = 'update Usuario set email = %s where id = %s'
#values = ('micorreo@correo.com ', 4)
#cursor.execute(sql, values)
#mydb.commit()

#####Delete########
#sql = 'delete from Usuario where id = %s'
#values = (5, ) #siempre tiene que ser una tupla con este formato
#cursor.execute(sql, values)
#mydb.commit()

#Limitar el size
cursor.execute('select * from Usuario limit 2')

resultado = cursor.fetchall() #para traernos todas las instancias de los elementos que encontro en ese query.
#resultado = cursor.fetchone() #traera el primero que encuentre
print(resultado)