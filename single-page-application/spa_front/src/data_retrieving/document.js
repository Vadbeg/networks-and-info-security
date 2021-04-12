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

        let response = Document.makeGetRequest(get_all_documents_url);

        let all_documents = response['all_documents']
        let creators = response['creators']

        console.log('all_documents')
        console.log(all_documents)

        return [all_documents, creators];
    }

    get_one_document(document_id) {
        let get_one_document_url =  this.root_uri + this.__GET_ONE_DOCUMENT_REL_PATH;

        get_one_document_url += '/' + document_id

        let response = Document.makeGetRequest(get_one_document_url);

        return response;
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


}

export default Document;