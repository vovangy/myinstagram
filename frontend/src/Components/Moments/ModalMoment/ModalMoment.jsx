import { useState, useEffect } from 'react'
import './ModalMoment.css'
import axios from 'axios'
import UserBadge from '../../UserBadge/UserBagde'

const ModalMoment = (props) => {
    const [comments, setComments] = useState([])
    const [isLiked, setLiked] = useState(false)
    const [comment, setComment] = useState("")
    const [likesCount, setLikesCount] = useState(0)

    const [def, setDef] = useState(0)
    const closeModalMomentHandler = () => {
        props.close(false)
    }

    const commentHandler = (e) => {
        setComment(e.target.value);
    }

    const commentSendHandler = async (e) => {
        let data = {
            content: comment,
            user_id: localStorage.getItem("user_id"),
            moment_id: props.data.id
        }
        const response = await axios.post("http://127.0.0.1:8000/api/comments/post/", data);
        setDef(def + 1)
        console.log(response)
    }

    const likeChangeHandler = async (e) => {
        let data = {
            user_id: localStorage.getItem("user_id"),
            moment_id: props.data.id
        }
        const response = await axios.post("http://127.0.0.1:8000/api/likeonmoments/post/", data);
        setLiked(!isLiked)
    }

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/likeonmoments/count/` + props.data.id)
          .then((response) => response.json())
          .then((jsonData) => {setLikesCount(jsonData)})
          .catch((error) => console.error('Error fetching data:', error));
      }, [isLiked]);

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/likeonmoments/` + localStorage.getItem("user_id") + "/" + props.data.id)
          .then((response) => response.json())
          .then((jsonData) => {setLiked(jsonData);          console.log(jsonData)
          })
          .catch((error) => console.error('Error fetching data:', error));
      }, []);

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/commentsbymoment/` + props.data.id)
          .then((response) => response.json())
          .then((jsonData) => setComments(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
      }, [isLiked]);

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/commentsbymoment/` + props.data.id)
          .then((response) => response.json())
          .then((jsonData) => setComments(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
      }, [def]);

    return <div className='mymodal'>
    <div className='mymodal-content'>
    <span onClick={closeModalMomentHandler} className="close">&times;</span>
    <div className="parentDiv">
  <div className="leftDiv">
    <img className="momentImg" src={(props.data.image_url[0] != 'h' ? "http://127.0.0.1:8000" : "") + props.data.image_url}/>
    </div>
    <div className="rightDiv">
    <div className="postContainer">
        <div>            <div className='badge'><UserBadge nickName={props.databadge.username} id={props.databadge.user_id} avatarUrl={props.databadge.photo} close={closeModalMomentHandler}/></div>
</div>
  <div className="postContent">
    <p className="description">
    {props.data.content}    
    </p>
    <div className="interactions">
    <div className="likeSection">
        {!isLiked && <button className="likeOffButton" onClick={likeChangeHandler}>Like</button>}
        {isLiked && <button className="likeOnButton" onClick={likeChangeHandler}>Like</button>}

        <span className="likeCount">{likesCount} Likes</span>
      </div>
      <span className="publishDate">{props.data.pub_date}</span>
    </div>
  </div>
  <div className="commentsContainer">
    <div className="comments">
    {console.log(comments)}
    {comments.map((item, index) => (
                <div className="comment">
                <label>USER: ID = {item.user_id}</label>
                <p key={index}> {item.content}</p>
                </div>
        ))}
    </div>
    <div className="addComment">
      <input type="text" onChange={commentHandler} placeholder="Добавить комментарий" class="commentInput"/>
      <button className="commentButton" onClick={commentSendHandler}>Отправить</button>
    </div>
  </div>
</div>
    </div>
    </div>
    </div>
</div>
}

export default ModalMoment