import './ModalNewMoment.css'
import NewMomentForm from '../NewMomentForm/NewMomentForm'

const ModalNewMoment = (props) => {

    const closeModalNewMoment = () => {
        props.close(false)
    }

    return <div className='mymodal'>
    <div className='mymodal-content'>
    <span onClick={closeModalNewMoment} className="close">&times;</span>
          <NewMomentForm />  
    </div>
</div>
}

export default ModalNewMoment