"""Module with interactions for document table threw backend API"""

import requests
import urllib.parse
from datetime import datetime
from typing import List, Dict, Tuple


class Document:
    __GET_DOCUMENTS_REL_PATH = 'documents'
    __GET_ONE_DOCUMENT_REL_PATH = 'get_one_document'
    __GET_DOCUMENTS_BY_DATE_REL_PATH = 'get_documents_by_date'

    __ADD_DOCUMENT_REL_PATH = 'add_document'
    __CHANGE_DOCUMENT_REL_PATH = 'change_document'
    __DELETE_DOCUMENT_REL_PATH = 'delete_document'

    def __init__(self, root_uri: str):
        """
        Class for interactions with backend API

        :param root_uri: root ling for backend API
        """

        self.root_uri = root_uri

    def get_all_documents(self) -> List[Dict]:
        """
        Gets all documents info from backend server

        :return:
        """

        get_documents_url = urllib.parse.urljoin(self.root_uri, self.__GET_DOCUMENTS_REL_PATH)

        response = requests.get(get_documents_url)
        result = response.json()

        all_documents = result['all_documents']

        return all_documents

    def get_one_document(self, document_id: int) -> Tuple[List[Dict], Dict]:
        """
        Gets info for on document and all task for it from backend server

        :param document_id: document index
        :return: list of tasks for one document, document info
        """

        get_one_document_url = urllib.parse.urljoin(self.root_uri, self.__GET_ONE_DOCUMENT_REL_PATH)
        get_one_document_url = get_one_document_url + '/'

        get_one_document_url = urllib.parse.urljoin(get_one_document_url, str(document_id))

        response = requests.get(get_one_document_url)
        result = response.json()

        document_description = result['document_description']
        all_document_tasks = result['all_document_tasks']

        return document_description, all_document_tasks

    def get_documents_by_date(self, document_n_days):
        get_documents_by_date_url = urllib.parse.urljoin(self.root_uri, self.__GET_DOCUMENTS_BY_DATE_REL_PATH)

        params = {
            'last_n_days': document_n_days
        }

        response = requests.get(get_documents_by_date_url, params=params)
        result = response.json()

        all_documents = result['all_documents']

        return all_documents

    def add_document(self, document_name: str, document_type: str,
                     creators_ids: List[int], controllers_ids: List[int],
                     date_of_creation: datetime, date_of_registration: datetime) -> int:
        """
        Adds document to database threw backend

        :param document_name: name of document
        :param document_type: type of document
        :param creators_ids: list of creators indexes
        :param controllers_ids: list of controllers indexes
        :param date_of_creation: date of document creation
        :param date_of_registration: date of document registration
        :return: status code
        """

        add_document_url = urllib.parse.urljoin(self.root_uri, self.__ADD_DOCUMENT_REL_PATH)

        params = {
            'document_name': document_name,
            'document_type': document_type,
            'creators_ids': creators_ids,
            'controllers_ids': controllers_ids,
            'date_of_creation': date_of_creation,
            'date_of_registration': date_of_registration
        }

        response = requests.post(add_document_url, params=params)

        return response.status_code

    def change_document(self, document_id: int, document_name: str, document_type: str,
                        creators_ids: List[int], controllers_ids: List[int],
                        date_of_creation: datetime, date_of_registration: datetime) -> int:
        """
        Changes document in database threw backend

        :param document_id: index of document to change
        :param document_name: name of document
        :param document_type: type of document
        :param creators_ids: list of creators indexes
        :param controllers_ids: list of controllers indexes
        :param date_of_creation: date of document creation
        :param date_of_registration: date of document registration
        :return: status code
        """

        change_one_document_url = urllib.parse.urljoin(self.root_uri, self.__CHANGE_DOCUMENT_REL_PATH)
        change_one_document_url = change_one_document_url + '/'

        change_one_document_url = urllib.parse.urljoin(change_one_document_url, str(document_id))

        params = {
            'document_name': document_name,
            'document_type': document_type,
            'creators_ids': creators_ids,
            'controllers_ids': controllers_ids,
            'date_of_creation': date_of_creation,
            'date_of_registration': date_of_registration
        }

        response = requests.post(change_one_document_url, params=params)

        return response.status_code

    def delete_document(self, document_id: int) -> int:
        """
        Deletes document in database threw backend

        :param document_id: index of document to delete
        :return: status code
        """

        delete_one_document_url = urllib.parse.urljoin(self.root_uri, self.__DELETE_DOCUMENT_REL_PATH)
        delete_one_document_url = delete_one_document_url + '/'

        delete_one_document_url = urllib.parse.urljoin(delete_one_document_url, str(document_id))

        response = requests.get(delete_one_document_url)

        return response.status_code
