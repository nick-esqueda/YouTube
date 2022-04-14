import React from 'react'
import { useHistory } from 'react-router-dom';

import './ProfileIcon.css';

export default function ProfileIcon({ channel }) {
    const history = useHistory();
    return (
        <div
            className='profile-icon-border'
            onClick={(e) => {
                window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
                history.push(`/channels/${channel.id}`);
            }}
        >
            <img
                className='profile-icon'
                src={channel.profileImageUrl}
                alt="profile-icon"
            />
        </div>
    )
}
