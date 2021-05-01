/**
 Module with interactions for document table threw backend API
 */

import $ from 'jquery';


class Factory{
    __GET_FACTORIES_REL_PATH = 'factories'
    __GET_ONE_FACTORY_REL_PATH = 'get_one_factory'

    __ADD_FACTORY_REL_PATH = 'add_factory'
    __CHANGE_FACTORY_REL_PATH = 'change_factory'
    __DELETE_FACTORY_REL_PATH = 'delete_factory'

    constructor(root_uri) {
        /**
         * Class for interactions with backend API
         */

        this.root_uri = root_uri;

        this.factoryState = null;
    }

    get_all_factories() {
        let get_all_documents_url =  this.root_uri + this.__GET_FACTORIES_REL_PATH;

        let response = Factory.makeGetRequest(get_all_documents_url);

        let all_documents = response['all_factories']

        return all_documents;
    }

    get_one_factory(factory_id) {
        let get_one_factory_url =  this.root_uri + this.__GET_ONE_FACTORY_REL_PATH;

        get_one_factory_url += '/' + factory_id

        let response = Factory.makeGetRequest(get_one_factory_url);
        let factory_description = response['factory_description'];

        return factory_description;
    }

    add_factory(
        factory_name, size, city,
    ) {
        let add_one_factory_url =  this.root_uri + this.__ADD_FACTORY_REL_PATH;

        let params = {
            'factory_name': factory_name,
            'size': size,
            'city': city,
        }

        Factory.makePostRequest(add_one_factory_url, params)
    }

    delete_factory(factory_id) {
        let delete_one_factory_url =  this.root_uri + this.__DELETE_FACTORY_REL_PATH;

        delete_one_factory_url += '/' + factory_id

        let response = Factory.makeGetRequest(delete_one_factory_url);
    }

    change_factory(
        factory_id, factory_name,
        size, city
    ) {
        let change_one_factory_url =  this.root_uri + this.__CHANGE_FACTORY_REL_PATH;
        change_one_factory_url += '/' + factory_id

        let params = {
            'factory_name': factory_name,
            'size': size,
            'city': city,
        }

        let response = Factory.makePostRequest(change_one_factory_url, params)
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

export default Factory;