import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import { customFetch } from '../utils';

function UsersList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await customFetch(`/api/channels/`);
      const responseData = await response.json();
      setUsers(responseData.channels);
    }
    fetchData();
  }, []);

  const userComponents = users.map((user) => {
    return (
      <li key={user.id}>
        <NavLink to={`/channels/${user.id}/videos`}>{user.channelName}</NavLink>
      </li>
    );
  });

  return (
    <>
      <h1>User List: </h1>
      <ul>{userComponents}</ul>
    </>
  );
}

export default UsersList;
