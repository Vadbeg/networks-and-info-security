import React from 'react';
import ReactDOM from 'react-dom';
import {Redirect, Route, Switch, withRouter} from "react-router-dom";

import Home from "./templates/pages/home";
import DocumentsTable from "./templates/pages/tables/documentsTable";
import FactoriesTable from "./templates/pages/tables/factoriesTable";
import TasksTable from "./templates/pages/tables/tasksTable";
import UsersTable from "./templates/pages/tables/usersTable";

class App extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        const { history } = this.props;

        let myfirstelement = (
            <div>
                <Switch>
                    <Route history={history} path='/home' component={Home} />
                    <Route history={history} path='/documentsTable' component={DocumentsTable} />
                    <Route history={history} path='/factoriesTable' component={FactoriesTable} />
                    <Route history={history} path='/tasksTable' component={TasksTable} />
                    <Route history={history} path='/usersTable' component={UsersTable} />
                    <Redirect from='/' to='/home'/>
                </Switch>
            </div>
        );

        return myfirstelement
    }
}

export default withRouter(App);
