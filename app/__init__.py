from app.models import db, User
from flask import Flask, Blueprint
from app.config import Configuration
from flask_migrate import Migrate
# from app.routes import session
from flask_login import LoginManager
from flask_restful import Api
from app.routes import initialize_routes
from app.seeds import seed
from app.schemas import ma

# creates the Flask instance.
# __name__ is the name of the current Python module.
# The app needs to know where it’s located to set up some paths,
# and __name__ is a convenient way to tell it that.
app = Flask(__name__)

# create a blueprint namespace of api for all backend routes
api_bp = Blueprint('api', __name__, url_prefix="/api")
# create api instance to add CRUD resources and create RESTful routes
api = Api(api_bp)

# use the built-in config dictionary from the Flask object named app
# update this config dictionary with the properties of the Configuration class
# in config module
app.config.from_object(Configuration)

# blueprint is just a way to organize routes into "subroutes"
# register these blueprints so the subroute prefixes can be used
# app.register_blueprint(session.bp)
app.register_blueprint(api_bp)

# Configure the application with SQLAlchemy
db.init_app(app)
# Configure the application with marshmallow
ma.init_app(app)
# add all the resources to build routes
initialize_routes(api)

# initialize a migration instance, provides access to flask db commands
# including flask db init to create the migration repo, flask db migrate to
# create a migration, and flask db upgrade to migrate
migrate = Migrate(app, db)


# create cli command to seed database
@app.cli.command("db_seed")
def db_seed():
    seed(db)

# login = LoginManager(app)
# login.login_view = "session.login"


# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))

