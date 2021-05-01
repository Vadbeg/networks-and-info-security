"""Module with routes for app authentication"""

import os

from flask import (Blueprint, Response,
                   request, abort)


try:
    # Used for server setup using command line
    from spa_oauth.backend.modules.api.database_connection import connection, cursor
    from spa_oauth.backend.modules.api.status_codes import StatusCodes
    from spa_oauth.backend.modules.database.database_interactions import (close_connection,
                                                                          connect_to_database)
    from spa_oauth.backend.modules.database.app_user import AppUser
    from spa_oauth.backend.modules.database.factory import Factory

    from spa_oauth.backend.modules.api.schemas import AddNewAppUser
except ModuleNotFoundError as err:
    # Used for server setup using Docker
    from modules.api.database_connection import connection, cursor
    from modules.api.status_codes import StatusCodes
    from modules.database.database_interactions import close_connection, connect_to_database
    from modules.database.document import Document
    from modules.database.user import User
    from modules.database.task import Task
    from modules.database.factory import Factory

    from modules.api.schemas import (AddNewUser, AddNewDocument,
                                     AddNewTask, UpdateTableSchema,
                                     AddNewFactory)


auth_blue_print = Blueprint('auth_app', __name__, url_prefix=os.environ['API_PREFIX'])


@auth_blue_print.route('/auth/register', methods=("GET", "POST"))
def register_user():
    """View for user registration"""

    if request.method == 'POST':
        add_new_app_user_schema = AddNewAppUser()

        errors = add_new_app_user_schema.validate(data=request.form)

        if errors:
            abort(StatusCodes.BadRequest, str(errors))

        args = add_new_app_user_schema.dump(request.form)

        app_user = AppUser(connection=connection, cursor=cursor)
        new_user_id = app_user.add_app_user(
            email=args['email'],
            password=args['password']
        )

        auth_token = app_user.encode_auth_token(user_id=new_user_id)

        response_payload = {
            'status': 'success',
            'message': 'Successfully registered.',
            'auth_token': auth_token.decode()
        }

        return Response(
            response_payload,
            status=StatusCodes.Created
        )
