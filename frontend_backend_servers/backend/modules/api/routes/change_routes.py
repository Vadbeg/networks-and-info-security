"""Module with routes for Flask application"""

import os
from datetime import datetime

from flask import (Blueprint, Response,
                   render_template,
                   make_response, jsonify,
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


change_blue_print = Blueprint('change_documentation', __name__, url_prefix=os.environ['API_PREFIX'])


@change_blue_print.route('/change_document/<int:document_idx>', methods=("GET", "POST"))
def change_document(document_idx: int):
    """View for document changing"""

    document = Document(connection=connection, cursor=cursor)

    document_to_change = document.get_document_by_id(document_id=document_idx)

    document_to_change['date_of_creation'] = datetime.strftime(document_to_change['date_of_creation'],
                                                               '%Y-%m-%d')
    document_to_change['date_of_registration'] = datetime.strftime(document_to_change['date_of_registration'],
                                                                   '%Y-%m-%d')

    document_controllers = [curr_controller['id'] for curr_controller in document_to_change['controllers']]
    document_creators = [curr_controller['id'] for curr_controller in document_to_change['creators']]

    user = User(connection=connection, cursor=cursor)
    all_users = user.get_all_users()

    for curr_user in all_users:
        if curr_user['id'] in document_controllers:
            curr_user['is_in_controllers'] = True
        else:
            curr_user['is_in_controllers'] = False

        if curr_user['id'] in document_creators:
            curr_user['is_in_creators'] = True
        else:
            curr_user['is_in_creators'] = False

    context = {
        'all_users': all_users,
        'document': document_to_change
    }

    if request.method == 'POST':
        creators_ids = request.form.getlist('choose_creators')  # if there is no such name, returns empty list
        controllers_ids = request.form.getlist('choose_controllers')

        request_form = dict(request.form)
        request_form.pop('choose_creators')  # there is no need in it now
        request_form.pop('choose_controllers')

        request_form['creators_ids'] = creators_ids
        request_form['controllers_ids'] = controllers_ids

        request_form['date_of_creation'] = datetime.strptime(request_form['date_of_creation'],
                                                             '%Y-%m-%d')
        request_form['date_of_registration'] = datetime.strptime(request_form['date_of_registration'],
                                                                 '%Y-%m-%d')

        add_new_document_schema = AddNewDocument()
        errors = add_new_document_schema.validate(data=request_form)

        if errors:
            abort(StatusCodes.BadRequest, str(errors))

        args = add_new_document_schema.dump(request_form)

        document = Document(connection=connection, cursor=cursor)

        document.change_document(
            document_id=document_idx,
            document_name=args['document_name'],
            document_type=args['document_type'],
            date_of_creation=args['date_of_creation'],
            date_of_registration=args['date_of_registration'],
            controllers_ids=args['controllers_ids'],
            creators_ids=args['creators_ids'],
        )

        context = {'idx': document_to_change['id']}
        return make_response(jsonify(context), StatusCodes.Created)

    return make_response(jsonify(context), StatusCodes.OK)


@change_blue_print.route('/change_factory/<int:factory_idx>', methods=("GET", "POST"))
def change_factory(factory_idx: int):
    """View for factory changing"""

    factory = Factory(connection=connection, cursor=cursor)

    factory_to_change = factory.get_factory_by_id(factory_id=factory_idx)

    context = {
        'factory': factory_to_change,
    }

    if request.method == 'POST':
        add_new_factory_schema = AddNewFactory()
        errors = add_new_factory_schema.validate(data=request.form)

        if errors:
            abort(StatusCodes.BadRequest, str(errors))

        args = add_new_factory_schema.dump(request.form)

        factory = Factory(connection=connection, cursor=cursor)

        factory.change_factory(
            factory_id=factory_idx,
            factory_name=args['factory_name'],
            size=args['size'],
            city=args['city'],
        )

        context = {'idx': factory_to_change['id']}
        return make_response(jsonify(context), StatusCodes.Created)

    return make_response(jsonify(context), StatusCodes.OK)


@change_blue_print.route('/change_task/<int:task_idx>', methods=("GET", "POST"))
def change_task(task_idx: int):
    """View for task changing"""

    task = Task(connection=connection, cursor=cursor)
    task_to_change = task.get_task_by_id(task_id=task_idx)

    document = Document(connection=connection, cursor=cursor)
    all_documents = document.get_all_documents()

    user = User(connection=connection, cursor=cursor)
    all_users = user.get_all_users()

    factory = Factory(connection=connection, cursor=cursor)
    all_factories = factory.get_all_factories()

    for curr_user in all_users:
        if curr_user['id'] == task_to_change['executor_id']:
            curr_user['is_in_users'] = True
        else:
            curr_user['is_in_users'] = False

    for curr_document in all_documents:
        if curr_document['id'] == task_to_change['document_id']:
            curr_document['is_in_documents'] = True
        else:
            curr_document['is_in_documents'] = False

    for curr_factory in all_factories:
        if curr_factory['id'] == task_to_change['factory_id']:
            curr_factory['is_in_factories'] = True
        else:
            curr_factory['is_in_factories'] = False

    context = {
        'task': task_to_change,
        'all_documents': all_documents,
        'all_users': all_users,
        'all_factories': all_factories
    }

    if request.method == 'POST':

        add_new_task_schema = AddNewTask()
        errors = add_new_task_schema.validate(data=request.form)

        if errors:
            abort(StatusCodes.BadRequest, str(errors))

        args = add_new_task_schema.dump(request.form)

        task = Task(connection=connection, cursor=cursor)

        task.change_task(
            task_id=task_idx,
            task_name=args['task_name'],
            executor_id=args['executor_id'],
            document_id=args['document_id'],
            factory_id=args['factory_id']
        )

        return Response(status=StatusCodes.Created)

    return make_response(jsonify(context), StatusCodes.OK)


@change_blue_print.route('/change_user/<int:user_idx>', methods=("GET", "POST"))
def change_user(user_idx: int):
    """View for user changing"""

    user = User(connection=connection, cursor=cursor)

    user_to_change = user.get_user_by_id(user_id=user_idx)

    context = {
        'user': user_to_change,
    }

    if request.method == 'POST':
        add_new_user_schema = AddNewUser()

        errors = add_new_user_schema.validate(data=request.form)

        if errors:
            abort(StatusCodes.BadRequest, str(errors))

        args = add_new_user_schema.dump(request.form)

        user = User(connection=connection, cursor=cursor)
        user.change_user(
            user_id=user_idx,
            first_name=args['first_name'],
            second_name=args['second_name'],
            is_internal=args['is_internal'],

            position=args['position'],
            email=args['email'],
            phone_number=args['phone_number']
        )

        return Response(status=StatusCodes.Created)

    return make_response(jsonify(context), StatusCodes.OK)

