/**
 Module with interactions for document table threw backend API
 */

import $ from 'jquery';


class User{
    __GET_USERS_REL_PATH = 'users'
    __GET_ONE_USER_REL_PATH = 'get_one_user'

    __ADD_USER_REL_PATH = 'add_user'
    __CHANGE_USER_REL_PATH = 'change_user'
    __DELETE_USER_REL_PATH = 'delete_user'

    constructor(root_uri) {
        /**
         * Class for interactions with backend API
         */

        this.root_uri = root_uri;

        this.userState = null;
    }

    get_all_users() {
        let get_all_users_url =  this.root_uri + this.__GET_USERS_REL_PATH;

        let response = User.makeGetRequest(get_all_users_url);


        let all_users = response['all_users']

        return all_users;
    }

    get_one_user(user_id) {
        let get_one_user_url =  this.root_uri + this.__GET_ONE_USER_REL_PATH;

        get_one_user_url += '/' + user_id

        let response = User.makeGetRequest(get_one_user_url);

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

export default User;