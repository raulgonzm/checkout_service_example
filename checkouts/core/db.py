# Python imports
# Flask imports
# Third-Party imports
# Project Imports


def init_db(db):
    db.create_all()
    db.session.commit()
