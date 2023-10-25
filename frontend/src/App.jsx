import './App.css';
import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

const client = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`
});

function App() {
  const [inputEmail, setEmail] = useState('');
  const [inputPassword, setPassword] = useState('');

  function loggedIn() {
    var response = client.post(
      "/jwt/create",
      {
        email: inputEmail,
        password: inputPassword
      }
    )
    console.log(response)
  }

  useEffect(()=> {
    console.log(import.meta.env.VITE_API_URL)

    async function fetchData() {
      console.log(import.meta.env.VITE_API_URL)
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}api/moments`);
        const result = await response.json();
        var a = result[0]
        console.log(a)
      } catch (error) {
      console.error('ERRROR');
      }
    
  }
  fetchData();

  }, [])

  return (
    <div id="block">
    
    </div>
  );
}

export default App
