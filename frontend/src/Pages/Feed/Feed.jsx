import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBar from '../../Components/NavigationBar/NavigationBar';
import './feed.css'

const Feed = () => {

    return (<div>
        <NavigationBar />
        <div className='feed'>
            <h1>Эти моменты</h1>
        </div>
    </div>)
}

export default Feed