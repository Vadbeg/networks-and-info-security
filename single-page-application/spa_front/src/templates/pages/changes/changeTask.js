import React from "react";
import Task from "../../../data_retrieving/task";
import {Link} from "react-router-dom";
import Document from "../../../data_retrieving/document";
import Factory from "../../../data_retrieving/factory";
import User from "../../../data_retrieving/user";


export default class ChangeTask extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'factory_name': null,
            'size': null,
            'city': null,
        }

        this.task = new Task('http://0.0.0.0:9000/api/v_0/');

        this.document = new Document('http://0.0.0.0:9000/api/v_0/');
        this.factory = new Factory('http://0.0.0.0:9000/api/v_0/');
        this.user = new User('http://0.0.0.0:9000/api/v_0/');
    }

    componentDidMount() {
        const { task_id } = this.props.match.params;
        let task_description = this.task.get_one_task(task_id);

        let all_documents = this.document.get_all_documents();
        let all_factories = this.factory.get_all_factories();
        let all_users = this.user.get_all_users();

        this.setState({
            'task_id': task_id,

            'all_factories': all_factories,
            'all_documents': all_documents,
            'all_users': all_users,

            'task_name': task_description['task_name'],
            'executor_id': task_description['executor_id'],
            'document_id': task_description['document_id'],
            'factory_id': task_description['factory_id'],
        })
    }

    inputChangeHandler = (event) => {
        var name = event.target.name;
        let value = event.target.value;

        this.setState({[name]: value})
    }

    changeTask = (event) => {
        event.preventDefault();

        const {
            task_id,
            task_name,
            executor_id,
            document_id,
            factory_id
        } = this.state;

        this.task.change_task(
            task_id,
            task_name,
            executor_id,
            document_id,
            factory_id
        )

        this.props.history.push('/tasksTable')
    }

    getOptionsForUsers(all_users) {
        let usersOptions = [];

        if (all_users !== undefined) {
            for (let i=0; i < all_users.length; i++){
                let curr_user = all_users[i];

                usersOptions.push(
                    <option value={ curr_user['id'] }>
                        { curr_user['id'] }. { curr_user['first_name'] } { curr_user['second_name'] }
                    </option>
                );
            }
        }

        return usersOptions;
    }

    getOptionsForDocuments(all_documents) {
        let documentsOptions = [];

        if (all_documents !== undefined) {
            for (let i=0; i < all_documents.length; i++){
                let curr_document = all_documents[i];

                documentsOptions.push(
                    <option value={ curr_document['id'] }>
                        { curr_document['id'] }. { curr_document['document_name'] }
                    </option>
                );
            }
        }

        return documentsOptions;
    }

    getOptionsForFactories(all_factories) {
        let factoriesOptions = [];

        if (all_factories !== undefined) {
            for (let i=0; i < all_factories.length; i++){
                let curr_factory = all_factories[i];

                factoriesOptions.push(
                    <option value={ curr_factory['id'] }>
                        { curr_factory['id'] }. { curr_factory['factory_name'] }
                    </option>
                );
            }
        }

        return factoriesOptions;
    }

    render() {
        const {
            all_factories, all_documents, all_users,
            task_name, executor_id, document_id,
            factory_id
        } = this.state;

        let userOptions = this.getOptionsForUsers(all_users);
        let documentOptions = this.getOptionsForDocuments(all_documents);
        let factoryOptions = this.getOptionsForFactories(all_factories);

        let changeTaskForm = (
            <div>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

                <div className="login-box">
                    <h2>Create new factory</h2>

                    <form onSubmit={ this.changeTask.bind(this) }>

                        <div className="user-box">
                            <input type="text"
                                   id="task_name"
                                   value={task_name}
                                   onChange={ this.inputChangeHandler }
                                   name="task_name" required />
                            <label>task_name</label>
                        </div>

                        <div className="user-box" style={{clear: 'both'}}>
                            <select style={{ textAlign: 'right' }}
                                    name="executor_id"
                                    id="executor_id"
                                    value={executor_id}
                                    onChange={ this.inputChangeHandler }
                                    required>
                                {userOptions}
                            </select>
                            <label>choose_executor</label>
                        </div>

                        <div className="user-box" style={{clear: 'both'}}>
                            <select style={{ textAlign: 'right' }}
                                    name="document_id"
                                    id="document_id"
                                    value={document_id}
                                    onChange={ this.inputChangeHandler }
                                    required>
                                {documentOptions}
                            </select>
                            <label>choose_document</label>
                        </div>

                        <div className="user-box" style={{clear: 'both'}}>
                            <select style={{ textAlign: 'right' }}
                                    name="factory_id"
                                    id="factory_id"
                                    value={factory_id}
                                    onChange={ this.inputChangeHandler }
                                    required>
                                {factoryOptions}
                            </select>
                            <label>choose_factory</label>
                        </div>

                        <input type="submit" className="button"
                               value="Register"
                        />
                    </form>
                </div>
            </div>
        );

        return changeTaskForm;
    }
};

