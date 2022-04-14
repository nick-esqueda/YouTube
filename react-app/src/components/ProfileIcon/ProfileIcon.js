import React from 'react'
import { useHistory } from 'react-router-dom';

import './ProfileIcon.css';
import defaultPfp from '../../static/default-profile-image.png';

export default function ProfileIcon({ channel }) {
    const history = useHistory();
    return (
        <div
            className='profile-icon-border'
            onClick={(e) => {
                window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
                history.push(`/channels/${channel.id}/home`);
            }}
        >
            <img
                className='profile-icon'
                src={channel?.profileImageUrl?.startsWith('https') ? channel.profileImageUrl : defaultPfp}
                alt="profile-icon"
            />
        </div>
    )
}
