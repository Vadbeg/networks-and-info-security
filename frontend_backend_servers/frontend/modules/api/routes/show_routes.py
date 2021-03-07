"""Module with routes for Flask application"""

import os

from flask import (Blueprint,
                   render_template,
                   request)

try:
    # Used for server setup using command line
    from frontend_backend_servers.frontend.modules.data_retrieving.document import Document
    from frontend_backend_servers.frontend.modules.data_retrieving.user import User
    from frontend_backend_servers.frontend.modules.data_retrieving.task import Task
    from frontend_backend_servers.frontend.modules.data_retrieving.factory import Factory

    from frontend_backend_servers.frontend.modules.api.schemas import UpdateTableSchema

except ModuleNotFoundError as err:
    # Used for server setup using Docker
    from modules.data_retrieving.document import Document
    from modules.data_retrieving.user import User
    from modules.data_retrieving.task import Task
    from modules.data_retrieving.factory import Factory

    from modules.api.schemas import UpdateTableSchema

show_blue_print = Blueprint('show_documentation', __name__)


@show_blue_print.route('/')
@show_blue_print.route('/home')
def home():
    """Home tab"""

    return render_template('pages/home.html')


@show_blue_print.route('/users')
def show_users():
    """View with users table"""

    user = User(root_uri=os.environ['ROOT_BACKEND_URI'])

    all_users = user.get_all_users()

    context = {
        'all_users': all_users
    }

    return render_template('pages/tables/users.html', **context)


@show_blue_print.route('/documents')
def show_documents():
    """View with documents table"""

    document = Document(root_uri=os.environ['ROOT_BACKEND_URI'])

    all_documents = document.get_all_documents()

    context = {
        'all_documents': all_documents
    }

    return render_template('pages/tables/documents.html', **context)


@show_blue_print.route('/factories')
def show_factories():
    """View with factories table"""

    factory = Factory(root_uri=os.environ['ROOT_BACKEND_URI'])

    all_factories = factory.get_all_factories()

    context = {
        'all_factories': all_factories
    }

    return render_template('pages/tables/factories.html', **context)


@show_blue_print.route('/show_tasks')
def show_tasks():
    """View for showing new tasks"""

    task = Task(root_uri=os.environ['ROOT_BACKEND_URI'])

    all_tasks = task.get_all_tasks()

    context = {
        'all_tasks': all_tasks
    }

    return render_template('pages/tables/tasks.html', **context)


@show_blue_print.route('/show_one_document/<int:idx>', methods=("GET", "POST"))
def show_one_document(idx: int):
    """View for one document page"""

    document = Document(root_uri=os.environ['ROOT_BACKEND_URI'])
    document_description, all_document_tasks = document.get_one_document(document_id=idx)

    context = {
        'document_description': document_description,
        'all_document_tasks': all_document_tasks
    }

    return render_template('pages/settings/document.html', **context)


@show_blue_print.route('/show_one_factory/<int:idx>', methods=("GET", "POST"))
def show_one_factory(idx: int):
    """View for one factory page"""

    factory = Factory(root_uri=os.environ['ROOT_BACKEND_URI'])
    factory_description = factory.get_one_factory(factory_id=idx)

    context = {
        'factory_description': factory_description,
    }

    return render_template('pages/settings/factory.html', **context)


@show_blue_print.route('/show_one_task/<int:idx>', methods=("GET", "POST"))
def show_one_task(idx: int):
    """View for one task page"""

    task = Task(root_uri=os.environ['ROOT_BACKEND_URI'])
    task_description = task.get_one_task(task_id=idx)

    context = {
        'task_description': task_description,
    }

    return render_template('pages/settings/task.html', **context)


@show_blue_print.route('/show_one_user/<int:idx>', methods=("GET", "POST"))
def show_one_user(idx: int):
    """View for one user page"""

    user = User(root_uri=os.environ['ROOT_BACKEND_URI'])
    user_description = user.get_one_user(user_id=idx)

    context = {
        'user_description': user_description,
    }

    return render_template('pages/settings/user.html', **context)


@show_blue_print.route('/update_table')
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

    document = Document(root_uri=os.environ['ROOT_BACKEND_URI'])

    documents_by_date = document.get_documents_by_date(document_n_days=last_n_days)

    context = {
        'all_documents': documents_by_date
    }

    return render_template('pages/tables/documents_table.html', **context)

