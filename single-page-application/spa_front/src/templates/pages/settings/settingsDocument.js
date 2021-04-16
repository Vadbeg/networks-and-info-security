import React from "react";
import Document from "../../../data_retrieving/document";
import User from "../../../data_retrieving/user";
import {Link} from "react-router-dom";


export default class SettingsDocument extends React.Component {
    constructor(props) {
        super(props);

        console.log('Creating document table')

        this.state = {
            'document_description': [],
            'all_document_tasks': []
        }

        this.document = new Document('http://0.0.0.0:9000/api/v_0/');
    }

    componentDidMount() {
        console.log(this.props)
        const { document_id } = this.props.match.params;

        let document_info = this.document.get_one_document(document_id);

        let document_description = document_info[0]
        let all_document_tasks = document_info[1]

        console.log(document_info)

        this.setState({
            'document_description': document_description,
            'all_document_tasks': all_document_tasks
        })
    }

    get_users_info(all_users) {
        let users_info = [];

        if (all_users !== undefined) {
            for (let i=0; i < all_users.length; i++){
                let curr_user = all_users[i];

                users_info.push(
                    <span style={{ display: 'block' }}>
                        { curr_user['first_name'] } { curr_user['second_name'] }
                    </span>
                );
            }
        }

        return users_info;
    }

    get_tasks_info(all_tasks) {
        let tasks_info = [];

        if (all_tasks !== undefined) {
            for (let i=0; i < all_tasks.length; i++){
                let curr_task = all_tasks[i];

                tasks_info.push(
                    <tr>
                        <td>{ curr_task['id'] }</td>
                        <td>{ curr_task['task_name'] }</td>
                        <td>{ curr_task['executor_id'] }</td>
                        <td>{ curr_task['document_id'] }</td>
                    </tr>
                );
            }
        }

        return tasks_info;
    }

    delete_document = () => {
        console.log('this.state', this.state)

        const { document_description } = this.state;

        this.document.delete_document(document_description['id'])

        this.props.history.push('/documentsTable')
    }

    render() {
        const { document_description, all_document_tasks } = this.state;
        const { controllers, creators } = document_description;


        let controllers_info = this.get_users_info(controllers);
        let creators_info = this.get_users_info(creators);

        let tasks_info = this.get_tasks_info(all_document_tasks);

        let addDocumentSettings = (
            <div>
                <table className="styled-table">
                    <tbody>
                    <tr>
                        <td>id</td>
                        <td>{ document_description['id'] }</td>
                    </tr>

                    <tr>
                        <td>document_name</td>
                        <td>{ document_description['document_name'] }</td>
                    </tr>

                    <tr>
                        <td>document_type</td>
                        <td>{ document_description['document_type'] }</td>
                    </tr>

                    <tr>
                        <td>date_of_creation</td>
                        <td>{ document_description['date_of_creation'] }</td>
                    </tr>

                    <tr>
                        <td>date_of_registration</td>
                        <td>{ document_description['date_of_registration'] }</td>
                    </tr>

                    <tr>
                        <td>creators</td>
                        <td>
                            { creators_info }
                        </td>
                    </tr>

                    <tr>
                        <td>controllers</td>
                        <td>
                            { controllers_info }
                        </td>
                    </tr>
                    </tbody>
                </table>


                <table className="styled-table">
                    <thead>
                    <tr>
                        <th>id</th>
                        <th>task_name</th>
                        <th>executor_id</th>
                        <th>document_id</th>
                    </tr>
                    </thead>
                    <tbody>
                    { tasks_info }
                    </tbody>
                </table>

                <Link className="button-link" to={`/addTask/${document_description['id']}`}>
                    Add new task
                </Link>
                {/*<a href="{{ url_for('change_documentation.change_document', document_idx=document_description.id) }}"*/}
                {/*   className="button-link">Change document</a>*/}
                <Link className="button-link" onClick={ this.delete_document }>Delete document</Link>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

            </div>
        );

        return addDocumentSettings;
    }
}

