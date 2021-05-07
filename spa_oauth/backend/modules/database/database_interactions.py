"""Module with database interactions"""

import urllib.parse
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


def connect_to_database_by_url(database_url) -> Tuple:
    """
    Waits until database is initiated. Connects to it by url
    """

    while True:
        try:
            connection = psycopg2.connect(database_url, sslmode='require')

            cursor = connection.cursor()
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

    psycopg2.connect('')

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

