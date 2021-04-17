import React from "react";
import Document from "../../../data_retrieving/document";
import User from "../../../data_retrieving/user";
import {Link} from "react-router-dom";


export default class AddUser extends React.Component {
    constructor(props) {
        super(props);

        console.log('Creating document table')

        this.state = {
            'first_name': null,
            'second_name': null,
            'is_internal': false,
            'position': null,
            'email': null,
            'phone_number': null,
        }

        this.user = new User(process.env.REACT_APP_ROOT_BACKEND_URI);
    }

    // componentDidMount() {
    //     let all_users = this.user.get_all_users();
    //
    //     this.setState({
    //         'all_users': all_users
    //     })
    // }

    inputChangeHandler = (event) => {
        var name = event.target.name;
        let value = event.target.value;

        if (name === 'is_internal'){
            let is_internal = event.target.checked;

            this.setState({[name]: is_internal});
        } else {
            this.setState({[name]: value});
        }
    }

    addUser = (event) => {
        event.preventDefault();

        const {
            first_name, second_name,
            is_internal, position,
            email, phone_number
        } = this.state;

        this.user.add_one_user(
            first_name,
            second_name,
            is_internal,
            position,
            email,
            phone_number
        )

        this.props.history.push('/usersTable')
    }

    render() {

        let addUserForm = (
            <div>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

                <div className="login-box">
                    <h2>Create new user</h2>

                    <form onSubmit={ this.addUser.bind(this) }>

                            <div className="user-box">
                                <input type="text"
                                       id="first_name"
                                       onChange={ this.inputChangeHandler }
                                       name="first_name" required />
                                    <label>first_name</label>
                            </div>

                            <div className="user-box">
                                <input type="text"
                                       id="second_name"
                                       onChange={ this.inputChangeHandler }
                                       name="second_name" required />
                                    <label>second_name</label>
                            </div>

                            <div className="user-box">
                                <input type="text"
                                       id="position"
                                       onChange={ this.inputChangeHandler }
                                       name="position" required />
                                    <label>position</label>
                            </div>

                            <div className="user-box">
                                <input type="text"
                                       name="email"
                                       onChange={ this.inputChangeHandler }
                                       id="email" required />
                                    <label>email</label>
                            </div>

                            <div className="user-box">
                                <input type="text"
                                       name="phone_number"
                                       onChange={ this.inputChangeHandler }
                                       id="phone_number" required />
                                    <label>phone_number</label>
                            </div>

                            <div className="user-box">
                                <input type="checkbox"
                                       name="is_internal"
                                       id="is_internal"
                                       onChange={ this.inputChangeHandler }
                                       value="on" />
                                    <label>is_internal</label>
                            </div>

                        <input type="submit" className="button"
                               value="Register"
                            // onClick={this.addDocument}
                        />
                    </form>
                </div>
            </div>
        );

        return addUserForm;
    }
};

