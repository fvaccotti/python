from flask import Flask, request, url_for, redirect, abort
from flask.templating import render_template
app = Flask(__name__) #el nombre del archivo que estas usando

import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chufa110309!",
    database="prueba"
)

cursor = midb.cursor(dictionary=True) #devuelve tipo json

@app.route('/')
def index():
    return 'hola mundo'

#GET, POST, PUT (actualizar todo un recurso), PATCH(actualizar parcialmente), DELETE
#Se puede dejar que una sola funcion maneje los dos metodos o mas, o bien hacer una por cada una
@app.route('/post/<post_id>', methods=['GET', 'POST']) #parametro en la url es post_id. Puedo poner <int:post_id> y le fuerzo el tipo de dato
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este no es un GET'

@app.route('/lele', methods=['POST', 'GET'])
def lele():
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    #abort(401)
    #return redirect(url_for('lala', post_id=2)) #le indico a que funcion lo quiero reenviar. Con redirect necesito SIEMPRE un return
    #print(request.form)
    #print(request.form['llave1'])
    #print(request.form['llave2'])
    #return render_template('lele.html') #para redireccionar a algun html. Render_template va a buscar una carpeta templates dentro del proyecto
    #return { #objeto json
     #   "username": 'Chanchito Feliz',
      #  "email": 'chanchito@feliz.com'
   # }
    return render_template('lele.html', usuarios=usuarios)
    
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola Mundo') #mensaje es el valor del parametro. Desde el html se levanta con {{ nombre_variable }}

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = "insert into Usuario (username, email, edad) values (%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for('lele'))
    return render_template('crear.html')