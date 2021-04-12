import React from "react";
import Document from "../../../data_retrieving/document";


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
        let documents_info = this.document.get_all_documents();
        let all_documents = documents_info[0];

        this.setState({
            'all_documents': all_documents
        })
    }

    render() {
        const { all_documents } = this.state;

        console.log(all_documents)

        // let documents_info = this.document.get_all_documents();

        // let all_documents = documents_info[0];

        let documentRows = [];

        for (let i=0; i < all_documents.length; i++){
            let curr_document = all_documents[i]

            documentRows.push(
                <tr>
                    <td>{ curr_document['id'] }</td>
                    <td>
                        <a>
                            { curr_document['document_name'] }
                        </a>
                    </td>
                    <td>{ curr_document['document_type'] }</td>
                    <td>{ curr_document['date_of_creation'] }</td>
                    <td>{ curr_document['date_of_registration'] }</td>
                </tr>
            )
        }

        let documentsTable = (
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
        );

        console.log('Rendered table')

        return documentsTable;
    }
};

