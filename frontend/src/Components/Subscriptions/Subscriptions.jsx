import { useState, useEffect } from "react";

const Subscriptions = (props) => {

    const   [subscriptions, setSubscriptions] = useState([])

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
          <li key={index}>
            <h3>{item.id}</h3>
            <p>{item.username}</p>
          </li>
        ))}
      </ul> 
    </div>
}

export default Subscriptions