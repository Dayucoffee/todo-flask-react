from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager 
from sqlalchemy import MetaData #new line


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

#new line
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))


migrate = Migrate(app, db,)
login = LoginManager(app) #new line
login.login_view = 'auth.login'


# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

# blueprint for non-authentication parts of the app
from .task import task as task_blueprint
app.register_blueprint(task_blueprint)

from core import views, models
