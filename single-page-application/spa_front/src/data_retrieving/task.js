/**
 Module with interactions for document table threw backend API
 */

import $ from 'jquery';


class Task{
    __GET_TASKS_REL_PATH = 'tasks'
    __GET_ONE_TASK_REL_PATH = 'get_one_task'

    __ADD_TASK_REL_PATH = 'add_task'
    __CHANGE_TASK_REL_PATH = 'change_task'
    __DELETE_TASK_REL_PATH = 'delete_task'

    constructor(root_uri) {
        /**
         * Class for interactions with backend API
         */

        this.root_uri = root_uri;

        this.taskState = null;
    }

    get_all_tasks() {
        let get_all_tasks_url =  this.root_uri + this.__GET_TASKS_REL_PATH;

        let response = Task.makeGetRequest(get_all_tasks_url);


        let all_tasks = response['all_tasks']

        return all_tasks;
    }

    get_one_task(task_id) {
        let get_one_task_url =  this.root_uri + this.__GET_ONE_TASK_REL_PATH;

        get_one_task_url += '/' + task_id

        let response = Task.makeGetRequest(get_one_task_url);
        let task_description = response['task_description']

        return task_description;
    }

    add_task(
        task_name, executor_id,
        document_id, factory_id
    ) {
        let add_one_task_url =  this.root_uri + this.__ADD_TASK_REL_PATH;

        let params = {
            'task_name': task_name,
            'executor_id': executor_id,
            'document_id': document_id,
            'factory_id': factory_id,
        }

        Task.makePostRequest(add_one_task_url, params)
    }

    delete_task(task_id) {
        let delete_one_task_url =  this.root_uri + this.__DELETE_TASK_REL_PATH;

        delete_one_task_url += '/' + task_id

        let response = Task.makeGetRequest(delete_one_task_url);
    }

    change_task(
        task_id, task_name,
        executor_id, document_id,
        factory_id
    ) {
        let change_one_task_url =  this.root_uri + this.__CHANGE_TASK_REL_PATH;
        change_one_task_url += '/' + task_id

        let params = {
            'task_name': task_name,
            'executor_id': executor_id,
            'document_id': document_id,
            'factory_id': factory_id,
        }

        let response = Task.makePostRequest(change_one_task_url, params)
    }


    static makeGetRequest(url, data = null) {
        var real_response = null;

        var settings = {
            url: url,
            method: "GET",
            timeout: 0,
            dataType: 'json',
            processData: false,
            mimeType: "multipart/form-data",
            contentType: false,
            async: false,
            data: data,
            success: function (data) {
                real_response = data;
            },
            error: function (error) {
                console.log('Error', error);
            }
        };

        $.ajax(settings);

        return real_response;
    }

    static makePostRequest(url, data) {
        var real_response = null;

        console.log(data)

        var settings = {
            url: url,
            method: "POST",
            dataType: 'json',
            async: false,
            traditional: true,
            data: data,
            success: function (data) {
                real_response = data;
            },
            error: function (error) {
                console.log('Error', error);
            }
        };

        $.ajax(settings);

        return real_response;
    }


}

export default Task;