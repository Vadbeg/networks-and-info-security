"""Module with routes for Flask application"""

import os
from datetime import datetime

from flask import (Blueprint, Response,
                   request, abort,
                   jsonify, make_response)

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


add_blue_print = Blueprint('add_documentation', __name__, url_prefix=os.environ['API_PREFIX'])


@add_blue_print.route('/add_user', methods=("GET", "POST"))
def add_user():
    """View for adding new users (form)"""

    if request.method == 'POST':
        add_new_user_schema = AddNewUser()

        errors = add_new_user_schema.validate(data=request.form)

        if errors:
            abort(StatusCodes.BadRequest, str(errors))

        args = add_new_user_schema.dump(request.form)

        user = User(connection=connection, cursor=cursor)
        user.add_user(
            first_name=args['first_name'],
            second_name=args['second_name'],
            is_internal=args['is_internal'],

            position=args['position'],
            email=args['email'],
            phone_number=args['phone_number']
        )

        return Response(status=StatusCodes.Created)

    return Response(status=StatusCodes.BadRequest)


@add_blue_print.route('/add_document', methods=("GET", "POST"))
def add_document():
    """View for adding new documents (form)"""

    if request.method == 'POST':
        creators_ids = request.form.getlist('creators_ids')  # if there is no such name, returns empty list
        controllers_ids = request.form.getlist('controllers_ids')

        request_args = dict(request.form)

        request_args.pop('creators_ids')  # there is no need in it now
        request_args.pop('controllers_ids')

        request_args['creators_ids'] = creators_ids
        request_args['controllers_ids'] = controllers_ids

        request_args['date_of_creation'] = datetime.strptime(request_args['date_of_creation'],
                                                             '%Y-%m-%d')
        request_args['date_of_registration'] = datetime.strptime(request_args['date_of_registration'],
                                                                 '%Y-%m-%d')

        add_new_document_schema = AddNewDocument()
        errors = add_new_document_schema.validate(data=request_args)

        if errors:
            abort(StatusCodes.BadRequest, str(errors))

        args = add_new_document_schema.dump(request_args)

        document = Document(connection=connection, cursor=cursor)
        document.add_document(
            document_name=args['document_name'],
            document_type=args['document_type'],
            date_of_creation=args['date_of_creation'],
            date_of_registration=args['date_of_registration'],
            controllers_ids=args['controllers_ids'],
            creators_ids=args['creators_ids'],
        )

        return Response(status=StatusCodes.Created)

    return Response(status=StatusCodes.BadRequest)


@add_blue_print.route('/add_factory', methods=("GET", "POST"))
def add_factory():
    """View for adding new factories (form)"""

    if request.method == 'POST':
        add_new_factory_schema = AddNewFactory()

        errors = add_new_factory_schema.validate(data=request.form)

        if errors:
            abort(400, str(errors))

        args = add_new_factory_schema.dump(request.form)

        factory = Factory(connection=connection, cursor=cursor)
        factory.add_factory(
            factory_name=args['factory_name'],
            size=args['size'],
            city=args['city']
        )

        return Response(status=StatusCodes.Created)

    return Response(status=StatusCodes.BadRequest)


@add_blue_print.route('/add_task', defaults={'document_idx': None}, methods=("GET", "POST"))
@add_blue_print.route('/add_task/<int:document_idx>', methods=("GET", "POST"))
def add_task(document_idx: int):
    """View for adding new tasks (form)"""

    if request.method == 'POST':

        add_new_task_schema = AddNewTask()
        errors = add_new_task_schema.validate(data=request.form)

        print(request.form)
        print(str(errors))

        if errors:
            abort(400, str(errors))

        args = add_new_task_schema.dump(request.form)

        task = Task(connection=connection, cursor=cursor)

        task.add_task(
            task_name=args['task_name'],
            executor_id=args['executor_id'],
            document_id=args['document_id'],
            factory_id=args['factory_id']
        )

        if document_idx:
            context = {'idx': document_idx}

            return make_response(jsonify(context), StatusCodes.Created)
        else:
            return Response(status=StatusCodes.Created)

    return Response(status=StatusCodes.BadRequest)

