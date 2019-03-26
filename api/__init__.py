from flask import Flask
from flask_jwt_extended import JWTManager

from api.views.bookings_views import staff_blueprint as staff_blueprint
from api.views.user_views import user_blueprint as user_blueprint


def create_app():

    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'masete'
    JWTManager(app)

    app.register_blueprint(staff_blueprint)
    app.register_blueprint(user_blueprint)

    return app
