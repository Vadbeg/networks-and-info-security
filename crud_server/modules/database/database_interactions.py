"""Module with database interactions"""

import time
from typing import Tuple

import psycopg2


def connect_to_database(host: str = 'localhost', port: str = '3306',
                        user: str = 'root', password: str = 'root',
                        database: str = 'documents') -> Tuple:
    """
    Waits until database is initiated
    """

    while True:
        try:
            print(host)
            print(port)
            print(user)
            print(password)
            print(database)

            connection, cursor = create_connection(host=host,
                                                   port=port,
                                                   user=user,
                                                   password=password,
                                                   database=database)
        except psycopg2.OperationalError as err:
            print(f'Waiting for database...')
            print(err)
            # time.sleep(0.)
        else:
            break

    return connection, cursor


def create_connection(host: str = 'localhost', port: str = '3306',
                      user: str = 'root', password: str = 'root',
                      database: str = 'documents') -> Tuple:
    """
    Creates connection to PostgreSQL database
    It returns connection and cursor, because of weak connection problem.

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

