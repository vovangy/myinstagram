import './App.css';
import React from 'react';
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from 'react';
import axios from 'axios';


const Login = () => {
  const navigate = useNavigate();
  const [inputEmail, setEmail] = useState('');
  const [inputPassword, setPassword] = useState('');
  var token;

  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(import.meta.env.VITE_API_URL + 'api/auth/token/login', formData);
      token = response.data['auth_token']
      console.log('API Response:', response.data['auth_token']);
      const config = {
        headers: { 'Authorization': 'Token ' + token }
      };

const headers = {
  'Authorization': `Token ${token}`,
};
console.log(headers)
      const loginresponse = await axios.get(import.meta.env.VITE_API_URL + 'api/auth/users/me', {headers: headers,});
      localStorage.setItem('myid', JSON.stringify(loginresponse['data']['id']));
//      localStorage.getItem('data');

      navigate("/Moment");
    } catch (error) {
      console.error('API Error:', error);
    }
    console.log('Submitting form with data:', formData);
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="text"
            id="email"
            name="email"
            value={formData.username}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
}

export default Login
