import React, { useEffect, useState } from 'react'
import { Link, useHistory } from 'react-router-dom';

import './ProfileIcon.css';
import defaultPfp from '../../static/default-profile-image.png';

export default function ProfileIcon({ channel, isNav }) {
    const history = useHistory();
    const [showMenu, setShowMenu] = useState(false);

    useEffect(() => {
        if (!showMenu) return;

        const closeMenu = () => {
            setShowMenu(false);
        };

        document.addEventListener('click', closeMenu);

        return () => {
            setShowMenu(false);
            document.removeEventListener("click", closeMenu);
        }
    }, [showMenu]);

    const openMenu = () => {
        if (showMenu) return;
        setShowMenu(true);
    };

    const linkToProfile = () => {
        window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
        history.push(`/channels/${channel.id}/home`);
    }

    return (
        <div
            className='profile-icon-border'
            onClick={isNav ? openMenu : linkToProfile}
        >
            <img
                className='profile-icon'
                src={channel?.profileImageUrl?.startsWith('https') ? channel.profileImageUrl : defaultPfp}
                alt="profile-icon"
            />

            {showMenu && (
                <div id="profile_nav_dropdown">
                    <div className='row-top row-left dropdown-header'>
                        <div
                            className='pfp-wrapper-nav'
                            style={{ minWidth: '40px', minHeight: '40px', margin: '0 16px 0 0', }}
                        >
                            <img
                                className='profile-icon'
                                src={channel?.profileImageUrl?.startsWith('https') ? channel.profileImageUrl : defaultPfp}
                                alt="profile-icon"
                            />
                        </div>

                        <div className="left-align col-left" style={{ height: '100%', justifyContent: 'space-between', fontWeight: '500' }}>
                            {channel.channelName}
                            <a href='https://www.linkedin.com/in/nick-esqueda/' className='link'>Looking for help?</a>
                        </div>
                    </div>


                    <div className='dropdown-section'>
                        <div onClick={linkToProfile}>
                            Your Channel
                        </div>
                        <div>
                            <Link to={`/users/settings`} onClick={() => window.scrollTo(0, 0)} style={{ width: '100%' }}>
                                Channel Appearance
                            </Link>
                        </div>
                        <div>
                            Sign Out
                        </div>
                    </div>
                </div>
            )}
        </div>

    )
}
