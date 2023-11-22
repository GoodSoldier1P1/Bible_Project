from flask import Flask
from config import Config
from flask_login import LoginManager
from app.models import db, User
from flask_migrate import Migrate
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)

# Import and register bluprints later (auth, etc)

from app.blueprints.main import main


app.register_blueprint(main)



from app import routes