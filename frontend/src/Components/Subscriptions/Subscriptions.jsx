import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Subscriptions = (props) => {

    const   [subscriptions, setSubscriptions] = useState([])
    const navigate = useNavigate();

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/subscriptions/user/` + props.userId)
          .then((response) => response.json())
          .then((jsonData) => setSubscriptions(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
      }, []);

    return <div>
    <h2>Subscription List</h2>
      <ul>
        {subscriptions.map((item, index) => (
          <div onClick={() => {
            localStorage.setItem("profile_id", item.id);
            window.location.reload();
          }} key={index}>
            
            <h3>{item.id}</h3>
            <p>{item.username}</p>
          </div>
        ))}
      </ul> 
    </div>
}

export default Subscriptions