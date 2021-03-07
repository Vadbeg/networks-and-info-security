"""Module with routes for Flask application"""

import os
from datetime import datetime

from flask import (Blueprint,
                   render_template,
                   request, abort,
                   redirect, url_for)

try:
    # Used for server setup using command line
    from frontend_backend_servers.frontend.modules.data_retrieving.document import Document
    from frontend_backend_servers.frontend.modules.data_retrieving.user import User
    from frontend_backend_servers.frontend.modules.data_retrieving.task import Task
    from frontend_backend_servers.frontend.modules.data_retrieving.factory import Factory

    from frontend_backend_servers.frontend.modules.api.schemas import (AddNewUser, AddNewDocument,
                                                                       AddNewTask,
                                                                       AddNewFactory)
except ModuleNotFoundError as err:
    # Used for server setup using Docker
    from modules.data_retrieving.document import Document
    from modules.data_retrieving.user import User
    from modules.data_retrieving.task import Task
    from modules.data_retrieving.factory import Factory

    from modules.api.schemas import (AddNewUser, AddNewDocument,
                                     AddNewTask,
                                     AddNewFactory)

change_blue_print = Blueprint('change_documentation', __name__)


@change_blue_print.route('/change_document/<int:document_idx>', methods=("GET", "POST"))
def change_document(document_idx: int):
    """View for document changing"""

    document = Document(root_uri=os.environ['ROOT_BACKEND_URI'])

    document_to_change, all_document_tasks = document.get_one_document(document_id=document_idx)

    document_to_change['date_of_creation'] = datetime.strptime(document_to_change['date_of_creation'],
                                                               '%Y-%m-%d').date()
    document_to_change['date_of_creation'] = str(document_to_change['date_of_creation'])

    document_to_change['date_of_registration'] = datetime.strptime(document_to_change['date_of_registration'],
                                                                   '%Y-%m-%d').date()
    document_to_change['date_of_registration'] = str(document_to_change['date_of_registration'])

    document_controllers = [curr_controller['id'] for curr_controller in document_to_change['controllers']]
    document_creators = [curr_controller['id'] for curr_controller in document_to_change['creators']]

    user = User(root_uri=os.environ['ROOT_BACKEND_URI'])
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
            abort(400, str(errors))

        args = add_new_document_schema.dump(request_form)

        document = Document(root_uri=os.environ['ROOT_BACKEND_URI'])

        document.change_document(
            document_id=document_idx,
            document_name=args['document_name'],
            document_type=args['document_type'],
            date_of_creation=args['date_of_creation'],
            date_of_registration=args['date_of_registration'],
            controllers_ids=args['controllers_ids'],
            creators_ids=args['creators_ids'],
        )

        return redirect(url_for('show_documentation.show_one_document', idx=document_to_change['id']))

    return render_template('pages/changes/change_document.html', **context)


@change_blue_print.route('/change_factory/<int:factory_idx>', methods=("GET", "POST"))
def change_factory(factory_idx: int):
    """View for factory changing"""

    factory = Factory(root_uri=os.environ['ROOT_BACKEND_URI'])

    factory_to_change = factory.get_one_factory(factory_id=factory_idx)

    context = {
        'factory': factory_to_change,
    }

    if request.method == 'POST':
        add_new_factory_schema = AddNewFactory()
        errors = add_new_factory_schema.validate(data=request.form)

        if errors:
            abort(400, str(errors))

        args = add_new_factory_schema.dump(request.form)

        factory = Factory(root_uri=os.environ['ROOT_BACKEND_URI'])

        factory.change_factory(
            factory_id=factory_idx,
            factory_name=args['factory_name'],
            size=args['size'],
            city=args['city'],
        )

        return redirect(url_for('show_documentation.show_one_factory', idx=factory_to_change['id']))

    return render_template('pages/changes/change_factory.html', **context)


@change_blue_print.route('/change_task/<int:task_idx>', methods=("GET", "POST"))
def change_task(task_idx: int):
    """View for task changing"""

    task = Task(root_uri=os.environ['ROOT_BACKEND_URI'])
    task_to_change = task.get_one_task(task_id=task_idx)

    document = Document(root_uri=os.environ['ROOT_BACKEND_URI'])
    all_documents = document.get_all_documents()

    user = User(root_uri=os.environ['ROOT_BACKEND_URI'])
    all_users = user.get_all_users()

    factory = Factory(root_uri=os.environ['ROOT_BACKEND_URI'])
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
            abort(400, str(errors))

        args = add_new_task_schema.dump(request.form)

        task = Task(root_uri=os.environ['ROOT_BACKEND_URI'])

        task.change_task(
            task_id=task_idx,
            task_name=args['task_name'],
            executor_id=args['executor_id'],
            document_id=args['document_id'],
            factory_id=args['factory_id']
        )

        return redirect(url_for('show_documentation.show_tasks'))

    return render_template('pages/changes/change_task.html', **context)


@change_blue_print.route('/change_user/<int:user_idx>', methods=("GET", "POST"))
def change_user(user_idx: int):
    """View for user changing"""

    user = User(root_uri=os.environ['ROOT_BACKEND_URI'])

    user_to_change = user.get_one_user(user_id=user_idx)

    context = {
        'user': user_to_change,
    }

    if request.method == 'POST':
        add_new_user_schema = AddNewUser()

        errors = add_new_user_schema.validate(data=request.form)

        if errors:
            abort(400, str(errors))

        args = add_new_user_schema.dump(request.form)

        user = User(root_uri=os.environ['ROOT_BACKEND_URI'])
        user.change_user(
            user_id=user_idx,
            first_name=args['first_name'],
            second_name=args['second_name'],
            is_internal=args['is_internal'],

            position=args['position'],
            email=args['email'],
            phone_number=args['phone_number']
        )

        return redirect(url_for('show_documentation.show_users'))

    return render_template('pages/changes/change_user.html', **context)

