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


all_blue_print = Blueprint('documentation', __name__)


@all_blue_print.route('/change_document/<int:document_idx>', methods=("GET", "POST"))
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

        return redirect(url_for('show_documentation.show_one_document', idx=document_to_change['id']))

    return render_template('pages/changes/change_document.html', **context)

