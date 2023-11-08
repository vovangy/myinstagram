import React from 'react';
import { useNavigate } from 'react-router-dom';
import RegistrationForm from '../../Components/Registration/RegistrationForm'

const Registration = () => {
    const navigate = useNavigate();

    return (<div>
        <RegistrationForm/>
    </div>)
}

export default Registration