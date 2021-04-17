import React from "react";
import Factory from "../../../data_retrieving/factory";
import {Link} from "react-router-dom";


export default class FactoriesTable extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'all_factories': []
        }

        this.factory = new Factory('http://0.0.0.0:9000/api/v_0/');
    }

    componentDidMount() {
        let factories_info = this.factory.get_all_factories();
        let all_factories = factories_info;

        this.setState({
            'all_factories': all_factories
        })
    }

    render() {
        const { all_factories } = this.state;

        let factoryRows = [];

        if (all_factories !== undefined) {
            for (let i=0; i < all_factories.length; i++){
                let curr_factory = all_factories[i]

                factoryRows.push(
                    <tr>
                        <td>{ curr_factory['id'] }</td>
                        <td>
                            <td>
                                <Link to={`/settingsFactory/${curr_factory.id}`}>
                                    { curr_factory['factory_name'] }
                                </Link>
                            </td>
                        </td>
                        <td>{ curr_factory['size'] }</td>
                        <td>{ curr_factory['city'] }</td>
                    </tr>
                )
            }
        }


        let factoriesTable = (
            <div>
                <div id="table-to-update">
                    <table className="styled-table">
                        <thead>
                            <tr>
                                <th>id</th>
                                <th>Factory name</th>
                                <th>Size</th>
                                <th>City</th>
                            </tr>
                        </thead>
                        <tbody>
                        {factoryRows}
                        </tbody>
                    </table>
                </div>

                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>
            </div>
        );

        console.log('Rendered table')

        return factoriesTable;
    }
};

