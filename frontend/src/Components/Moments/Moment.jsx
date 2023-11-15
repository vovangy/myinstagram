import { useState } from 'react'
import ModalMoment from './ModalMoment/ModalMoment'
import { Modal } from 'react-bootstrap'
import './Moment.css'

const Moment = (props) => {
    const [open, setOpen] = useState(false)

    return <div>
    {open && <ModalMoment data={props.data} close={setOpen}/>}
        <div className="filler moment" key={props.index}>
    <h3>{props.data.title}</h3>
    <img onClick={() => {setOpen(true);console.log(open)}} className="photo" src={"http://127.0.0.1:8000" + props.data.image_url}/>
  </div>
  </div>
}

export default Moment