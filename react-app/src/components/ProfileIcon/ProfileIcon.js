import React from 'react'

import './ProfileIcon.css';

export default function ProfileIcon({ channel }) {
    return (
        <div
            className='profile-icon-border'
            // onClick={(e) => {
            //     window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
            //     // TODO: redirect to channel here
            // }}
        >
            <img
                className='profile-icon'
                src={channel.profileImageUrl}
                alt="profile icon"
            />
        </div>
    )
}
