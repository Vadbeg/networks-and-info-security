import React from "react";
import Factory from "../../../data_retrieving/factory";
import {Link} from "react-router-dom";


export default class AddFactory extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'factory_name': null,
            'size': null,
            'city': null,
        }

        this.factory = new Factory('http://0.0.0.0:9000/api/v_0/');
    }

    inputChangeHandler = (event) => {
        var name = event.target.name;
        let value = event.target.value;

        this.setState({[name]: value})
    }

    addFactory = (event) => {
        event.preventDefault();

        const {
            factory_name,
            size,
            city
        } = this.state;

        this.factory.add_factory(
            factory_name,
            size,
            city,
        )

        this.props.history.push('/factoriesTable')
    }

    render() {

        let addFactoryForm = (
            <div>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

                <div className="login-box">
                    <h2>Create new factory</h2>

                    <form onSubmit={ this.addFactory.bind(this) }>

                        <div className="user-box">
                            <input type="text"
                                   id="factory_name"
                                   onChange={ this.inputChangeHandler }
                                   name="factory_name" required />
                            <label>factory_name</label>
                        </div>

                        <div className="user-box">
                            <input type="text"
                                   id="size"
                                   onChange={ this.inputChangeHandler }
                                   name="size" required />
                            <label>size</label>
                        </div>

                        <div className="user-box">
                            <input type="text"
                                   id="city"
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

        return addFactoryForm;
    }
};

