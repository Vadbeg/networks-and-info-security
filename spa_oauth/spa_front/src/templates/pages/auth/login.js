import React from "react";
import {Link} from "react-router-dom";

import AppUser from "../../../data_retrieving/appUser";

import GoogleLogin from "react-google-login";
// import GitHubLogin from "react-github-login/src";


export default class Login extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'email': null,
            'password': null,
        }

        this.appUser = new AppUser(process.env.REACT_APP_ROOT_BACKEND_URI);
    }

    componentDidMount() {

    }

    inputChangeHandler = (event) => {
        let name = event.target.name;
        let value = event.target.value;

        this.setState({[name]: value})
    }

    loginUser = (event) => {
        event.preventDefault();

        const {
            email,
            password,
        } = this.state;
        const { setToken } = this.props

        let response = this.appUser.login_user(
            email,
            password
        )

        if (response === 403) {
            alert('Incorrect password')
        } else if (response === 404) {
            alert('No user with give email')
        } else if (response !== null) {
            let { auth_token } = response;

            setToken(auth_token);
        }

    }

    responseGoogle = (event) => {
        console.log(event);

        const {
            tokenObj,
            profileObj,
        } = event;

        console.log(event);

        const { email } = profileObj;
        const { login_hint } = tokenObj;

        const { setToken } = this.props

        let response = this.appUser.login_user_google(
            email,
            login_hint
        )

        if (response === 403) {
            alert('Incorrect password')
        } else if (response === 404) {
            alert('No user with give email')
        } else if (response !== null) {
            let { auth_token } = response;

            setToken(auth_token);
        }
    }

    responseGithub = (response) => {
        console.log(response);
    }

    render() {

        let loginUserForm = (
            <div>

                <div className="login-box">
                    <h2>Login</h2>

                    <form onSubmit={this.loginUser.bind(this)} >

                        <div className="user-box">
                            <input type="text"
                                   id="email"
                                   name="email"
                                   onChange={ this.inputChangeHandler }
                                   required />
                            <label>email</label>
                        </div>

                        <div className="user-box">
                            <input type="password"
                                   id="password"
                                   name="password"
                                   onChange={ this.inputChangeHandler }
                                   required />
                            <label>password</label>
                        </div>

                        <input type="submit" className="button"
                               value="Login"
                            // onClick={this.addDocument}
                        />

                        <div>
                            Have no account yet?
                            <Link className='registration-link' to={'/registration'}>
                                Sign up
                            </Link>
                        </div>
                        <div>
                            or
                        </div>

                        <div>
                            <GoogleLogin
                                clientId='476155838688-163di12pq91fs3tdjht124bp7qn4v3vs.apps.googleusercontent.com'
                                buttonText="Login"
                                onSuccess={ this.responseGoogle.bind(this) }
                                onFailure={ this.responseGoogle.bind(this) }
                                cookiePolicy={'single_host_origin'}
                            />

                        </div>

                    </form>
                </div>
            </div>
        );

        return loginUserForm;
    }
};

