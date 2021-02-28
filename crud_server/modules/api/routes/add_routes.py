"""Module with routes for Flask application"""

from datetime import datetime

from flask import (Blueprint,
                   render_template,
                   request, abort,
                   redirect, url_for)

try:
    # Used for server setup using command line
    from crud_server.modules.api.database_connection import connection, cursor
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
    from modules.api.database_connection import connection, cursor
    from modules.database.database_interactions import close_connection, connect_to_database
    from modules.database.document import Document
    from modules.database.user import User
    from modules.database.task import Task
    from modules.database.factory import Factory

    from modules.api.schemas import (AddNewUser, AddNewDocument,
                                     AddNewTask, UpdateTableSchema,
                                     AddNewFactory)


add_blue_print = Blueprint('add_documentation', __name__)


@add_blue_print.route('/add_user', methods=("GET", "POST"))
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

        return redirect(url_for('show_documentation.show_users'))

    return render_template('pages/inputs/add_user.html')


@add_blue_print.route('/add_document', methods=("GET", "POST"))
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

        return redirect(url_for('show_documentation.show_documents'))

    return render_template('pages/inputs/add_document.html', **context)


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

        return redirect(url_for('show_documentation.show_factories'))

    return render_template('pages/inputs/add_factory.html')


@add_blue_print.route('/add_task', defaults={'document_idx': None}, methods=("GET", "POST"))
@add_blue_print.route('/add_task/<int:document_idx>', methods=("GET", "POST"))
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
            return redirect(url_for('show_documentation.show_one_document', idx=document_idx))
        else:
            return redirect(url_for('show_documentation.show_tasks'))

    return render_template('pages/inputs/add_task.html', **context)
