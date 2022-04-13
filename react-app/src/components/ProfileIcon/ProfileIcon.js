import React from 'react'

import n from '../../static/default-pfps/A.png';
import './ProfileIcon.css';

export default function ProfileIcon() {
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
                src={n}
                alt="profile preview"
            />
        </div>
    )
}
