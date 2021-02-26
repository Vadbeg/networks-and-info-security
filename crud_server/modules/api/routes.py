"""Module with routes for Flask application"""

import os
import time
from datetime import datetime

import psycopg2
from flask import (Blueprint, Flask,
                   render_template,
                   request, abort,
                   redirect, url_for)

try:
    # Used for server setup using command line
    from crud_server.modules.database.database_interactions import close_connection, connect_to_database
    from crud_server.modules.database.document import Document
    from crud_server.modules.database.user import User
    from crud_server.modules.database.task import Task
    from crud_server.modules.database.factory import Factory

    from crud_server.modules.api.schemas import (AddNewUser, AddNewDocument,
                                                 AddNewTask, UpdateTableSchema,
                                                 AddNewFactory)
except ModuleNotFoundError as err:
    # Used for server setup using Docker
    from modules.database.database_interactions import close_connection, connect_to_database
    from modules.database.document import Document
    from modules.database.user import User
    from modules.database.task import Task
    from modules.database.factory import Factory

    from modules.api.schemas import (AddNewUser, AddNewDocument,
                                     AddNewTask, UpdateTableSchema,
                                     AddNewFactory)


blue_print = Blueprint('documentation', __name__)

database_host = os.getenv('DATABASE_HOST', default='localhost')
database_port = os.getenv('DATABASE_PORT', default='5432')
database_user = os.getenv('DATABASE_USER', default='user')
database_password = os.getenv('DATABASE_PASSWORD', default='password')
database_name = os.getenv('DATABASE_NAME', default='database')

connection, cursor = connect_to_database(host=database_host,
                                         port=database_port,
                                         user=database_user,
                                         password=database_password,
                                         database=database_name)


@blue_print.route('/')
@blue_print.route('/home')
def home():
    """Home tab"""

    return render_template('pages/home.html')


@blue_print.route('/users')
def show_users():
    """View with users table"""

    user = User(connection=connection, cursor=cursor)

    all_users = user.get_all_users()

    context = {
        'all_users': all_users
    }

    return render_template('pages/tables/users.html', **context)


@blue_print.route('/documents')
def show_documents():
    """View with documents table"""

    document = Document(connection=connection, cursor=cursor)

    all_documents = document.get_all_documents()

    context = {
        'all_documents': all_documents
    }

    return render_template('pages/tables/documents.html', **context)


@blue_print.route('/factories')
def show_factories():
    """View with factories table"""

    factory = Factory(connection=connection, cursor=cursor)

    all_factories = factory.get_all_factories()

    context = {
        'all_factories': all_factories
    }

    return render_template('pages/tables/factories.html', **context)


@blue_print.route('/add_user', methods=("GET", "POST"))
def add_user():
    """View for adding new users (form)"""

    if request.method == 'POST':
        add_new_user_schema = AddNewUser()

        errors = add_new_user_schema.validate(data=request.form)

        if errors:
            abort(400, str(errors))

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

        return redirect(url_for('documentation.home'))

    return render_template('pages/inputs/add_user.html')


@blue_print.route('/add_document', methods=("GET", "POST"))
def add_document():
    """View for adding new documents (form)"""

    user = User(connection=connection, cursor=cursor)
    all_users = user.get_all_users()

    context = {
        'all_users': all_users
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

        document = Document(connection=connection, cursor=cursor)
        document.add_document(
            document_name=args['document_name'],
            document_type=args['document_type'],
            date_of_creation=args['date_of_creation'],
            date_of_registration=args['date_of_registration'],
            controllers_ids=args['controllers_ids'],
            creators_ids=args['creators_ids'],
        )

        return redirect(url_for('documentation.show_documents'))

    return render_template('pages/inputs/add_document.html', **context)


@blue_print.route('/add_factory', methods=("GET", "POST"))
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

        return redirect(url_for('documentation.home'))

    return render_template('pages/inputs/add_factory.html')


@blue_print.route('/add_task', defaults={'document_idx': None}, methods=("GET", "POST"))
@blue_print.route('/add_task/<int:document_idx>', methods=("GET", "POST"))
def add_task(document_idx: int):
    """View for adding new tasks (form)"""

    document = Document(connection=connection, cursor=cursor)

    if document_idx:
        all_documents = document.get_document_by_id(document_id=document_idx)
        all_documents = [all_documents]
    else:
        all_documents = document.get_all_documents()

    user = User(connection=connection, cursor=cursor)
    all_users = user.get_all_users()

    factory = Factory(connection=connection, cursor=cursor)
    all_factories = factory.get_all_factories()

    context = {
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

        task = Task(connection=connection, cursor=cursor)

        task.add_task(
            task_name=args['task_name'],
            executor_id=args['executor_id'],
            document_id=args['document_id'],
            factory_id=args['factory_id']
        )

        if document_idx:
            return redirect(url_for('documentation.show_one_document', idx=document_idx))
        else:
            return redirect(url_for('documentation.show_tasks'))

    return render_template('pages/inputs/add_task.html', **context)


@blue_print.route('/show_tasks')
def show_tasks():
    """View for showing new tasks"""

    task = Task(connection=connection, cursor=cursor)

    all_tasks = task.get_all_tasks()

    context = {
        'all_tasks': all_tasks
    }

    return render_template('pages/tables/tasks.html', **context)


@blue_print.route('/show_one_document/<int:idx>', methods=("GET", "POST"))
def show_one_document(idx: int):
    """View for one document page"""

    document = Document(connection=connection, cursor=cursor)
    document_description = document.get_document_by_id(document_id=idx)

    task = Task(connection=connection, cursor=cursor)
    all_document_tasks = task.get_task_by_document_id(document_id=idx)

    context = {
        'document_description': document_description,
        'all_document_tasks': all_document_tasks
    }

    return render_template('pages/settings/document.html', **context)


@blue_print.route('/show_one_factory/<int:idx>', methods=("GET", "POST"))
def show_one_factory(idx: int):
    """View for one factory page"""

    factory = Factory(connection=connection, cursor=cursor)
    factory_description = factory.get_factory_by_id(factory_id=idx)

    context = {
        'factory_description': factory_description,
    }

    return render_template('pages/settings/factory.html', **context)


@blue_print.route('/show_one_task/<int:idx>', methods=("GET", "POST"))
def show_one_task(idx: int):
    """View for one task page"""

    task = Task(connection=connection, cursor=cursor)
    task_description = task.get_task_by_id(task_id=idx)

    context = {
        'task_description': task_description,
    }

    return render_template('pages/settings/task.html', **context)


@blue_print.route('/show_one_user/<int:idx>', methods=("GET", "POST"))
def show_one_user(idx: int):
    """View for one user page"""

    user = User(connection=connection, cursor=cursor)
    user_description = user.get_user_by_id(user_id=idx)

    context = {
        'user_description': user_description,
    }

    return render_template('pages/settings/user.html', **context)


@blue_print.route('/update_table')
def update_table():
    """View for table updating (using JQuery and ajax)"""

    update_table_schema = UpdateTableSchema()

    errors = update_table_schema.validate(request.args)

    # if user inputs not number or nothing, than show him all entries
    if errors:
        last_n_days = 0
    else:
        args = update_table_schema.dump(request.args)
        last_n_days = args['last_n_days']

    document = Document(connection=connection, cursor=cursor)

    if last_n_days == 0:
        documents_by_date = document.get_all_documents()
    else:
        documents_by_date = document.get_document_by_date(document_n_days=last_n_days)

    context = {
        'all_documents': documents_by_date
    }

    return render_template('pages/tables/documents_table.html', **context)


@blue_print.route('/change_document/<int:document_idx>', methods=("GET", "POST"))
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
            abort(400, str(errors))

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

        return redirect(url_for('documentation.show_one_document', idx=document_to_change['id']))

    return render_template('pages/inputs/change_document.html', **context)

