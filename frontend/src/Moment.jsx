import React from 'react';
import axios from 'axios';
import { useState, useEffect } from 'react';


function Moment() {
  var myid = localStorage.getItem('myid');
  const [momentslist, setMoments] = useState([]);
  
  useEffect(() => {
    // Fetch data from the JSON file (or an API) here
    fetch(`${import.meta.env.VITE_API_URL}api/moments/` + myid)
      .then((response) => response.json())
      .then((jsonData) => setMoments(jsonData))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  /*useEffect(()=> {
    console.log(import.meta.env.VITE_API_URL)

    async function fetchData() {
      try {
        fetch(`${import.meta.env.VITE_API_URL}api/moments/` + myid)
        .then((response)) => response.json())
        .then
        const result = await response.json();
        setMoments(result);
        console.log(momentslist);
      } catch (error) {
      console.error('ERRROR');
      }
    
  }
  fetchData();
}, [])*/


  return (
    <div>
      <h1>Hello your id is {myid}</h1>
    <div>
      <h2>Item List</h2>
      <ul>
        {momentslist.map((item, index) => (
          <li key={index}>
            <h3>{item.title}</h3>
            <img src="https://images.velog.io/images/beton/post/28ff75c7-ff14-4419-b135-d75068a994f4/react0admin-logo.png"/><p>{item.content}</p>
            <p>Pubdate: {item.pub_date}</p>
          </li>
        ))}
      </ul>
    </div>
    </div>   
  );
}

export default Moment;