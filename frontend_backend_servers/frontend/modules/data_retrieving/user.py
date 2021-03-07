"""Module with interactions for user table threw backend API"""

import requests
import urllib.parse
from typing import Union, List, Dict


class User:
    __GET_USERS_REL_PATH = 'users'
    __GET_ONE_USER_REL_PATH = 'get_one_user'

    __ADD_USER_REL_PATH = 'add_user'
    __CHANGE_USER_REL_PATH = 'change_user'
    __DELETE_USER_REL_PATH = 'delete_user'

    def __init__(self, root_uri: str):
        """
        Class for interactions with backend API

        :param root_uri: root ling for backend API
        """

        self.root_uri = root_uri

    def get_all_users(self) -> List[Dict]:
        """
        Gets all users from database threw backend API

        :return: list of users info
        """

        get_users_url = urllib.parse.urljoin(self.root_uri, self.__GET_USERS_REL_PATH)

        response = requests.get(get_users_url)
        result = response.json()

        result = result['all_users']

        return result

    def get_one_user(self, user_id: int) -> Dict:
        """
        Gets one user from database threw backend API

        :param user_id: index of user
        :return: user description
        """

        get_one_user_url = urllib.parse.urljoin(self.root_uri, self.__GET_ONE_USER_REL_PATH)
        get_one_user_url = get_one_user_url + '/'

        get_one_user_url = urllib.parse.urljoin(get_one_user_url, str(user_id))

        response = requests.get(get_one_user_url)
        result = response.json()

        user_description = result['user_description']

        return user_description

    def add_user(self, first_name: str, second_name: str,
                 is_internal: bool, position: int,
                 email: str, phone_number: str) -> int:
        """
        Adds user to database threw backend API

        :param first_name: name of new user
        :param second_name: second name of new user
        :param is_internal: is user is internal True, else False
        :param position: position of user
        :param email: email of user
        :param phone_number: phone number of user
        :return: status code
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

    def change_user(self, user_id: int, first_name: str, second_name: str,
                    is_internal: bool, position: int,
                    email: str, phone_number: str) -> int:
        """
        Changes user in database threw backend API

        :param user_id: index of user
        :param first_name: name of new user
        :param second_name: second name of new user
        :param is_internal: is user is internal True, else False
        :param position: position of user
        :param email: email of user
        :param phone_number: phone number of user
        :return: status code
        """

        change_one_user_url = urllib.parse.urljoin(self.root_uri, self.__CHANGE_USER_REL_PATH)
        change_one_user_url = change_one_user_url + '/'

        change_one_user_url = urllib.parse.urljoin(change_one_user_url, str(user_id))

        params = {
            'first_name': first_name,
            'second_name': second_name,
            'is_internal': is_internal,

            'position': position,
            'email': email,
            'phone_number': phone_number
        }

        response = requests.post(change_one_user_url, params=params)

        return response.status_code

    def delete_user(self, user_id: int) -> int:
        """
        Deletes user from database threw backend API

        :param user_id: index of user to delete
        :return: status code
        """

        delete_one_user_url = urllib.parse.urljoin(self.root_uri, self.__DELETE_USER_REL_PATH)
        delete_one_user_url = delete_one_user_url + '/'

        delete_one_user_url = urllib.parse.urljoin(delete_one_user_url, str(user_id))

        response = requests.get(delete_one_user_url)

        return response.status_code



