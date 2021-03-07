"""Module for starting app"""

from flask import Flask


def create_app(test_config=None) -> Flask:
    """
    Creates app

    :param test_config: config for the flask app
    :return: app function
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(SECRET_KEY='dev')

    if test_config:
        app.config.update(test_config)

    try:
        from frontend_backend_servers.frontend.modules.api.routes.show_routes import show_blue_print
        from frontend_backend_servers.frontend.modules.api.routes.change_routes import change_blue_print
        from frontend_backend_servers.frontend.modules.api.routes.add_routes import add_blue_print
        from frontend_backend_servers.frontend.modules.api.routes.delete_routes import delete_blue_print
    except ModuleNotFoundError as err:
        from modules.api.routes.show_routes import show_blue_print
        from modules.api.routes.change_routes import change_blue_print
        from modules.api.routes.add_routes import add_blue_print
        from modules.api.routes.delete_routes import delete_blue_print

    app.register_blueprint(show_blue_print)
    app.register_blueprint(change_blue_print)
    app.register_blueprint(add_blue_print)
    app.register_blueprint(delete_blue_print)

    app.add_url_rule('/', endpoint='index')

    return app
