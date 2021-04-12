import React from 'react';
import {
    Link
} from 'react-router-dom'


const SECTIONS = [
    {title: 'Documents', href: '/documentsTable'},
]


class Home extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'sections': SECTIONS
        }
    }

    render() {
        const { sections } = this.state

        let all_links = []

        for (let i=0; i < sections.length; i++){
            let curr_section = SECTIONS[i]

            all_links.push(
                <Link className='button-link' to={curr_section['href']}>
                    {curr_section['title']}
                </Link>
            )
        }

        let myfirstelement = (
            <div>
                <Link className='button-link' to={'/documentsTable'}>
                    Documents
                </Link>
            </div>
        );

        console.log('WTF')

        return myfirstelement
    }
}


export default Home;
