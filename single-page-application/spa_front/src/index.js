import React from 'react';
import ReactDOM from 'react-dom';
import DateShower from "./App";
import Form from "./Form";

function Text() {
    return <h1>Some bullshit!</h1>
}


ReactDOM.render(<DateShower color='red'/>, document.getElementById('root'));
ReactDOM.render(<Text />, document.getElementById('value'));
ReactDOM.render(<Form />, document.getElementById('custom-form'));
