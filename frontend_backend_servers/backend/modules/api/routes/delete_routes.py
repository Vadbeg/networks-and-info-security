"""Module with functions for items removing"""

import os

from flask import (Blueprint, Response,
                   render_template, jsonify,
                   make_response,
                   request, abort,
                   redirect, url_for)

try:
    # Used for server setup using command line
    from frontend_backend_servers.backend.modules.api.database_connection import connection, cursor
    from frontend_backend_servers.backend.modules.api.status_codes import StatusCodes
    from frontend_backend_servers.backend.modules.database.database_interactions import (close_connection,
                                                                                         connect_to_database)
    from frontend_backend_servers.backend.modules.database.document import Document
    from frontend_backend_servers.backend.modules.database.user import User
    from frontend_backend_servers.backend.modules.database.task import Task
    from frontend_backend_servers.backend.modules.database.factory import Factory

    from frontend_backend_servers.backend.modules.api.schemas import (AddNewUser, AddNewDocument,
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


delete_blue_print = Blueprint('delete_documentation', __name__, url_prefix=os.environ['API_PREFIX'])


@delete_blue_print.route('/delete_document/<int:document_idx>', methods=["GET"])
def delete_document(document_idx: int):
    """View for deleting document"""

    document = Document(connection=connection, cursor=cursor)

    document.delete_document(document_id=document_idx)

    all_documents = document.get_all_documents()

    context = {
        'all_documents': all_documents
    }

    return make_response(jsonify(context), StatusCodes.OK)


@delete_blue_print.route('/delete_factory/<int:factory_idx>', methods=["GET"])
def delete_factory(factory_idx: int):
    """View for deleting factory"""

    factory = Factory(connection=connection, cursor=cursor)

    factory.delete_factory(factory_id=factory_idx)

    all_factories = factory.get_all_factories()

    context = {
        'all_factories': all_factories
    }

    return make_response(jsonify(context), StatusCodes.OK)


@delete_blue_print.route('/delete_task/<int:task_idx>', methods=["GET"])
def delete_task(task_idx: int):
    """View for deleting factory"""

    task = Task(connection=connection, cursor=cursor)

    task.delete_task(task_id=task_idx)

    all_tasks = task.get_all_tasks()

    context = {
        'all_tasks': all_tasks
    }

    return make_response(jsonify(context), StatusCodes.OK)


@delete_blue_print.route('/delete_user/<int:user_idx>', methods=["GET"])
def delete_user(user_idx: int):
    """View for deleting users"""

    user = User(connection=connection, cursor=cursor)
    document = Document(connection=connection, cursor=cursor)

    user.delete_user(user_id=user_idx)
    document.delete_documents_with_no_users_assigned()

    all_users = user.get_all_users()

    context = {
        'all_users': all_users
    }

    return make_response(jsonify(context), StatusCodes.OK)
