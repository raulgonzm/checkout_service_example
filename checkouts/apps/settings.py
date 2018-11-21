# Python imports
import os
# Flask imports
# Third-Party imports
# Project imports


base_dir = os.path.abspath(os.path.dirname(__file__))


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
    SERVER_PORT = 9000
    SERVER_BIND_ADDRESS = "0.0.0.0"
    DATABASE_NAME = get_env_variable('DATABASE_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(base_dir, DATABASE_NAME)}"


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    pass


class ItgConfig(Config):
    pass


class LocalConfig(Config):
    pass


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    TESTING = True
    DATABASE_NAME = "test.db"
    SQLALCHEMY_CONTEXT_ON_EXCEPTION = False


config_by_name = dict(
    test=TestConfig,
    local=LocalConfig,
    itg=ItgConfig,
    stg=StagingConfig,
    prod=ProductionConfig,
)
