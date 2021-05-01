import React from "react";
import Factory from "../../../data_retrieving/factory";
import {Link} from "react-router-dom";


export default class ChangeFactory extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'factory_name': null,
            'size': null,
            'city': null,
        }

        this.factory = new Factory(process.env.REACT_APP_ROOT_BACKEND_URI);
    }

    componentDidMount() {
        const { factory_id } = this.props.match.params;
        let one_factory = this.factory.get_one_factory(factory_id);

        this.setState({
            'factory_id': factory_id,

            'factory_name': one_factory['factory_name'],
            'size': one_factory['size'],
            'city': one_factory['city'],
        })
    }

    inputChangeHandler = (event) => {
        var name = event.target.name;
        let value = event.target.value;

        this.setState({[name]: value})
    }

    changeFactory = (event) => {
        event.preventDefault();

        const {
            factory_id,
            factory_name,
            size,
            city
        } = this.state;

        this.factory.change_factory(
            factory_id,
            factory_name,
            size,
            city,
        )

        this.props.history.push('/factoriesTable')
    }

    render() {
        const {
            factory_name,
            size, city
        } = this.state;

        let changeFactoryForm = (
            <div>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

                <div className="login-box">
                    <h2>Create new factory</h2>

                    <form onSubmit={ this.changeFactory.bind(this) }>

                        <div className="user-box">
                            <input type="text"
                                   id="factory_name"
                                   value={ factory_name }
                                   onChange={ this.inputChangeHandler }
                                   name="factory_name" required />
                            <label>factory_name</label>
                        </div>

                        <div className="user-box">
                            <input type="text"
                                   id="size"
                                   value={ size }
                                   onChange={ this.inputChangeHandler }
                                   name="size" required />
                            <label>size</label>
                        </div>

                        <div className="user-box">
                            <input type="text"
                                   id="city"
                                   value={ city }
                                   onChange={ this.inputChangeHandler }
                                   name="city" required />
                            <label>city</label>
                        </div>

                        <input type="submit" className="button"
                               value="Register"
                            // onClick={this.addDocument}
                        />
                    </form>
                </div>
            </div>
        );

        return changeFactoryForm;
    }
};

