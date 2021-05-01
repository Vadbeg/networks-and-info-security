import React from "react";
import Factory from "../../../data_retrieving/factory";
import {Link} from "react-router-dom";


export default class SettingsFactory extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'factory_description': [],
        }

        this.factory = new Factory(process.env.REACT_APP_ROOT_BACKEND_URI);
    }

    componentDidMount() {
        const { factory_id } = this.props.match.params;

        let factory_description = this.factory.get_one_factory(factory_id);

        this.setState({
            'factory_description': factory_description,
        })
    }

    delete_factory = () => {
        const { factory_description } = this.state;

        this.factory.delete_factory(factory_description['id'])

        this.props.history.push('/factoriesTable')
    }

    render() {
        const { factory_description } = this.state;

        let addFactorySettings = (
            <div>
                <table className="styled-table">
                    <tbody>
                    <tr>
                        <td>id</td>
                        <td>{ factory_description['id'] }</td>
                    </tr>

                    <tr>
                        <td>factory_name</td>
                        <td>{ factory_description['factory_name'] }</td>
                    </tr>

                    <tr>
                        <td>size</td>
                        <td>{ factory_description['size'] }</td>
                    </tr>

                    <tr>
                        <td>city</td>
                        <td>{ factory_description['city'] }</td>
                    </tr>

                    </tbody>
                </table>

                <Link className="button-link" to={`/changeFactory/${factory_description['id']}`}>
                    Change factory
                </Link>
                <Link className="button-link" onClick={ this.delete_factory }>
                    Delete factory
                </Link>
                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>

            </div>
        );

        return addFactorySettings;
    }
}

