from flask import Flask

from api.views.bookings_views import staff_blueprint as staff_blueprint


def create_app():

    app = Flask(__name__)

    app.register_blueprint(staff_blueprint)

    return app
