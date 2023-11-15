import { useState, useEffect } from 'react';
import Moments from '../../Components/Moments/Moments';
import { useNavigate } from 'react-router-dom';
import NavigationBar from '../../Components/NavigationBar/NavigationBar';
import './feed.css'


const Feed = () => {

    const [id, setId] = useState(localStorage.getItem('user_id'));
    const [momentslist, setMoments] = useState([]);

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/subscription/moments/` + id)
          .then((response) => response.json())
          .then((jsonData) => setMoments(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
      }, []);

    return (<div>
        <NavigationBar />
        <div className='feed bodypage'>
            <h1>Эти моменты</h1>
            <Moments data={momentslist}/>
        </div>
    </div>)
}

export default Feed