"""Module with database connection objects"""

import os

try:
    # Used for server setup using command line
    from spa_oauth.backend.modules.database.database_interactions import connect_to_database, connect_to_database_by_url
except ModuleNotFoundError as err:
    # Used for server setup using Docker
    from modules.database.database_interactions import connect_to_database, connect_to_database_by_url

connection = None
cursor = None


if os.getenv('DATABASE_URL'):
    connection, cursor = connect_to_database_by_url(database_url=os.getenv('DATABASE_URL'))
    try:
        cursor.execute(open("schema.sql", "r").read())
        connection.commit()
    except Exception:
        connection.rollback()
else:
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
