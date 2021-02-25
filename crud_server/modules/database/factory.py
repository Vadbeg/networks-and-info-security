"""Module with interactions for factory table"""

from typing import List, Dict


class Factory:
    COLUMNS_FACTORY = [
        'id', 'factory_name',
        'size', 'city'
    ]

    def __init__(self, connection, cursor):
        """
        Class for faster interactions with factory table

        :param connection: connection to database
        :param cursor: cursor for database
        """

        self.connection = connection
        self.cursor = cursor

    def add_factory(self, factory_name: str, size: int, city: str):
        """
        For adding new document to database

        :param factory_name: name of the document type
        :param size: name of the document type
        :param city: date of document creation
        """

        add_factory_query = """
INSERT INTO factory (factory_name, size, city)
VALUES (%s, %s, %s)
RETURNING id
        """

        val = [factory_name, size, city]

        self.cursor.execute(add_factory_query, val)
        self.connection.commit()

    def get_all_factories(self) -> List[Dict]:
        """
        Returns all factories from database with controllers and creators

        :return: list of documents (with controllers and creators)
        """

        get_all_documents_query = """
SELECT *
FROM factory
        """

        self.cursor.execute(get_all_documents_query)
        all_documents = self.cursor.fetchall()

        all_documents = [dict(zip(self.COLUMNS_FACTORY, curr_user)) for curr_user in all_documents]

        return all_documents

    def get_factory_by_id(self, factory_id: int) -> Dict:
        """
        Finds factory in database by its id and returns it.

        :param factory_id: id of the factory
        :return: factory with give id
        """

        get_factory_query = """
SELECT *
FROM factory
WHERE factory.id = %s
        """

        val = [factory_id]

        self.cursor.execute(get_factory_query, val)
        document = self.cursor.fetchall()[0]

        document = dict(zip(self.COLUMNS_FACTORY, document))

        return document
