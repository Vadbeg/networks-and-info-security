"""Module with interactions for user table"""

import requests
import urllib.parse
from typing import Union, List, Dict


class User:
    __GET_USERS_REL_PATH = 'users'
    __GET_ONE_USER_REL_PATH = 'get_one_user'

    __ADD_USER_REL_PATH = 'add_user'

    def __init__(self, root_uri: str):
        """
        Class for interactions with backend API

        :param root_uri: root ling for backend API
        """

        self.root_uri = root_uri

    def get_users(self):
        """

        :return:
        """
        get_users_url = urllib.parse.urljoin(self.root_uri, self.__GET_USERS_REL_PATH)

        response = requests.get(get_users_url)
        result = response.json()

        result = result['all_users']

        return result

    def get_one_user(self, user_id: int):
        """

        :return:
        """
        get_one_user_url = urllib.parse.urljoin(self.root_uri, self.__GET_ONE_USER_REL_PATH)

        params = {'idx': user_id}

        response = requests.get(get_one_user_url, params=params)
        result = response.json()

        return result

    def add_user(self, first_name: str, second_name: str,
                 is_internal: bool, position: int,
                 email: str, phone_number: str):
        """

        :param first_name:
        :param second_name:
        :param is_internal:
        :param position:
        :param email:
        :param phone_number:
        :return:
        """

        add_user_url = urllib.parse.urljoin(self.root_uri, self.__ADD_USER_REL_PATH)

        params = {
            'first_name': first_name,
            'second_name': second_name,
            'is_internal': is_internal,

            'position': position,
            'email': email,
            'phone_number': phone_number
        }

        response = requests.post(add_user_url, params=params)

        return response.status_code



