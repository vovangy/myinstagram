import React from 'react';
import { useState, useEffect } from 'react';

const Moments = (props) => {
    
    const [id, setId] = useState(props.userId)
    const [momentslist, setMoments] = useState([]);
  
  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}api/moments/` + props.userId)
      .then((response) => response.json())
      .then((jsonData) => setMoments(jsonData))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h2>Item List</h2>
      <ul>
        {momentslist.map((item, index) => (
          <li key={index}>
            <h3>{item.title}</h3>
            <p>{item.content}</p>
            <p>Pubdate: {item.pub_date}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Moments