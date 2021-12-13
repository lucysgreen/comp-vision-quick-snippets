from flask import Flask
from os import environ
import app_config

# Import any globally accessible flask libraries here.
# eg: from flask_sqlalchemy import SQLAlchemy
# eg: db = SQLAlchemy()

def init_app():
    """Initialize the core application."""

    app = Flask(__name__, instance_relative_config=False)

    # Here, we set our config variables based on the 'FLASK_ENV' environment variable.

    if environ.get("FLASK_ENV").replace('"', '') == 'production':
        app.config.from_object('app_config.ProductionConfig')

    elif environ.get("FLASK_ENV").replace('"', '') == 'testing':
        app.config.from_object('app_config.TestingConfig')

    else:
        app.config.from_object('app_config.DevelopmentConfig')

    # Initialise any globally accessible flask libraries here.
    # eg: db.init_app(app)

    # Initialise our app context.
    with app.app_context():

        # Include our application's routes.
        from .redact import redact_blueprint
        from .healthcheck import healthcheck_blueprint

        # Register any application blueprints.
        app.register_blueprint(redact_blueprint.redact_bp)
        app.register_blueprint(healthcheck_blueprint.healthcheck_bp)

        return app