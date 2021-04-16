import React from 'react';
import ReactDOM from 'react-dom';
import {Redirect, Route, Switch, withRouter} from "react-router-dom";

import Home from "./templates/pages/home";
import DocumentsTable from "./templates/pages/tables/documentsTable";
import FactoriesTable from "./templates/pages/tables/factoriesTable";
import TasksTable from "./templates/pages/tables/tasksTable";
import UsersTable from "./templates/pages/tables/usersTable";

import AddDocument from "./templates/pages/inputs/addDocument";
import AddUser from "./templates/pages/inputs/addUser";
import AddFactory from "./templates/pages/inputs/addFactory";
import AddTask from "./templates/pages/inputs/addTask";

import SettingsDocument from "./templates/pages/settings/settingsDocument";

import ChangeDocument from "./templates/pages/changes/changeDocument";

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

                    <Route history={history} path='/addDocument' component={AddDocument} />
                    <Route history={history} path='/addUser' component={AddUser} />
                    <Route history={history} path='/addFactory' component={AddFactory} />
                    <Route history={history} exact path='/addTask' component={AddTask} />
                    <Route history={history} exact path='/addTask/:document_id' component={AddTask} />

                    <Route history={history} path='/settingsDocument/:document_id' component={SettingsDocument} />

                    <Route history={history} path='/changeDocument/:document_id' component={ChangeDocument} />


                    <Redirect from='/' to='/home'/>
                </Switch>
            </div>
        );

        return myfirstelement
    }
}

export default withRouter(App);
