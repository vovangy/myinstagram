import './ModalSubscriptions.css'
import Subscriptions from '../Subscriptions'

const ModalSubscriptions = (props) => {

    const closeModalSubscriptionsHandler = () => {
        props.close(false)
    }

    return <div className='mymodal'>
    <div className='mymodal-content'>
    <span onClick={closeModalSubscriptionsHandler} className="close">&times;</span>
        <Subscriptions userId={props.userId} close={closeModalSubscriptionsHandler}/>
    </div>
</div>
}

export default ModalSubscriptions