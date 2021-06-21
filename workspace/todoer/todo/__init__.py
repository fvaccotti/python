import os

from flask import Flask

def create_app(): #necesaria para crear una aplicacion en Flask
    app = Flask(__name__) #todas las aplicaciones heredan de la clase Flask

    app.config.from_mapping( #utilizar variables de entorno para configurar la aplicacion. Nos permite definir variables de configuracion para usar despues
        SECRET_KEY='mikey', #para definir las sesiones de la aplicacion
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'), 
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'), 
        DATABASE=os.environ.get('FLASK_DATABASE'),  
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)
    
    @app.route('/hola')
    def hola():
        return 'Hola Mundo'
    return app

#para correr Flask no olvidar export FLASK_APP=todo
#flask run
#para pasarlo a dev export FLASK_ENV=development