import React from 'react';
import "./FeedMoments.css"
import FeedMoment from './FeedMoment';

const FeedMoments = ({ photos }) => {
  return (
    <div className="photo-gallery">
      {photos.map((photo, index) => (
        
                      <FeedMoment data={photo} key={index}/>
      ))}
    </div>
  );
};

export default FeedMoments;