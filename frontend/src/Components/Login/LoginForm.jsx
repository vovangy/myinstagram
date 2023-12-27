import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './LoginForm.css';


const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const registrationButtonHandler = (event) => {
      navigate('/registration');
    }

    const changeEmailHandler = (event) => {
        setEmail(event.target.value);
    }

    const changePasswordHandler = (event) => {
        setPassword(event.target.value);
    }

    const loginSubmitHandler = async (event) => {
        event.preventDefault();
        try {
            let data = {
                email: email,
                password: password
            } // Штучка все в массивчик -> ;)
            console.log(data);
            const response = await axios.post("http://127.0.0.1:8000/api/auth/token/login", data);
            const token = response.data['auth_token']
            console.log('API Response:', response.data['auth_token']);
              //console.log(response2)
              const headers = {
                         'Authorization': `Token ${token}`,
                 };
                 console.log(headers);
            const response2 = await axios.get("http://127.0.0.1:8000/api/auth/users/me", {headers: headers,});
            console.log(response2);
            localStorage.setItem('token', JSON.stringify(token));
            localStorage.setItem('user_id', JSON.stringify(response2.data.id));
            localStorage.setItem('profile_id', JSON.stringify(response2.data.id));
            localStorage.setItem('username', JSON.stringify(response2.data.username));
              //localStorage.setItem('token', JSON.stringify(token));
              //localStorage.getItem('data');
    //          const headers = {
   //             'Authorization': `Token ${token}`,
 //             };
///            const response2 = await axios.get("http://127.0.0.1:8000/api/auth/users/me", {headers: headers,});
            navigate("/feed");

            //const config = {
            //  headers: { 'Authorization': 'Token ' + token }
        } catch {
            console.log('Loshara');
        }
    }

    return (<div className='wrapper d-flex align-items-center justify-content-center w-100'><div className='login'><div className='form-group' >
        <h1 className='loginTitle'>MyInstagram</h1>
        <form className='mb-3' onSubmit={loginSubmitHandler}>
            <div className='mb-2'>
            <label className='form-label'>Email</label>
            <input className='form-control' placeholder="Введите email" type="email" onChange={changeEmailHandler}></input>
            </div>
            <div className='mb-2' >
            <label className='form-label'>Password</label>
            <input className='form-control' placeholder="Введите пароль" type="password" onChange={changePasswordHandler}></input>
            </div>
            <button className='border btn w-100 mt-2'
            type="submit">Войти</button>
            <button className='border btn w-100 mt-2' onClick={registrationButtonHandler}>Зарегистрироваться</button>
        </form>
        </div>
        </div>
    </div>);
}

export default LoginForm