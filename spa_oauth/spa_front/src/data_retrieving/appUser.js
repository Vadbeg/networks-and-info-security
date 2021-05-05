/**
 Module with interactions for document table threw backend API
 */

import $ from 'jquery';
import App from "../App";


class AppUser{
    __REGISTER_USER = 'auth/register'
    __LOGIN_USER = 'auth/login'

    constructor(root_uri) {
        /**
         * Class for interactions with backend API
         */

        this.root_uri = root_uri;
    }

    register_user(
        email, password
    ) {
        let params = {
            'email': email,
            'password': password,
        }

        let register_user_url =  this.root_uri + this.__REGISTER_USER;

        let response = AppUser.makePostRequest(register_user_url, params);

        if (response['status'] === 403) {
            response = 403;
        }

        return response;
    }

    login_user(
        email, password
    ) {
        let params = {
            'email': email,
            'password': password,
        }

        let register_user_url =  this.root_uri + this.__LOGIN_USER;

        let response = AppUser.makePostRequest(register_user_url, params);

        if (response['status'] === 403) {
            response = 403;
        } else if (response['status'] === 404) {
            response = 404
        }

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


    static makePostRequest(url, data) {
        var real_response = null;

        console.log(url, data)

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
                real_response = error;
            }
        };

        $.ajax(settings);

        return real_response;
    }


}

export default AppUser;