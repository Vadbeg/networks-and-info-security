import React, {useState} from 'react';
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
import SettingsFactory from "./templates/pages/settings/settingsFactory";
import SettingsTask from "./templates/pages/settings/settingsTask";
import SettingsUser from "./templates/pages/settings/settingsUser";

import ChangeDocument from "./templates/pages/changes/changeDocument";
import ChangeFactory from "./templates/pages/changes/changeFactory";
import ChangeTask from "./templates/pages/changes/changeTask";
import ChangeUser from "./templates/pages/changes/changeUser";

import Login from "./templates/pages/auth/login";
import Registration from "./templates/pages/auth/registration";


class App extends React.Component {
    constructor(props) {
        super(props);
    }

    setToken = (userToken) => {
        sessionStorage.setItem('token', JSON.stringify(userToken));

        this.forceUpdate();
    }

    getToken = () => {
        const tokenString = sessionStorage.getItem('token')
        const userToken = JSON.parse(tokenString)

        return userToken
    }

    render() {
        const { history } = this.props;

        let token = this.getToken();

        if (!token){
            let login_element = (
                <div>
                    <Switch>
                        <Route history={history}
                               path='/registration'
                               render={(props) => <Registration setToken={this.setToken} {...props} />} />
                        <Route history={history}
                               path="/login"
                               render={(props) => <Login setToken={this.setToken} {...props} />} />

                        <Redirect from='/' to='/login'/>
                    </Switch>

                </div>

                )

            return login_element;
        }

        let main_app_element = (
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
                    <Route history={history} path='/settingsFactory/:factory_id' component={SettingsFactory} />
                    <Route history={history} path='/settingsTask/:task_id' component={SettingsTask} />
                    <Route history={history} path='/settingsUser/:user_id' component={SettingsUser} />

                    <Route history={history} path='/changeDocument/:document_id' component={ChangeDocument} />
                    <Route history={history} path='/changeFactory/:factory_id' component={ChangeFactory} />
                    <Route history={history} path='/changeTask/:task_id' component={ChangeTask} />
                    <Route history={history} path='/changeUser/:user_id' component={ChangeUser} />

                    {/*<Route history={history} path='/registration' component={Registration} />*/}
                    {/*<Route history={history} path='/auth' component={AuthPage} />*/}

                    <Redirect from='/' to='/home'/>
                </Switch>
            </div>
        );

        return main_app_element
    }
}

export default withRouter(App);
