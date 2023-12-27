import { useNavigate } from 'react-router-dom';
import './UserBadge.css';

const UserBadge = ({
    nickName,
    avatarUrl,
    id,
    close
}) => {
    const navigate = useNavigate();

    const onUserBadgeClick = () => {
        navigate('/profile/'+ id, {username: nickName});
        close();
    };

    return (
        <div className="cnUserBadgeRoot" onClick={onUserBadgeClick}>
            {avatarUrl ? (<img src={(avatarUrl[0] != 'h' ? "http://127.0.0.1:8000" : "") + avatarUrl} alt="logo" className="cnUserBadgeAvatar" />) : <img src="http://127.0.0.1:8000/media/images/base.jpeg" className="cnUserBadgeAvatar"/>}
            <span className="cnUserBadgeName">{nickName}</span>
        </div>
    );
};

export default UserBadge;