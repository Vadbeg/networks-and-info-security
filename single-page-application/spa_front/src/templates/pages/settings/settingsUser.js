import React from "react";
import User from "../../../data_retrieving/user";
import {Link} from "react-router-dom";


export default class SettingsUser extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'user_description': [],
        }

        this.user = new User(process.env.REACT_APP_ROOT_BACKEND_URI);
    }

    componentDidMount() {
        const { user_id } = this.props.match.params;

        let user_description = this.user.get_one_user(user_id);

        this.setState({
            'user_description': user_description,
        })
    }

    delete_user = () => {
        const { user_description } = this.state;

        this.user.delete_user(user_description['id'])

        this.props.history.push('/usersTable')
    }

    render() {
        const { user_description } = this.state;

        console.log(user_description['is_internal'])

        let addUserSettings = (
            <div>
                <table className="styled-table">
                    <tbody>
                    <tr>
                        <td>id</td>
                        <td>{ user_description['id'] }</td>
                    </tr>

                    <tr>
                        <td>name</td>
                        <td>
                            { user_description['first_name'] } { user_description['second_name'] }
                        </td>
                    </tr>

                    <tr>
                        <td>is_internal</td>
                        <td>{ '' + user_description['is_internal'] }</td>
                    </tr>

                    <tr>
                        <td>position</td>
                        <td>{ user_description['position'] }</td>
                    </tr>

                    <tr>
                        <td>email</td>
                        <td>{ user_description['email'] }</td>
                    </tr>

                    <tr>
                        <td>phone_number</td>
                        <td>{ user_description['phone_number'] }</td>
                    </tr>
                    </tbody>
                </table>

                <Link className="button-link" to={`/changeUser/${user_description['id']}`}>
                    Change user
                </Link>
                <Link className="button-link" onClick={ this.delete_user }>
                    Delete user
                </Link>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

            </div>
        );

        return addUserSettings;
    }
}

