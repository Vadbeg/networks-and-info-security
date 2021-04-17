import React from "react";
import Task from "../../../data_retrieving/task";
import {Link} from "react-router-dom";


export default class TasksTable extends React.Component {
    constructor(props) {
        super(props);

        console.log('Creating document table')

        this.state = {
            'all_tasks': []
        }

        this.task = new Task('http://0.0.0.0:9000/api/v_0/');
    }

    componentDidMount() {
        let all_tasks = this.task.get_all_tasks();

        this.setState({
            'all_tasks': all_tasks
        })
    }

    render() {
        const { all_tasks } = this.state;

        let tasksRows = [];

        if (all_tasks !== undefined) {
            for (let i=0; i < all_tasks.length; i++){
                let curr_task = all_tasks[i]

                console.log('task_name', curr_task['task_name'])

                tasksRows.push(
                    <tr>
                        <td>{ curr_task['id'] }</td>
                        <td>
                            <Link to={`/settingsTask/${curr_task.id}`}>
                                { curr_task['task_name'] }
                            </Link>
                        </td>
                        <td>{ curr_task['executor_id'] }</td>
                        <td>{ curr_task['document_id'] }</td>
                        <td>{ curr_task['factory_id'] }</td>
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
                                <th>task_name</th>
                                <th>executor_id</th>
                                <th>document_id</th>
                                <th>factory_id</th>
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

