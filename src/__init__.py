import os
import mimetypes
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

from flask import Flask
from flask_migrate import Migrate

from src.database import db
from src.entidades import entidades_bp
from src.spa import spa_bp


def create_app() -> Flask:
    """
    Cria e inicializa a aplicação Flask.
    :return: Flask
    """

    # Cria a instância da aplicação Flask.
    app = Flask(__name__, instance_relative_config=True)

    # Configura a aplicação Flask.
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # Inicializa o gerenciador de banco de dados (SQLAlchemy).
    db.app = app
    db.init_app(app)
    db.create_all()
    Migrate(app, db)

    # Registra os Blueprints das rotas da aplicação.
    app.register_blueprint(entidades_bp)
    app.register_blueprint(spa_bp)

    # Retorna a aplicação Flask.
    return app
