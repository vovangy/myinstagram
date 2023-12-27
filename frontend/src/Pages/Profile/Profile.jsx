import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Moments from '../../Components/Moments/Moments'
import { useEffect } from 'react';
import NavigationBar from '../../Components/NavigationBar/NavigationBar';
import './Profile.css'
import ModalSubscribers from '../../Components/Subscribers/ModalSubscribers/ModalSubscribers';
import ModalSubscriptions from '../../Components/Subscriptions/ModalSubscriptions/ModalSubscriptions';
import ModalNewMoment from '../../Components/Moments/ModalNewMoment/ModalNewMoment';
import e from 'cors';

const Profile = (props) => {

    const { id } = useParams();
    const [username, setUsername] = useState(localStorage.getItem('username'));
    const user_id = localStorage.getItem('user_id');

    const [profilePhoto, setProfilePhoto] = useState('');
    const [subscribersModalOpen, setSubscribersModalOpen] = useState(false)
    const [subscriptionModalOpen, setSubscriptionModalOpen] = useState(false)
    const [newMomentModalOpen, setNewMomentModalOpen] = useState(false)
    const [momentslist, setMoments] = useState([]);
    const [isSubscribed, setIsSubscribed] = useState(false)

    const navigate = useNavigate();

    useEffect(() => {
        const fetchImageData = async () => {
            try {
              const response = await axios.get("http://127.0.0.1:8000/api/users/photo/" + id);
              console.log(response.data);
              setProfilePhoto(response.data[0]["image_url"]);
              setUsername(response.data[0]["username"]);
            } catch (error) {
              console.error('Error fetching image data:', error);
            }
    };
        const subscribeData = async () => {
          const response = await axios.get("http://127.0.0.1:8000/api/subscriptions/" + id + "/" + user_id);
          setIsSubscribed(response.data)
        }
        if (id != user_id)
          subscribeData();
        fetchImageData();
  }, [profilePhoto, id]);

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/moments/` + id)
          .then((response) => response.json())
          .then((jsonData) => setMoments(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
      }, [id]);

    const subscribersButtonHadler = () => {
        setSubscribersModalOpen(true)
    }

    const subscribeButtonHadler = async () => {
      setIsSubscribed(!isSubscribed)
      let data = {
        user_id: id,
        subscriber_id: user_id
      }
      const response = await axios.post("http://127.0.0.1:8000/api/subscriptions/post/", data);
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
        <div className='profileHead'>
            <div className='profilePhoto'>
            {profilePhoto && <img className="photop" src={"http://127.0.0.1:8000/media/" + profilePhoto} />}
            {!profilePhoto && <img className="photop" src={"http://127.0.0.1:8000/media/images/base.jpeg"} />}
            </div>
            <div className='profileData'>
                <div className='username'>{username}</div>
                <div className='button-container'>
                    <button onClick={subscribersButtonHadler}>Подписчики</button>
                    <button onClick={subscriptionsButtonHadler}>Подписки</button>
                    {user_id == id && <button onClick={newMomentButtonHandler}>Добавить момент</button>}
                    {user_id != id && !isSubscribed && <button onClick={subscribeButtonHadler}>Подписаться</button>}
                    {user_id != id && isSubscribed && <button onClick={subscribeButtonHadler}>Отписаться</button>}
                </div>
            </div>
        </div>
        {momentslist && <Moments data={momentslist}/>}
        {subscriptionModalOpen && <ModalSubscriptions userId={id} close={setSubscriptionModalOpen}/>}
        {subscribersModalOpen && <ModalSubscribers userId={id} close={setSubscribersModalOpen}/>}
        {newMomentModalOpen && <ModalNewMoment userId={id} close={setNewMomentModalOpen}/>}
        </div>
        </div>
    </div>)
}

export default Profile