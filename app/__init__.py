from flask import Flask
from config import Config
from flask_login import LoginManager
from app.models import db, User
from flask_migrate import Migrate
from flask_moment import Moment
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
migrate = Migrate(app, db)


# Import and register bluprints later (auth, etc)

from app.blueprints.main import main
from app.blueprints.auth import auth


app.register_blueprint(main)
app.register_blueprint(auth)


from app import routes