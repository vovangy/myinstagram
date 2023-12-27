import React, { useState } from 'react';
import axios from 'axios'; 
import NavigationBar from '../NavigationBar/NavigationBar';
import UserList from '../UsersList/UsersList';
import { useEffect } from 'react';
import "./SearchProfiles.css";

const SearchProfiles = () => {

    const [username, setUsername] = useState('');
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/users/search/?username=${username}`)
          .then((response) => response.json())
          .then((jsonData) => setUsers(jsonData.results))
          .catch((error) => console.error('Error fetching data:', error));
      }, [username]);

    const functionA = () => {

    };

    return (
        <div>
            <NavigationBar />
        <div className="bodypage">
            <div>
            <input
                type="text"
                placeholder="Search by username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
            />
            <div className='searchList'>
                <UserList users={users} close={functionA}/>
            </div>
            </div>
        </div>
        </div>
    );
}


export default SearchProfiles