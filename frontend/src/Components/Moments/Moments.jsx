import React from 'react';
import { useState, useEffect } from 'react';
import Moment from './Moment';
import './Moments.css'
import { Modal } from 'react-bootstrap';

const Moments = (props) => {
  return (
    <div>
    <h2>Моменты</h2>
    {console.log(props)}
    <div className='flex-box'>
        {props.data.map((item, index) => (
          <Moment data={item} key={index}/>
        ))}
    </div>
    </div>
  );
}

export default Moments