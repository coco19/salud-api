# -*- coding: utf-8 -*-

import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql:///salud_dev?client_encoding=utf8')
    # Parámetro que indica si el parser de argumentos debe devolver la totalidad de los errores encontrados en una
    # petición a la API (True), o sólo el primer error (False).
    BUNDLE_ERRORS = True
    # Directorio donde guardaremos el archivo
    UPLOAD_FOLDER = '/tmp'
    ALLOWED_FILE_EXTENSIONS = set(['png'])
    MAX_CONTENT_LENGTH = 6 * 1024 * 1024


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
