"""Module with routes for app authentication"""

import os
from datetime import datetime

from flask import (Blueprint, Response,
                   make_response, jsonify,
                   request, abort)


try:
    # Used for server setup using command line
    from spa_oauth.backend.modules.api.database_connection import connection, cursor
    from spa_oauth.backend.modules.api.status_codes import StatusCodes
    from spa_oauth.backend.modules.database.database_interactions import (close_connection,
                                                                          connect_to_database)
    from spa_oauth.backend.modules.database.document import Document
    from spa_oauth.backend.modules.database.user import User
    from spa_oauth.backend.modules.database.task import Task
    from spa_oauth.backend.modules.database.factory import Factory

    from spa_oauth.backend.modules.api.schemas import (AddNewUser, AddNewDocument,
                                                       AddNewTask, UpdateTableSchema,
                                                       AddNewFactory)
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

