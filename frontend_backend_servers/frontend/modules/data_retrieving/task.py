"""Module with interactions for task table"""

import requests
import urllib.parse
from datetime import datetime
from typing import List, Dict


class Task:
    __GET_TASKS_REL_PATH = 'tasks'
    __GET_ONE_TASK_REL_PATH = 'get_one_factory'

    __ADD_TASK_REL_PATH = 'add_task'

    def __init__(self, root_uri: str):
        """
        Class for interactions with backend API

        :param root_uri: root ling for backend API
        """

        self.root_uri = root_uri

    def get_tasks(self):
        """

        :return:
        """
        get_documents_url = urllib.parse.urljoin(self.root_uri, self.__GET_TASKS_REL_PATH)

        response = requests.get(get_documents_url)
        result = response.json()

        result = result['all_tasks']

        return result

    def get_one_task(self, task_id: int):
        """

        :return:
        """
        get_one_document_url = urllib.parse.urljoin(self.root_uri, self.__GET_ONE_TASK_REL_PATH)

        params = {'idx': task_id}

        response = requests.get(get_one_document_url, params=params)
        result = response.json()

        return result

    def add_task(self, task_name: str, executor_id: str,
                 document_id: int, factory_id: int):
        """

        :param task_name:
        :param executor_id:
        :param document_id:
        :param factory_id:
        :return:
        """

        add_document_url = urllib.parse.urljoin(self.root_uri, self.__ADD_TASK_REL_PATH)

        params = {
            'task_name': task_name,
            'executor_id': executor_id,
            'document_id': document_id,
            'factory_id': factory_id,
        }

        response = requests.post(add_document_url, params=params)

        return response.status_code

