import React from "react";
import Document from "../../../data_retrieving/document";
import User from "../../../data_retrieving/user";
import Task from "../../../data_retrieving/task";
import {Link} from "react-router-dom";


export default class SettingsTask extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'task_description': [],
        }

        this.task = new Task('http://0.0.0.0:9000/api/v_0/');
    }

    componentDidMount() {
        const { task_id } = this.props.match.params;

        let task_description = this.task.get_one_task(task_id);

        this.setState({
            'task_description': task_description,
        })
    }

    delete_task = () => {
        const { task_description } = this.state;

        this.task.delete_task(task_description['id'])

        this.props.history.push('/tasksTable')
    }

    render() {
        const { task_description } = this.state;

        let addTaskSettings = (
            <div>
                <table className="styled-table">
                    <tbody>
                    <tr>
                        <td>id</td>
                        <td>{ task_description['id'] }</td>
                    </tr>

                    <tr>
                        <td>task_name</td>
                        <td>
                            { task_description['task_name'] }
                        </td>
                    </tr>

                    <tr>
                        <td>executor_id</td>
                        <td>{ task_description['executor_id'] }</td>
                    </tr>

                    <tr>
                        <td>document_id</td>
                        <td>{ task_description['document_id'] }</td>
                    </tr>

                    <tr>
                        <td>factory_id</td>
                        <td>{ task_description['factory_id'] }</td>
                    </tr>

                    </tbody>
                </table>

                <Link className="button-link" to={`/changeTask/${task_description['id']}`}>
                    Change task
                </Link>
                <Link className="button-link" onClick={ this.delete_task }>
                    Delete task
                </Link>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

            </div>
        );

        return addTaskSettings;
    }
}

