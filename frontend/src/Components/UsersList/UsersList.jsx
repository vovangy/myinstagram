import React from 'react';
import UserBadge from '../UserBadge/UserBagde';
import "./UsersList.css"

const UserList = ({ users, close }) => {
  return (
    <div className="userList">
      <div className="userListContainer">
        {users.map(user => (
            < UserBadge nickName={user.username} avatarUrl={user.image_url} id={user.id} close={close}/>
        ))}
      </div>
    </div>
  );
};

export default UserList;
