import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import UserList from "../UsersList/UsersList";
import "./Subscriptions.css"

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
      <UserList users={subscriptions} close={props.close} />
    </div>
}

export default Subscriptions