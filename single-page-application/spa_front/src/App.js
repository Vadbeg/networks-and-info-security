import React from 'react';
import ReactDOM from 'react-dom';

class DateShower extends React.Component {
    constructor(props) {
        super(props);

        this.state = {'country': 'Belarus'}
    }

    changeCountry = () => {
        this.setState({country: 'US'});
    }

    render() {
        var today = new Date();
        const myfirstelement = (
        <div>
            <h1>Hello React, motherfucker {String(today.getDate())}!</h1>
            <h2>{this.props.color}</h2>
            <h2>Your country is {this.state.country}</h2>

            <button type='button' onClick={this.changeCountry}>
                Change country
            </button>
        </div>
        );

        return myfirstelement
    }
}



export default DateShower;
