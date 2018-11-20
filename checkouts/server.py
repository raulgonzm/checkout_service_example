# Python imports
# Flask imports
# Third-Party imports
from flask_restful import Api
# Project imports
from apps import CheckoutApp
from core import db as db_handler
from apps.settings import get_env_variable

app, db = CheckoutApp(env=get_env_variable("ENV"))
db_handler.init_db(db=db)


if __name__ == "__main__":
    from apps.urls import Router
    Router(Api(app))
    app.run(
        host='0.0.0.0',
        port=9000,
        debug=True
    )


