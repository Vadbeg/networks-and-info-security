"""Module with database interactions"""

from typing import Tuple

import psycopg2


def create_connection(host: str = 'localhost', port: str = '3306',
                      user: str = 'root', password: str = 'root',
                      database: str = 'documents') -> Tuple:
    """
    Creates connection to PostgreSQL database
    It returns connection and cursor, because of weak connection problem.

    :url: https://stackoverflow.com/questions/1482141/what-does-it-mean-weakly-referenced-object-no-longer-exists
    :return: connection and cursor for PostgreSQL databse
    """

    connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        dbname=database
    )

    cursor = connection.cursor()

    return connection, cursor


def close_connection(connection, cursor):
    """
    Closes cursor and connection

    :param connection: connection to mysql database
    :param cursor: cursor for given connection
    """

    connection.close()
    cursor.close()

