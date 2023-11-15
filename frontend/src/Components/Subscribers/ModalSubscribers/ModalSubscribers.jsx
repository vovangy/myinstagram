import './ModalSubscribers.css'
import Subscribers from '../Subscriber'

const ModalSubscribers = (props) => {

    const closeModalSubscribersHandler = () => {
        props.close(false)
    }

    return <div className='mymodal'>
    <div className='mymodal-content'>
    <span onClick={closeModalSubscribersHandler} className="close">&times;</span>
        <Subscribers userId={props.userId}/>
    </div>
</div>
}

export default ModalSubscribers