import React from "react";
import {Link} from "react-router-dom";

import AppUser from "../../../data_retrieving/appUser";


export default class Registration extends React.Component {
    constructor(props) {
        super(props);

        console.log(props)
        console.log('Creating document table')

        this.state = {
            'email': null,
            'password': null,
            'password_repeat': null
        }

        this.appUser = new AppUser(process.env.REACT_APP_ROOT_BACKEND_URI);
    }

    componentDidMount() {

    }

    inputChangeHandler = (event) => {
        var name = event.target.name;
        let value = event.target.value;

        if ((name==='password_repeat') && (value !== this.state['password'])) {
            event.target.style.color = 'red';
        } else {
            event.target.style.color = '';
        }

        this.setState({[name]: value})
    }

    registerUser = (event) => {
        event.preventDefault();

        const {
            email,
            password,
            password_repeat
        } = this.state;
        const { setToken } = this.props

        if (password !== password_repeat) {
            alert('Passwords are not equal!')
        } else {
            let response = this.appUser.register_user(
                email,
                password
            )

            if (response === 403){
                alert('User with given email exists')
            } else if (response !== null) {
                let {auth_token} = response;

                setToken(auth_token);
            }

        }

    }

    render() {

        let loginUserForm = (
            <div>
                <Link className='button-link' to={'/home'}>
                    Login
                </Link>

                <div className="login-box">
                    <h2>Login</h2>

                    <form onSubmit={this.registerUser.bind(this)} >

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

                        <div className="user-box">
                            <input type="password"
                                   id="password_repeat"
                                   name="password_repeat"
                                   onChange={ this.inputChangeHandler }
                                   required />
                            <label>password</label>
                        </div>

                        <input type="submit" className="button"
                               value="Register"
                            // onClick={this.addDocument}
                        />
                    </form>
                </div>
            </div>
        );

        return loginUserForm;
    }
};

