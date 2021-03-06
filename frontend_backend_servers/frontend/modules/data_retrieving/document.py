"""Module with interactions for document table"""

import requests
import urllib.parse
from datetime import datetime
from typing import List, Dict


class Document:
    __GET_DOCUMENTS_REL_PATH = 'documents'
    __GET_ONE_DOCUMENT_REL_PATH = 'get_one_document'

    __ADD_DOCUMENT_REL_PATH = 'add_document'
    __CHANGE_DOCUMENT_REL_PATH = 'change_document'
    __DELETE_DOCUMENT_REL_PATH = 'delete_document'

    def __init__(self, root_uri: str):
        """
        Class for interactions with backend API

        :param root_uri: root ling for backend API
        """

        self.root_uri = root_uri

    def get_documents(self):
        """

        :return:
        """
        get_documents_url = urllib.parse.urljoin(self.root_uri, self.__GET_DOCUMENTS_REL_PATH)

        response = requests.get(get_documents_url)
        result = response.json()

        result = result['all_documents']

        return result

    def get_one_document(self, document_id: int):
        """

        :return:
        """

        get_one_document_url = urllib.parse.urljoin(self.root_uri, self.__GET_ONE_DOCUMENT_REL_PATH)
        get_one_document_url = get_one_document_url + '/'

        get_one_document_url = urllib.parse.urljoin(get_one_document_url, str(document_id))

        response = requests.get(get_one_document_url)
        result = response.json()

        return result

    def add_document(self, document_name: str, document_type: str,
                     creators_ids: List[int], controllers_ids: List[int],
                     date_of_creation: datetime, date_of_registration: datetime):
        """

        :param document_name:
        :param document_type:
        :param creators_ids:
        :param controllers_ids:
        :param date_of_creation:
        :param date_of_registration:
        :return:
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
                        date_of_creation: datetime, date_of_registration: datetime):

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

    def delete_document(self, document_id: int):
        """

        :return:
        """
        delete_one_document_url = urllib.parse.urljoin(self.root_uri, self.__DELETE_DOCUMENT_REL_PATH)
        delete_one_document_url = delete_one_document_url + '/'

        delete_one_document_url = urllib.parse.urljoin(delete_one_document_url, str(document_id))

        response = requests.get(delete_one_document_url)

        return response.status_code
