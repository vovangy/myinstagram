import { useEffect } from 'react'
import { useState } from 'react'
import ModalMoment from '../Moments/ModalMoment/ModalMoment'
import UserBadge from '../UserBadge/UserBagde'
import "./FeedMoment.css"

const FeedMoment = (props) => {
    const [open, setOpen] = useState(false)
    const [photo, setPhoto] = useState("")
    const [username, setUsername] = useState("")

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/users/username/` + props.data.user_id)
          .then((response) => response.json())
          .then((jsonData) => setUsername(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
        fetch(`${import.meta.env.VITE_API_URL}api/users/photo/` + props.data.user_id)
          .then((response) => response.json())
          .then((jsonData) => {console.log(jsonData);setPhoto('/media/' + jsonData[0].image_url)})
          .catch((error) => console.error('Error fetching data:', error));
      }, []);

    return <div>
    {open && <ModalMoment data={props.data} databadge={{username:username, user_id:props.data.user_id, photo:photo}} close={setOpen}/>}
        <div className="photo-item" key={props.index}>
            {console.log(props)}
            <div className='badge'><UserBadge nickName={username} id={props.data.user_id} avatarUrl={photo}/></div>
    <img className="photo-item" onClick={() => {setOpen(true);console.log(open)}} src={props.data.image_url}/>
  </div>
  </div>
}

export default FeedMoment