"""Module with interactions for factory table threw backend API"""

import requests
import urllib.parse
from typing import List, Dict


class Factory:
    __GET_FACTORIES_REL_PATH = 'factories'
    __GET_ONE_FACTORY_REL_PATH = 'get_one_factory'

    __ADD_FACTORY_REL_PATH = 'add_factory'
    __CHANGE_FACTORY_REL_PATH = 'change_factory'
    __DELETE_FACTORY_REL_PATH = 'delete_factory'

    def __init__(self, root_uri: str):
        """
        Class for interactions with backend API

        :param root_uri: root ling for backend API
        """

        self.root_uri = root_uri

    def get_all_factories(self) -> List[Dict]:
        """
        Gets all factories threw backend API

        :return:
        """

        get_factories_url = urllib.parse.urljoin(self.root_uri, self.__GET_FACTORIES_REL_PATH)

        response = requests.get(get_factories_url)
        result = response.json()

        result = result['all_factories']

        return result

    def get_one_factory(self, factory_id: int) -> Dict:
        """
        Gets one factory info threw backend API

        :param factory_id: index of factory
        :return:
        """

        get_one_factory_url = urllib.parse.urljoin(self.root_uri, self.__GET_ONE_FACTORY_REL_PATH)
        get_one_factory_url = get_one_factory_url + '/'

        get_one_factory_url = urllib.parse.urljoin(get_one_factory_url, str(factory_id))

        response = requests.get(get_one_factory_url)
        result = response.json()

        factory_description = result['factory_description']

        return factory_description

    def add_factory(self, factory_name: str, size: int,
                    city: str) -> int:
        """
        Adds factory to database threw backend API

        :param factory_name: name of factory
        :param size: size of factory
        :param city: city where factory is located
        :return: status code
        """

        add_document_url = urllib.parse.urljoin(self.root_uri, self.__ADD_FACTORY_REL_PATH)

        params = {
            'factory_name': factory_name,
            'size': size,
            'city': city,
        }

        response = requests.post(add_document_url, params=params)

        return response.status_code

    def change_factory(self, factory_id: int, factory_name: str,
                       size: int, city: str) -> int:
        """
        Changes factory in database threw backend API

        :param factory_id: factory index to change
        :param factory_name: name of factory
        :param size: size of factory
        :param city: city where factory is located
        :return: status code
        """

        change_one_factory_url = urllib.parse.urljoin(self.root_uri, self.__CHANGE_FACTORY_REL_PATH)
        change_one_factory_url = change_one_factory_url + '/'

        change_one_factory_url = urllib.parse.urljoin(change_one_factory_url, str(factory_id))

        params = {
            'factory_name': factory_name,
            'size': size,
            'city': city,
        }

        response = requests.post(change_one_factory_url, params=params)

        return response.status_code

    def delete_factory(self, factory_id: int) -> int:
        """
        Deletes factory in database threw backend API

        :param factory_id: index of factory to delete
        :return: status code
        """

        delete_one_factory_url = urllib.parse.urljoin(self.root_uri, self.__DELETE_FACTORY_REL_PATH)
        delete_one_factory_url = delete_one_factory_url + '/'

        delete_one_factory_url = urllib.parse.urljoin(delete_one_factory_url, str(factory_id))

        response = requests.get(delete_one_factory_url)

        return response.status_code
