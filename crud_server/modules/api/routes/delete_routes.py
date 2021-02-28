"""Module with functions for items removing"""


from flask import (Blueprint,
                   render_template)

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


delete_blue_print = Blueprint('delete_documentation', __name__)


@delete_blue_print.route('/delete_document/<int:document_idx>', methods=["GET"])
def delete_document(document_idx: int):
    """View for deleting document"""

    document = Document(connection=connection, cursor=cursor)

    document.delete_document(document_id=document_idx)

    all_documents = document.get_all_documents()

    context = {
        'all_documents': all_documents
    }

    return render_template('pages/tables/documents.html', **context)


@delete_blue_print.route('/delete_factory/<int:factory_idx>', methods=["GET"])
def delete_factory(factory_idx: int):
    """View for deleting factory"""

    factory = Factory(connection=connection, cursor=cursor)

    factory.delete_factory(factory_id=factory_idx)

    all_factories = factory.get_all_factories()

    context = {
        'all_factories': all_factories
    }

    return render_template('pages/tables/factories.html', **context)


@delete_blue_print.route('/delete_task/<int:task_idx>', methods=["GET"])
def delete_task(task_idx: int):
    """View for deleting factory"""

    task = Task(connection=connection, cursor=cursor)

    task.delete_task(task_id=task_idx)

    all_tasks = task.get_all_tasks()

    context = {
        'all_tasks': all_tasks
    }

    return render_template('pages/tables/tasks.html', **context)


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

    return render_template('pages/tables/users.html', **context)
