import './NewMomentForm.css'
import { useState } from 'react'
import axios from 'axios'

const NewMomentForm = () => {
    const [title, setTitle] = useState()
    const [content, setContent] = useState()
    const [photo, setPhoto] = useState()

    const titleHandler = (event) => {
        setTitle(event.target.value)
    }
    const contentHandler = (event) => {
        setContent(event.target.value)
    }
    const photoHandler = (event) => {
        setPhoto(event.target.files[0])
    }

    const submitHandler = async (event) =>{
        let data = {
            title: title,
            content: content,
            image_url: photo,
            user_id: localStorage.getItem("user_id"),
        }
        const response = await axios.post("http://127.0.0.1:8000/api/moments/post/", data, {headers: {"Content-Type": "multipart/form-data"}});
        window.location.reload();
    }

    return <div> 
        <form onSubmit={submitHandler}>
        <div className='myform'>
            <label>Title</label>
            <input type="text" onChange={titleHandler}></input>
        </div>
        <div className='myform'>
            <label>Content</label>
            <input type="text" onChange={contentHandler}></input>
        </div>
        <div className='myform'>
            <label>Img</label>
            <input type="file" onChange={photoHandler}></input>
        </div>
        <button type='submit'>Опубликовать</button>
        </form>
        </div>
}

export default NewMomentForm