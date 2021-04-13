import React from "react";
import User from "../../../data_retrieving/user";
import {Link} from "react-router-dom";


export default class UsersTable extends React.Component {
    constructor(props) {
        super(props);

        console.log('Creating document table')

        this.state = {
            'all_users': []
        }

        this.user = new User('http://0.0.0.0:9000/api/v_0/');
    }

    componentDidMount() {
        let all_users = this.user.get_all_users();

        this.setState({
            'all_users': all_users
        })
    }

    render() {
        const { all_users } = this.state;

        let tasksRows = [];

        if (all_users !== undefined) {
            for (let i=0; i < all_users.length; i++){
                let curr_user = all_users[i]

                tasksRows.push(
                    <tr>
                        <td>{ curr_user['id'] }</td>
                        <td>
                            <a>
                                { curr_user['first_name'] }
                            </a>
                        </td>
                        <td>{ curr_user['second_name'] }</td>
                        <td>{ curr_user['is_internal'] }</td>
                        <td>{ curr_user['position'] }</td>
                        <td>{ curr_user['email'] }</td>
                        <td>{ curr_user['phone_number'] }</td>
                    </tr>
                )
            }
        }

        let tasksTable = (
            <div>
                <div id="table-to-update">
                    <table className="styled-table">
                        <thead>
                            <tr>
                                <th>id</th>
                                <th>First name</th>
                                <th>Last name</th>
                                <th>Is Internal</th>
                                <th>Position</th>
                                <th>Email</th>
                                <th>Phone number</th>
                            </tr>
                        </thead>
                        <tbody>
                        {tasksRows}
                        </tbody>
                    </table>
                </div>

                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>
            </div>
        );

        console.log('Rendered table')

        return tasksTable;
    }
};

