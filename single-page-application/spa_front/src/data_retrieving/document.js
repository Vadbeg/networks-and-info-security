/**
 Module with interactions for document table threw backend API
 */

import $ from 'jquery';


class Document{
    __GET_DOCUMENTS_REL_PATH = 'documents';
    __GET_ONE_DOCUMENT_REL_PATH = 'get_one_document';
    __GET_DOCUMENTS_BY_DATE_REL_PATH = 'get_documents_by_date';

    __ADD_DOCUMENT_REL_PATH = 'add_document';
    __CHANGE_DOCUMENT_REL_PATH = 'change_document';
    __DELETE_DOCUMENT_REL_PATH = 'delete_document';

    constructor(root_uri) {
        /**
         * Class for interactions with backend API
         */

        this.root_uri = root_uri;

        this.documentState = null;
    }

    get_all_documents() {
        let get_all_documents_url =  this.root_uri + this.__GET_DOCUMENTS_REL_PATH;

        console.log(get_all_documents_url);

        let response = Document.makeGetRequest(get_all_documents_url);
        console.log(response);

        let all_documents = response['all_documents']

        return all_documents;
    }

    get_one_document(document_id) {
        let get_one_document_url =  this.root_uri + this.__GET_ONE_DOCUMENT_REL_PATH;

        get_one_document_url += '/' + document_id

        let response = Document.makeGetRequest(get_one_document_url);

        let document_description = response['document_description']
        let all_document_tasks = response['all_document_tasks']

        return [document_description, all_document_tasks];
    }

    add_document(document_name, document_type, creators_ids,
                 controllers_ids, date_of_creation, date_of_registration) {
        let add_one_document_url =  this.root_uri + this.__ADD_DOCUMENT_REL_PATH;

        let params = {
            'document_name': document_name,
            'document_type': document_type,
            'creators_ids': creators_ids,
            'controllers_ids': controllers_ids,
            'date_of_creation': date_of_creation,
            'date_of_registration': date_of_registration
        }

        Document.makePostRequest(add_one_document_url, params)
    }

    delete_document(document_id) {
        let delete_one_document_url =  this.root_uri + this.__DELETE_DOCUMENT_REL_PATH;

        delete_one_document_url += '/' + document_id

        let response = Document.makeGetRequest(delete_one_document_url);
    }

    change_document(
        document_id, document_name, document_type, creators_ids,
        controllers_ids, date_of_creation, date_of_registration
    ) {
        let change_one_document_url =  this.root_uri + this.__CHANGE_DOCUMENT_REL_PATH;
        change_one_document_url += '/' + document_id

        let params = {
            'document_name': document_name,
            'document_type': document_type,
            'creators_ids': creators_ids,
            'controllers_ids': controllers_ids,
            'date_of_creation': date_of_creation,
            'date_of_registration': date_of_registration
        }

        let response = Document.makePostRequest(change_one_document_url, params)
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

export default Document;