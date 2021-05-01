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
        let user_description = response['user_description'];

        return user_description;
    }

    add_one_user(
        first_name, second_name,
        is_internal, position,
        email, phone_number) {

        let add_one_user_url =  this.root_uri + this.__ADD_USER_REL_PATH;

        let params = {
            'first_name': first_name,
            'second_name': second_name,
            'is_internal': is_internal,

            'position': position,
            'email': email,
            'phone_number': phone_number
        }

        console.log('Params', params)

        User.makePostRequest(add_one_user_url, params)

    }

    delete_user(user_id) {
        let delete_one_user_url =  this.root_uri + this.__DELETE_USER_REL_PATH;

        delete_one_user_url += '/' + user_id

        let response = User.makeGetRequest(delete_one_user_url);
    }

    change_user(
        user_id, first_name, second_name,
        is_internal, position,
        email, phone_number
    ) {
        let change_one_user_url =  this.root_uri + this.__CHANGE_USER_REL_PATH;
        change_one_user_url += '/' + user_id

        let params = {
            'first_name': first_name,
            'second_name': second_name,
            'is_internal': is_internal,

            'position': position,
            'email': email,
            'phone_number': phone_number
        }

        let response = User.makePostRequest(change_one_user_url, params)
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

export default User;