import { useState, useEffect } from 'react';
import Moments from '../../Components/Moments/Moments';
import { useNavigate } from 'react-router-dom';
import NavigationBar from '../../Components/NavigationBar/NavigationBar';
import './feed.css'
import FeedMoments from '../../Components/FeedMoments/FeedMoments';


const Feed = () => {

    const [id, setId] = useState(localStorage.getItem('user_id'));
    const [momentslist, setMoments] = useState([]);

    const [page, setPage] = useState(0);
    const count = 5
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const handleScroll = () => {
          if (
            window.innerHeight + document.documentElement.scrollTop !==
            document.documentElement.offsetHeight
          )
            return;
          setLoading(true);
        };
        window.addEventListener("scroll", handleScroll);
        return () => window.removeEventListener("scroll", handleScroll);
      }, []);

    const getData = () => {
      try{
        setLoading(true)
        const resp_moments = fetch(`http://127.0.0.1:8000/api/moments/feed/${id}/?feed=true&offset=${page}&count=${count}`)
            .then((response) => response.json())
            .then((jsonData) => {

                if (!jsonData.count) return setLoading(true);
                console.log(jsonData)

                setMoments(momentslist.concat(jsonData.results))
                setPage(page + count);
                console.log(momentslist)
                setLoading(false);}
                )

            
      }catch(error){
          console.log(error)
      }
    }
    
      useEffect(() => {
        if (!loading) return;
        if (!momentslist.length){
          getData()
          return
        }
        setTimeout(() => {
             getData()
        }, 500);
      }, [loading]);

    return (<div>
        <NavigationBar />
        <div className='feed bodypage'>
        <h1>Эти моменты</h1>
            <FeedMoments photos={momentslist}/>
        </div>
    </div>)
}

export default Feed