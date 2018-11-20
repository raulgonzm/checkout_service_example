# Python imports
import os
# Flask imports
# Third-Party imports
# Project imports


def get_env_variable(var_name):
    try:
        return os.getenv(var_name)
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise EnvironmentError(error_msg)


class Config:
    ENV = get_env_variable("ENV")
    SECRET_KEY = get_env_variable("SECRET_KEY")
    DEBUG = get_env_variable("DEBUG")
    DATABASE_NAME = get_env_variable('DATABASE_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    pass


class IntegrationConfig(Config):
    pass


class ItgConfig(Config):
    pass


class LocalConfig(Config):
    pass


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DATABASE_NAME = "test.db"
