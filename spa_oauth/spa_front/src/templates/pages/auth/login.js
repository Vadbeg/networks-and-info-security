import React from "react";
import {Link} from "react-router-dom";

import AppUser from "../../../data_retrieving/appUser";


export default class Login extends React.Component {
    constructor(props) {
        super(props);

        console.log(props)
        console.log('Creating document table')

        this.state = {
            'email': null,
            'password': null,
        }

        this.appUser = new AppUser(process.env.REACT_APP_ROOT_BACKEND_URI);
    }

    componentDidMount() {

    }

    inputChangeHandler = (event) => {
        var name = event.target.name;
        let value = event.target.value;

        this.setState({[name]: value})
    }

    registerUser = (event) => {
        event.preventDefault();

        const {
            email,
            password,
        } = this.state;
        const { setToken } = this.props

        let response = this.appUser.register_user(
            email,
            password
        )

        let { auth_token } = response;
        console.log(auth_token)
        console.log(setToken)

        setToken(auth_token);
    }

    render() {

        let loginUserForm = (
            <div>

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

                        <input type="submit" className="button"
                               value="Login"
                            // onClick={this.addDocument}
                        />

                        Have no account yet?
                        <Link className='registration-link' to={'/registration'}>
                            Sign up
                        </Link>

                    </form>
                </div>
            </div>
        );

        return loginUserForm;
    }
};

