import { useState, useEffect } from "react";

const Subscribers = (props) => {

    const   [subscribers, setSubscribers] = useState([])

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/subscribers/` + props.userId)
          .then((response) => response.json())
          .then((jsonData) => setSubscribers(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
      }, []);

    return <div>
    <h2>Subscriber List</h2>
      <ul>
        {subscribers.map((item, index) => (
          <li key={index}>
            <h3>{item.id}</h3>
            <p>{item.username}</p>
          </li>
        ))}
      </ul> 
    </div>
}

export default Subscribers