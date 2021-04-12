import React from 'react';
import ReactDOM from 'react-dom';
import {Redirect, Route, Switch, withRouter} from "react-router-dom";

import Home from "./templates/pages/home";
import DocumentsTable from "./templates/pages/tables/documentsTable";

// class App extends React.Component {
//     // constructor(props) {
//     //     super(props);
//     // }
//
//     render() {
//         const { history } = this.props;
//
//         let myfirstelement = (
//             <div>
//                 <Switch>
//                     <Route history={history} path='/home' component={Home} />
//                     <Route history={history} path='/documentsTable' component={DocumentsTable} />
//                     <Redirect from='/' to='/home'/>
//                 </Switch>
//             </div>
//         );
//
//         return myfirstelement
//     }
// }

class App extends React.Component {
    render() {
        const { history } = this.props

        return (
            <div className="App">
                <Switch>
                    <Route history={history} path='/documentsTable' component={DocumentsTable} />
                    <Route history={history} path='/home' component={Home} />
                    <Redirect from='/' to='/home'/>
                </Switch>
            </div>
        );
    }
}

export default withRouter(App);
