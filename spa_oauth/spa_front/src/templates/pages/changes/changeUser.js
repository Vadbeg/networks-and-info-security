import React from "react";
import Task from "../../../data_retrieving/task";
import {Link} from "react-router-dom";
import Document from "../../../data_retrieving/document";
import Factory from "../../../data_retrieving/factory";
import User from "../../../data_retrieving/user";


export default class ChangeUser extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'user_id': null,

            'first_name': null,
            'second_name': null,
            'is_internal': null,
            'position': null,
            'email': null,
            'phone_number': null,
        }

        this.user = new User(process.env.REACT_APP_ROOT_BACKEND_URI);
    }

    componentDidMount() {
        const { user_id } = this.props.match.params;
        let user_description = this.user.get_one_user(user_id);

        this.setState({
            'user_id': user_id,

            'first_name': user_description['first_name'],
            'second_name': user_description['second_name'],
            'is_internal': user_description['is_internal'],
            'position': user_description['position'],
            'email': user_description['email'],
            'phone_number': user_description['phone_number'],
        })
    }

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

    changeUser = (event) => {
        event.preventDefault();

        const {
            user_id,
            first_name, second_name,
            is_internal, position,
            email, phone_number
        } = this.state;

        this.user.change_user(
            user_id,
            first_name, second_name,
            is_internal, position,
            email, phone_number
        )

        this.props.history.push('/usersTable')
    }

    render() {
        const {
            first_name, second_name,
            is_internal, position,
            email, phone_number
        } = this.state;

        let changeUserForm = (
            <div>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

                <div className="login-box">
                    <h2>Create new user</h2>

                    <form onSubmit={ this.changeUser.bind(this) }>

                        <div className="user-box">
                            <input type="text"
                                   id="first_name"
                                   value={ first_name }
                                   onChange={ this.inputChangeHandler }
                                   name="first_name" required />
                            <label>first_name</label>
                        </div>

                        <div className="user-box">
                            <input type="text"
                                   id="second_name"
                                   value={ second_name }
                                   onChange={ this.inputChangeHandler }
                                   name="second_name" required />
                            <label>second_name</label>
                        </div>

                        <div className="user-box">
                            <input type="text"
                                   id="position"
                                   value={ position }
                                   onChange={ this.inputChangeHandler }
                                   name="position" required />
                            <label>position</label>
                        </div>

                        <div className="user-box">
                            <input type="text"
                                   name="email"
                                   value={ email }
                                   onChange={ this.inputChangeHandler }
                                   id="email" required />
                            <label>email</label>
                        </div>

                        <div className="user-box">
                            <input type="text"
                                   name="phone_number"
                                   value={ phone_number }
                                   onChange={ this.inputChangeHandler }
                                   id="phone_number" required />
                            <label>phone_number</label>
                        </div>

                        <div className="user-box">
                            <input type="checkbox"
                                   name="is_internal"
                                   id="is_internal"
                                   checked={ is_internal }
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

        return changeUserForm;
    }
};

