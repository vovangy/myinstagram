import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Moments from '../../Components/Moments/Moments'
import { useEffect } from 'react';
import NavigationBar from '../../Components/NavigationBar/NavigationBar';
import './Profile.css'

const Profile = () => {

    const [id, setId] = useState(localStorage.getItem('user_id'));
    const [username, setUsername] = useState(localStorage.getItem('username'));

    const navigate = useNavigate();

    const logoutButtonHandler = (event) => {
        localStorage.removeItem('user_id');
        localStorage.removeItem('username');
        localStorage.removeItem('token');
        navigate("/")
    }
           
    return (<div>
        <NavigationBar />
        <div className='profile'>
        <h1>Это я</h1>
        <h2>Я {username} и мой айди {id}</h2>
        <button className='border btn w-100 mt-2' onClick={logoutButtonHandler}>Выйти</button>
        <Moments userId={id}/>
        </div>
    </div>)
}

export default Profile