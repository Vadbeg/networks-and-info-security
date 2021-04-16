import React from "react";
import Document from "../../../data_retrieving/document";
import User from "../../../data_retrieving/user";
import {Link} from "react-router-dom";


export default class ChangeDocument extends React.Component {
    constructor(props) {
        super(props);

        console.log('Creating document table')

        this.state = {
            'all_users': [],
            'document_name': null,
            'document_type': null,
            'date_of_creation': null,
            'date_of_registration': null,
            'choose_creators': [],
            'choose_controllers': [],
        }

        this.document = new Document('http://0.0.0.0:9000/api/v_0/');
        this.user = new User('http://0.0.0.0:9000/api/v_0/');
    }

    componentDidMount() {
        const { document_id } = this.props.match.params;
        let one_document = this.document.get_one_document(document_id);

        let creator_ids = [];
        let controller_ids = [];

        if (one_document !== undefined) {
            one_document = one_document[0];
            let creators_info = one_document['creators'];
            let controllers_info = one_document['controllers'];

            for (let i = 0; i < creators_info.length; i++) {
                let curr_creator_id = creators_info[i]['id'];
                creator_ids.push(curr_creator_id);
            }

            for (let i = 0; i < controllers_info.length; i++) {
                let curr_controller_id = controllers_info[i]['id'];
                controller_ids.push(curr_controller_id);
            }
        }

        let all_users = this.user.get_all_users();

        console.log('one_document', one_document)

        this.setState({
            'all_users': all_users,

            'document_id': one_document['id'],
            'document_name': one_document['document_name'],
            'document_type': one_document['document_type'],
            'date_of_creation': one_document['date_of_creation'],
            'date_of_registration': one_document['date_of_registration'],
            'choose_creators': creator_ids,
            'choose_controllers': controller_ids,
        })
    }

    inputChangeHandler = (event) => {
        let name = event.target.name;

        if (name === 'choose_creators' || name === 'choose_controllers') {
            let options = event.target.options;
            let value = [];

            for (var i = 0; i < options.length; i++) {
                console.log(name, options[i].selected);

                if (options[i].selected) {
                    value.push(options[i].value);
                }
            }

            this.setState({[name]: value});
        } else {
            let value = event.target.value;

            this.setState({[name]: value})
        }
    }

    addDocument = (event) => {
        event.preventDefault();

        const {
            document_id,
            document_name, document_type,
            date_of_creation, date_of_registration,
            choose_creators, choose_controllers
        } = this.state;

        this.document.change_document(
            document_id,
            document_name,
            document_type,
            choose_creators,
            choose_controllers,
            date_of_creation,
            date_of_registration
        )

        this.props.history.push(`/settingsDocument/${document_id}`)
    }

    getUserOptions(all_users) {
        let userOptions = [];

        if (all_users !== undefined) {
            for (let i=0; i < all_users.length; i++){
                let curr_user = all_users[i];

                userOptions.push(
                    <option value={ curr_user['id'] }>
                        { curr_user['id'] }. { curr_user['first_name'] } { curr_user['second_name'] }
                    </option>
                );
            }
        }

        return userOptions;
    }

    render() {
        const {
            all_users, document_id,
            document_name, document_type,
            date_of_creation, date_of_registration,
            choose_creators, choose_controllers
        } = this.state;

        let userOptions = this.getUserOptions(all_users);

        console.log(choose_controllers)

        let changeDocumentForm = (
            <div>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

                <div className="login-box">
                    <h2>Create new document</h2>

                    <form onSubmit={ this.addDocument.bind(this) }>

                        <div className="user-box">
                            <input type="text"
                                   id="document_name"
                                   name="document_name"
                                   value={ document_name }
                                   onChange={ this.inputChangeHandler }
                                   required />
                            <label>document_name</label>
                        </div>

                        <div className="user-box">
                            <input type="text"
                                   id="document_type"
                                   name="document_type"
                                   value={ document_type }
                                   onChange={ this.inputChangeHandler }
                                   required />
                            <label>document_type</label>
                        </div>

                        <div className="user-box">
                            <input type="date" style={{ textAlign: 'right' }}
                                   id="date_of_creation"
                                   name="date_of_creation"
                                   value={ date_of_creation }
                                   onChange={ this.inputChangeHandler }
                                   required />
                            <label>date_of_creation</label>
                        </div>

                        <div className="user-box">
                            <input type="date" style={{ textAlign: 'right' }}
                                   name="date_of_registration"
                                   id="date_of_registration"
                                   value={ date_of_registration }
                                   onChange={ this.inputChangeHandler }
                                   required />
                            <label>date_of_registration</label>
                        </div>

                        <div className="user-box">
                            <select style={{ textAlign: 'right' }}
                                    name="choose_creators"
                                    id="creators"
                                    value={ choose_creators }
                                    onChange={ this.inputChangeHandler }
                                    required multiple>
                                {userOptions}
                            </select>
                            <label className="select-label">choose_creators</label>
                        </div>

                        <div className="user-box" style={{clear: 'both'}}>
                            <select style={{ textAlign: 'right' }}
                                    name="choose_controllers"
                                    id="controllers"
                                    value={ choose_controllers }
                                    onChange={ this.inputChangeHandler }
                                    required multiple>
                                {userOptions}
                            </select>
                            <label>choose_controllers</label>
                        </div>

                        <div className="user-box" style={{clear: 'both'}}>
                            * you can add tasks on document page
                        </div>

                        <input type="submit" className="button"
                               value="Register"
                            // onClick={this.addDocument}
                        />
                    </form>
                </div>
            </div>
        );

        return changeDocumentForm;
    }
};

