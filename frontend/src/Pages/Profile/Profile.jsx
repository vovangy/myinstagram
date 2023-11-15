import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Moments from '../../Components/Moments/Moments'
import { useEffect } from 'react';
import NavigationBar from '../../Components/NavigationBar/NavigationBar';
import './Profile.css'
import Subscribers from '../../Components/Subscribers/Subscriber';
import ModalSubscribers from '../../Components/Subscribers/ModalSubscribers/ModalSubscribers';
import ModalSubscriptions from '../../Components/Subscriptions/ModalSubscriptions/ModalSubscriptions';

const Profile = () => {

    const [id, setId] = useState(localStorage.getItem('user_id'));
    const [username, setUsername] = useState(localStorage.getItem('username'));

    const [subscribersModalOpen, setSubscribersModalOpen] = useState(false)
    const [subscriptionModalOpen, setSubscriptionModalOpen] = useState(false)
    const [momentslist, setMoments] = useState([]);

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/moments/` + id)
          .then((response) => response.json())
          .then((jsonData) => setMoments(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
      }, []);

    const subscribersButtonHadler = () => {
        setSubscribersModalOpen(true)
    }

    const subscriptionsButtonHadler = () => {
        setSubscriptionModalOpen(true)
    }

    return (<div>
        <NavigationBar />
        <div className="bodypage">
        <div className='profile'>
        <h1>Это я</h1>
        <button onClick={subscribersButtonHadler}>Мои подписчики</button>
        <button onClick={subscriptionsButtonHadler}>Мои подписки</button>
        <img href="" />
        <h2>Я {username} и мой айди {id}</h2>
        <Moments data={momentslist}/>
        {subscriptionModalOpen && <ModalSubscriptions userId={id} close={setSubscriptionModalOpen}/>}
        {subscribersModalOpen && <ModalSubscribers userId={id} close={setSubscribersModalOpen}/>}
        </div>
        </div>
    </div>)
}

export default Profile