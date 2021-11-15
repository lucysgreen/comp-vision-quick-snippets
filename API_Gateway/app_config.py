"""Class-based Flask app configuration."""

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config(object):
    """Initialisation of config for classes."""

    FLASK_APP = "wsgi.py"

    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    '''Takes the Production Config of our app.'''
    
    FLASK_ENV = 'Production'
    ENV = 'Production'

    SECRET_KEY = environ.get("PROD_SECRET_KEY")

    # API URLs - The root urls of each service - must not have '/' at end.

    TRANSLATE_API_URL = "0.0.0.0/5000"
    IDENTIFY_API_URL = "0.0.0.0/5000"
    SENTIMENT_API_URL = "0.0.0.0/5000"
    REDACT_API_URL = "0.0.0.0/5000"
    FACIAL_RECOGNITION_API_URL = "0.0.0.0/5000"

class DevelopmentConfig(Config):
    '''Configures the Development Config of our app.'''

    DEBUG = True

    FLASK_ENV = 'Development'
    ENV = 'Development'

    SECRET_KEY = environ.get('DEV_SECRET_KEY')

    # API URLs

    TRANSLATE_API_URL = "0.0.0.0/5000"  # The root url of our translate API. Must not have '/' at end.


class TestingConfig(Config):
    '''Configures the Testing Config of our app.'''

    TESTING = True

    FLASK_ENV = 'Testing'
    ENV = 'Testing'

    SECRET_KEY = environ.get('TEST_SECRET_KEY')

    # API URLs

    TRANSLATE_API_URL = "0.0.0.0/5000"  # The root url of our translate API. Must not have '/' at end.

# It is good practice to specify configurations for different environments.
# Below, we consolidate these configuration names into a dictionary.

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}