from typing import MutableMapping
import mysql.connector

import click #para ejecutar comandos en la terminal en la bd
from flask import current_app, g #current_app mantiene la que esta corriendo, g vive en toda la aplicacion. Entiendo son globales. El usuario se guardara en g
from flask.cli import with_appcontext #trae el contexto de configuracion de la aplicacion, las variables que pusimos en la app.config
from .schema import instructions #el archivo que vamos a definir los scripts

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None) #si db es none es porque nunca se corrio get_db. Es un null

    if db is not None:
        db.close()

def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)
    db.commit()

@click.command('init-db') #flask init-db va a ejecutar esta funcion desde la consola
@with_appcontext #accedera a las variables de mi app
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')

def init_app(app):
    app.teardown_appcontext(close_db) #ejecutara funciones que pasemos como argumento cuando terminemos la ejecucion de alguna funcion o metodo creado. Aca siempre nos aseguramos que se cierre la conexion
    app.cli.add_command(init_db_command)
