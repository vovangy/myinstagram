import { useState, useEffect } from "react";
import UserList from "../UsersList/UsersList";

const Subscribers = (props) => {

    const   [subscribers, setSubscribers] = useState([])

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/subscribers/` + props.userId)
          .then((response) => response.json())
          .then((jsonData) => setSubscribers(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
      }, []);

    return <div>
      <h2>Subscribers List</h2>
      <UserList users={subscribers} close={props.close}/>
    </div>
}

export default Subscribers