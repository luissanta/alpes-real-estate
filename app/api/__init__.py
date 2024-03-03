import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import app.moduls.lists.aplication
    #import aeroalpes.modulos.vuelos.aplicacion

def importar_modelos_alchemy():
    import app.moduls.lists.infrastructure.dto
    

def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    #import threading
    # import app.moduls.lists.infrastructure.co as cliente
    # import aeroalpes.modulos.hoteles.infraestructura.consumidores as hoteles
    # import aeroalpes.modulos.pagos.infraestructura.consumidores as pagos
    # import aeroalpes.modulos.precios_dinamicos.infraestructura.consumidores as precios_dinamicos
    # import aeroalpes.modulos.vehiculos.infraestructura.consumidores as vehiculos
    import app.moduls.lists.infrastructure.consumers as list_consumer
    import threading
    # Suscripción a eventos
    # threading.Thread(target=cliente.suscribirse_a_eventos).start()
    # threading.Thread(target=hoteles.suscribirse_a_eventos).start()
    # threading.Thread(target=pagos.suscribirse_a_eventos).start()
    # threading.Thread(target=precios_dinamicos.suscribirse_a_eventos).start()
    # threading.Thread(target=vehiculos.suscribirse_a_eventos).start()
    threading.Thread(target=list_consumer.suscribirse_a_eventos).start()

    # # Suscripción a comandos
    # threading.Thread(target=cliente.suscribirse_a_comandos).start()
    # threading.Thread(target=hoteles.suscribirse_a_comandos).start()
    # threading.Thread(target=pagos.suscribirse_a_comandos).start()
    # threading.Thread(target=precios_dinamicos.suscribirse_a_comandos).start()
    # threading.Thread(target=vehiculos.suscribirse_a_comandos).start()
    threading.Thread(target=list_consumer.suscribirse_a_comandos).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from app.config.db import init_db
    init_db(app)

    from app.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        #if not app.config.get('TESTING'):
        comenzar_consumidor()

     # Importa Blueprints
    from . import list_router
    # from . import hoteles
    # from . import pagos
    # from . import precios_dinamicos
    # from . import vehiculos
    # from . import vuelos

    # Registro de Blueprints
    app.register_blueprint(list_router.bp)
    # app.register_blueprint(hoteles.bp)
    # app.register_blueprint(pagos.bp)
    # app.register_blueprint(precios_dinamicos.bp)
    # app.register_blueprint(vehiculos.bp)
    # app.register_blueprint(vuelos.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app


# from .health_check_router import health_check_router
# from .list_router import list_router

# from flask import Flask 
# from app.seedwork.presentation import apiflask
# from flask_cors import CORS
# from config import settings
# import logging


# #app = create_app('default')
# app = Flask(__name__)
# app_context = app.app_context()
# app_context.push()
# app.title = settings.PROJECT_NAME
# app.version = settings.PROJECT_VERSION

# cors = CORS(app)

# logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# # Importa Blueprints
# from . import list_router

# # Registro de Blueprints
# app.register_blueprint(list_router.bp)

# #app_test = app


