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

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)

    try:
        print(f'I am here')
        from crud_server.modules.api.routes.show_routes import show_blue_print
        from crud_server.modules.api.routes.all_routes import all_blue_print
    except ModuleNotFoundError as err:
        print(f'I am there')
        from modules.api.routes.show_routes import show_blue_print
        from modules.api.routes.all_routes import all_blue_print

    app.register_blueprint(show_blue_print)
    app.register_blueprint(all_blue_print)

    app.add_url_rule('/', endpoint='index')

    return app
