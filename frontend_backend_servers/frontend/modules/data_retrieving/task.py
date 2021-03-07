"""Module with interactions for task table"""

import requests
import urllib.parse
from typing import List, Dict


class Task:
    __GET_TASKS_REL_PATH = 'tasks'
    __GET_ONE_TASK_REL_PATH = 'get_one_task'

    __ADD_TASK_REL_PATH = 'add_task'
    __CHANGE_TASK_REL_PATH = 'change_task'
    __DELETE_TASK_REL_PATH = 'delete_task'

    def __init__(self, root_uri: str):
        """
        Class for interactions with backend API

        :param root_uri: root ling for backend API
        """

        self.root_uri = root_uri

    def get_all_tasks(self) -> List[Dict]:
        """
        Gets all tasks from database threw backend API

        :return: list of tasks info
        """

        get_tasks_url = urllib.parse.urljoin(self.root_uri, self.__GET_TASKS_REL_PATH)

        response = requests.get(get_tasks_url)
        result = response.json()

        all_tasks = result['all_tasks']

        return all_tasks

    def get_one_task(self, task_id: int) -> Dict:
        """
        Gets one task from database threw backend API

        :param task_id: task index
        :return: task info
        """

        get_one_task_url = urllib.parse.urljoin(self.root_uri, self.__GET_ONE_TASK_REL_PATH)
        get_one_task_url = get_one_task_url + '/'

        get_one_task_url = urllib.parse.urljoin(get_one_task_url, str(task_id))

        response = requests.get(get_one_task_url)

        result = response.json()
        task_description = result['task_description']

        return task_description

    def add_task(self, task_name: str, executor_id: str,
                 document_id: int, factory_id: int) -> int:
        """
        Adds task to database threw backend API

        :param task_name: name of new task
        :param executor_id: index of the executor
        :param document_id: index of document
        :param factory_id: index of factory
        :return: status code
        """

        add_task_url = urllib.parse.urljoin(self.root_uri, self.__ADD_TASK_REL_PATH)

        params = {
            'task_name': task_name,
            'executor_id': executor_id,
            'document_id': document_id,
            'factory_id': factory_id,
        }

        response = requests.post(add_task_url, params=params)

        return response.status_code

    def change_task(self, task_id: int, task_name: str, executor_id: str,
                    document_id: int, factory_id: int) -> int:
        """
        Changes task in database threw backend API

        :param task_id: index of task to change
        :param task_name: name of task
        :param executor_id: index of executor
        :param document_id: index of document
        :param factory_id: index of factory
        :return: status code
        """

        change_one_task_url = urllib.parse.urljoin(self.root_uri, self.__CHANGE_TASK_REL_PATH)
        change_one_task_url = change_one_task_url + '/'

        change_one_task_url = urllib.parse.urljoin(change_one_task_url, str(task_id))

        params = {
            'task_name': task_name,
            'executor_id': executor_id,
            'document_id': document_id,
            'factory_id': factory_id,
        }

        response = requests.post(change_one_task_url, params=params)

        return response.status_code

    def delete_task(self, task_id: int) -> int:
        """
        Deletes task from database threw backend API

        :param task_id: index of task to delete
        :return: status code
        """

        delete_one_task_url = urllib.parse.urljoin(self.root_uri, self.__DELETE_TASK_REL_PATH)
        delete_one_task_url = delete_one_task_url + '/'

        delete_one_task_url = urllib.parse.urljoin(delete_one_task_url, str(task_id))

        response = requests.get(delete_one_task_url)

        return response.status_code
