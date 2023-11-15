import React from 'react';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../Login/LoginForm.css';
import './RegistrationForm.css';

const RegistrationForm = () => {
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const navigate = useNavigate();

    const loginButtonHandler = (event) => {
        navigate('/');
      }

    const changeEmailHandler = (event) => {
        setEmail(event.target.value);
    }

    const changeUsernameHandler = (event) => {
        setUsername(event.target.value);
    }

    const changePasswordHandler = (event) => {
        setPassword(event.target.value);
    }

    const loginSubmitHandler = async (event) => {
        event.preventDefault();
        try {
            let data = {
                email: email,
                username: username,
                password: password
            } // Штучка все в массивчик -> ;)
            const response = await axios.post("http://127.0.0.1:8000/api/auth/users/", data);
            navigate("/");
        } catch (error) {
            console.log(error)
            console.log('Loshara');
        }
    }

    return (<div className='wrapper d-flex align-items-center justify-content-center w-100' ><div className='login'><div className='form-group' >
        <h2 className='loginTittle registrationTitle'>Регистрация</h2>
        <form className='mb-3   ' onSubmit={loginSubmitHandler}>
            <div className='mb-2'>
            <label className='form-label'>Email</label>
            <input className='form-control' placeholder='Введите email' onChange={changeEmailHandler}></input>
            </div>
            <div className='mb-2'>
            <label className='form-label'>Username</label>
            <input className='form-control' placeholder='Введите никнейм' onChange={changeUsernameHandler}></input>
            </div>
            <div className='mb-2'>
            <label className='form-label'>Password</label>
            <input className='form-control' placeholder='Введите пароль' type="password" onChange={changePasswordHandler}></input>
            </div>
            <button className='border btn w-100 mt-2' type="submit">Зарегистрироваться</button>
            <button className='border btn w-100 mt-2' onClick={loginButtonHandler}>Войти</button>
        </form>
        </div>
        </div>
    </div>);
}

export default RegistrationForm