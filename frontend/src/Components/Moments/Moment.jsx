import { useState } from 'react'
import ModalMoment from './ModalMoment/ModalMoment'
import { Modal } from 'react-bootstrap'
import './Moment.css'
import { useEffect } from 'react'

const Moment = (props) => {
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
          console.log("Props")
          console.log(props)
      }, []);

    return <div>
    {open && <ModalMoment data={props.data} databadge={{username:username, user_id:props.data.user_id, photo:photo}} close={setOpen}/>}
        <div className="myexmpl mywrapper filler moment" key={props.index}>
    <img className="photo" onClick={() => {setOpen(true);console.log(open)}} src={"http://127.0.0.1:8000" + props.data.image_url}/>
  </div>
  </div>
}

export default Moment