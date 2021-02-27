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
        :param curso`r: cursor for database
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
        factory = self.cursor.fetchall()[0]

        factory = dict(zip(self.COLUMNS_FACTORY, factory))

        return factory

    def change_factory(self, factory_id: int, factory_name: str, size: int, city: str):
        """
        For changing factory in database

        :param factory_id: index of factory to change
        :param factory_name: factory name
        :param size: factory size
        :param city: factory city
        """

        change_document_query = """
UPDATE factory
SET factory_name = %s, size = %s,
    city=%s
WHERE factory.id = %s;
        """

        val = [factory_name, size, city, factory_id]

        self.cursor.execute(change_document_query, val)
        self.connection.commit()

    def delete_factory(self, factory_id: int):
        """
        Deletes factory by id from database

        :param factory_id: id of the factory
        """

        delete_factory_query = """
DELETE FROM factory
WHERE factory.id = %s;
                """

        val = [factory_id]

        self.cursor.execute(delete_factory_query, val)
        self.connection.commit()
