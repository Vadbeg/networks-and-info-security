import React from "react";
import Factory from "../../../data_retrieving/factory";
import Document from "../../../data_retrieving/document";
import Task from "../../../data_retrieving/task";
import User from "../../../data_retrieving/user";

import {Link} from "react-router-dom";


export default class AddTask extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'all_factories': [],
            'all_documents': [],
            'all_users': [],

            'task_name': null,
            'executor_id': null,
            'document_id': null,
            'factory_id': null,
        }

        this.factory = new Factory(process.env.REACT_APP_ROOT_BACKEND_URI);
        this.document = new Document(process.env.REACT_APP_ROOT_BACKEND_URI);
        this.user = new User(process.env.REACT_APP_ROOT_BACKEND_URI);

        this.task = new Task(process.env.REACT_APP_ROOT_BACKEND_URI);
    }

    componentDidMount() {
        const { document_id } = this.props.match.params;

        console.log('document_id', document_id)

        let all_documents = []
        if (document_id !== undefined) {
            let one_document = this.document.get_one_document(document_id);
            all_documents = [one_document[0]];

            console.log('all_documents', all_documents)
        } else {
            all_documents = this.document.get_all_documents();
        }

        let all_factories = this.factory.get_all_factories();
        let all_users = this.user.get_all_users();

        let factory_id_default = null
        if ((all_factories !== undefined) && (all_factories[0] !== undefined)) {
            factory_id_default = all_factories[0]['id']
        }

        let document_id_default = null
        if ((all_documents !== undefined) && (all_documents[0] !== undefined)) {
            document_id_default = all_documents[0]['id']
        }

        let executor_id_default = null
        if ((all_users !== undefined) && (all_users[0] !== undefined)) {
            executor_id_default = all_users[0]['id']
        }

        this.setState({
            'all_factories': all_factories,
            'all_documents': all_documents,
            'all_users': all_users,

            'factory_id': factory_id_default,
            'document_id': document_id_default,
            'executor_id': executor_id_default,
        })
    }


    inputChangeHandler = (event) => {
        var name = event.target.name;
        let value = event.target.value;

        this.setState({[name]: value})
    }

    addTask = (event) => {
        event.preventDefault();

        const {
            task_name,
            executor_id,
            document_id,
            factory_id
        } = this.state;

        this.task.add_task(
            task_name,
            executor_id,
            document_id,
            factory_id
        )

        const document_id_query  = this.props.match.params['document_id'];

        if (document_id_query !== undefined) {
            this.props.history.push(`/settingsDocument/${document_id_query}`)
        } else {
            this.props.history.push('/tasksTable')
        }

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
        const { all_factories, all_documents, all_users } = this.state;

        let userOptions = this.getOptionsForUsers(all_users);
        let documentOptions = this.getOptionsForDocuments(all_documents);
        let factoryOptions = this.getOptionsForFactories(all_factories);

        let defaultUser = null
        if (all_users.length !== 0){
            defaultUser = all_users[0]['id']
        }

        let addTaskForm = (
            <div>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

                <div className="login-box">
                    <h2>Create new factory</h2>

                    <form onSubmit={ this.addTask.bind(this) }>

                        <div className="user-box">
                            <input type="text"
                                   id="task_name"
                                   onChange={ this.inputChangeHandler }
                                   name="task_name" required />
                            <label>task_name</label>
                        </div>

                        <div className="user-box" style={{clear: 'both'}}>
                            <select style={{ textAlign: 'right' }}
                                    name="executor_id"
                                    id="executor_id"
                                    onChange={ this.inputChangeHandler }
                                    defaultValue={ defaultUser }
                                    required>
                                {userOptions}
                            </select>
                            <label>choose_executor</label>
                        </div>

                        <div className="user-box" style={{clear: 'both'}}>
                            <select style={{ textAlign: 'right' }}
                                    name="document_id"
                                    id="document_id"
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

        return addTaskForm;
    }
};

