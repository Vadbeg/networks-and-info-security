import React from "react";
import Document from "../../../data_retrieving/document";
import {Link} from "react-router-dom";


export default class DocumentsTable extends React.Component {
    constructor(props) {
        super(props);

        console.log('Creating document table')

        this.state = {
            'all_documents': []
        }

        this.document = new Document('http://0.0.0.0:9000/api/v_0/');
    }

    componentDidMount() {
        let all_documents = this.document.get_all_documents();

        this.setState({
            'all_documents': all_documents
        })
    }

    render() {
        const { all_documents } = this.state;

        console.log(all_documents)

        let documentRows = [];

        if (all_documents !== undefined) {
            for (let i=0; i < all_documents.length; i++){
                let curr_document = all_documents[i]

                documentRows.push(
                    <tr>
                        <td>{ curr_document['id'] }</td>
                        <td>
                            <Link to={`/settingsDocument/${curr_document.id}`}>
                                { curr_document['document_name'] }
                            </Link>
                        </td>
                        <td>{ curr_document['document_type'] }</td>
                        <td>{ curr_document['date_of_creation'] }</td>
                        <td>{ curr_document['date_of_registration'] }</td>
                    </tr>
                )
            }
        }

        let documentsTable = (
            <div>
                <div id="table-to-update">
                    <table className="styled-table">
                        <thead>
                        <tr>
                            <th>id</th>
                            <th>document_name</th>
                            <th>document_type</th>
                            <th>date_of_creation</th>
                            <th>date_of_registration</th>
                        </tr>
                        </thead>
                        <tbody>
                        {documentRows}
                        </tbody>
                    </table>
                </div>

                <Link className='button-link' to={'/home'}>
                    Go Home
                </Link>
            </div>
        );

        console.log('Rendered table')

        return documentsTable;
    }
};

