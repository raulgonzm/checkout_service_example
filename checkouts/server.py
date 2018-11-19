# Python imports
# Flask imports
# Third-Party imports
from flask_restful import Api
# Project imports
from apps import app

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=9000,
        debug=True
    )


