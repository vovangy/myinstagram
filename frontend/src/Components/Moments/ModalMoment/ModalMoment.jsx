import { useState, useEffect } from 'react'
import './ModalMoment.css'

const ModalMoment = (props) => {
    const [comments, setComments] = useState([])

    const closeModalMomentHandler = () => {
        props.close(false)
    }

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/commentsbymoment/` + props.data.id)
          .then((response) => response.json())
          .then((jsonData) => setComments(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
      }, []);

    return <div className='mymodal'>
    <div className='mymodal-content'>
    <span onClick={closeModalMomentHandler} className="close">&times;</span>
    <div>
    <img className="photo" src={"http://127.0.0.1:8000" + props.data.image_url}/>
    </div>
    <div>
        <div>
            <h2>Описание</h2>
            <p>{props.data.content}</p>
        </div>
        <div>
            <h2>Дата публикации</h2>
            <p>{props.data.pub_date}</p>
        </div>
        <div>
            <h2>Лайки</h2>
        </div>
        <div>
            <h2>Комментарии</h2>
            {comments.map((item, index) => (
                <div>
                <label>USER: ID = {item.user_id}</label>
                <p key={index}> {item.content}</p>
                </div>
        ))}
        </div>
    </div>
    </div>
</div>
}

export default ModalMoment