"""Module with functions for items removing"""

import os

from flask import (Blueprint,
                   render_template)

try:
    # Used for server setup using command line
    from frontend_backend_servers.frontend.modules.data_retrieving.document import Document
    from frontend_backend_servers.frontend.modules.data_retrieving.user import User
    from frontend_backend_servers.frontend.modules.data_retrieving.task import Task
    from frontend_backend_servers.frontend.modules.data_retrieving.factory import Factory

except ModuleNotFoundError as err:
    # Used for server setup using Docker
    from modules.data_retrieving.document import Document
    from modules.data_retrieving.user import User
    from modules.data_retrieving.task import Task
    from modules.data_retrieving.factory import Factory


delete_blue_print = Blueprint('delete_documentation', __name__)


@delete_blue_print.route('/delete_document/<int:document_idx>', methods=["GET"])
def delete_document(document_idx: int):
    """View for deleting document"""

    document = Document(root_uri=os.environ['ROOT_BACKEND_URI'])

    document.delete_document(document_id=document_idx)

    all_documents = document.get_all_documents()

    context = {
        'all_documents': all_documents
    }

    return render_template('pages/tables/documents.html', **context)


@delete_blue_print.route('/delete_factory/<int:factory_idx>', methods=["GET"])
def delete_factory(factory_idx: int):
    """View for deleting factory"""

    factory = Factory(root_uri=os.environ['ROOT_BACKEND_URI'])

    factory.delete_factory(factory_id=factory_idx)

    all_factories = factory.get_all_factories()

    context = {
        'all_factories': all_factories
    }

    return render_template('pages/tables/factories.html', **context)


@delete_blue_print.route('/delete_task/<int:task_idx>', methods=["GET"])
def delete_task(task_idx: int):
    """View for deleting factory"""

    task = Task(root_uri=os.environ['ROOT_BACKEND_URI'])

    task.delete_task(task_id=task_idx)

    all_tasks = task.get_all_tasks()

    context = {
        'all_tasks': all_tasks
    }

    return render_template('pages/tables/tasks.html', **context)


@delete_blue_print.route('/delete_user/<int:user_idx>', methods=["GET"])
def delete_user(user_idx: int):
    """View for deleting users"""

    user = User(root_uri=os.environ['ROOT_BACKEND_URI'])

    user.delete_user(user_id=user_idx)

    all_users = user.get_all_users()

    context = {
        'all_users': all_users
    }

    return render_template('pages/tables/users.html', **context)
