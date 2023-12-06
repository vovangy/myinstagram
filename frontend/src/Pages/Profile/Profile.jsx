import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Moments from '../../Components/Moments/Moments'
import { useEffect } from 'react';
import NavigationBar from '../../Components/NavigationBar/NavigationBar';
import './Profile.css'
import ModalSubscribers from '../../Components/Subscribers/ModalSubscribers/ModalSubscribers';
import ModalSubscriptions from '../../Components/Subscriptions/ModalSubscriptions/ModalSubscriptions';
import ModalNewMoment from '../../Components/Moments/ModalNewMoment/ModalNewMoment';

const Profile = () => {

    const [id, setId] = useState(localStorage.getItem('user_id'));
    const [username, setUsername] = useState(localStorage.getItem('username'));
    const [idProfile, setIdProflie] = useState(localStorage.getItem('profile_id'));
    const [_id, set_id] = useState(idProfile ? id : idProfile);

    const [profilePhoto, setProfilePhoto] = useState('');
    const [subscribersModalOpen, setSubscribersModalOpen] = useState(false)
    const [subscriptionModalOpen, setSubscriptionModalOpen] = useState(false)
    const [newMomentModalOpen, setNewMomentModalOpen] = useState(false)
    const [momentslist, setMoments] = useState([]);

    useEffect(() => {
        const fetchImageData = async () => {
          if (!profilePhoto) {
            try {
              const response = await axios.get("http://127.0.0.1:8000/api/users/photo/" + _id);
              console.log(response.data);
              setProfilePhoto(response.data[0]["image_url"]);
            } catch (error) {
              console.error('Error fetching image data:', error);
            }
          }
    };
        fetchImageData(); // Call fetchImageData when imageURL changes
  }, [profilePhoto]);


    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/moments/` + _id)
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

    const newMomentButtonHandler = () => {
        setNewMomentModalOpen(true)
    }

    return (<div>
        <NavigationBar />
        <div className="bodypage">
        <div className='profile'>
        <h2>Я {username} и мой айди {_id}</h2>
        <div className='profileHead'>
            <div className='profilePhoto'>
            {profilePhoto && <img className="photop" src={"http://127.0.0.1:8000/media/" + profilePhoto} />}
            {!profilePhoto && <img className="photop" src={"http://127.0.0.1:8000/media/images/base.jpeg"} />}
            </div>
        </div>
        <div className='button-container'>
        <button onClick={subscribersButtonHadler}>Мои подписчики</button>
        <button onClick={subscriptionsButtonHadler}>Мои подписки</button>
        <button onClick={newMomentButtonHandler}>Добавить момент</button>
        </div>
        <Moments data={momentslist}/>
        {subscriptionModalOpen && <ModalSubscriptions userId={_id} close={setSubscriptionModalOpen}/>}
        {subscribersModalOpen && <ModalSubscribers userId={_id} close={setSubscribersModalOpen}/>}
        {newMomentModalOpen && <ModalNewMoment userId={_id} close={setNewMomentModalOpen}/>}
        </div>
        </div>
    </div>)
}

export default Profile