import './NewMomentForm.css'
import { useState } from 'react'
import axios from 'axios'
import { useEffect } from 'react'

const NewMomentForm = (props) => {
    const [title, setTitle] = useState()
    const [content, setContent] = useState()
    const [photo, setPhoto] = useState()
    const [allTags, setAllTags] = useState([])

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}api/tags`)
          .then((response) => response.json())
          .then((jsonData) => setAllTags(jsonData))
          .catch((error) => console.error('Error fetching data:', error));
          console.log(allTags)
    }, []);

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
        props.close()
    }

    return <div> 
        <div class="containerAddMoment">
    <h2>Добавление момента</h2>
    <form id="momentForm" onSubmit={submitHandler} enctype="multipart/form-data">
      <div class="form-group">
        <label for="title">Заголовок:</label>
        <input type="text" onChange={titleHandler} id="title" name="title" required/>
      </div>
      <div class="form-group">
        <label for="content">Содержание:</label>
        <textarea id="content" onChange={contentHandler} name="content" rows="4" required></textarea>
      </div>
      <div class="form-group">
      <div class="containerTag">
    <h2>Тэги</h2>
    <div class="buttonTag-container">
      <div class="scrollable-div">
        {allTags.map((tag, index) => (
        <button className='buttonTag'>{tag.title}</button>
        ))}
      </div>
    </div>
  </div>
      </div>
      <div class="form-group">
        <label for="file">Выберите файл:</label>
        <input type="file" id="file" name="file" onChange={photoHandler}/>
      </div>
      <button type="submit">Добавить момент</button>
    </form>
  </div>
        </div>
}

export default NewMomentForm