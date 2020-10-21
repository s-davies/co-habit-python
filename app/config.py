import os


class Configuration:
    # get the secret key from the .env file
    # this is used to prevent client side tampering with session data
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # get the database uri from the .env file or use default development database
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "postgresql://co_habit_python:ep3NVJXzCU8NcqQt@localhost/co_habit_python_dev"

    # disable the Flask-SQLAlchemy event system so it doesn't track modifications
    # and use resources, since it isn't being used
    SQLALCHEMY_TRACK_MODIFICATIONS = False
