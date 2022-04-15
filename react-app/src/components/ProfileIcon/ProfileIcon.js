import React, { useEffect, useState } from 'react'
import { Link, useHistory } from 'react-router-dom';

import './ProfileIcon.css';
import defaultPfp from '../../static/default-profile-image.png';
import channelIcon from '../../static/icons/channel.png';
import logoutIcon from '../../static/icons/logout.png';
import settingsIcon from '../../static/icons/settings.png';
import { useDispatch } from 'react-redux';
import { logout } from '../../store/session';

export default function ProfileIcon({ channel, isNav }) {
    const history = useHistory();
    const dispatch = useDispatch();
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
    
    const linkToSettings = () => {
        window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
        history.push(`/channels/${channel.id}/settings`);
    }

    const logoutUser = (e) => {
        setShowMenu(false);
        if (window.confirm('Are you sure you want to log out?')) {
            dispatch(logout());
            window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
            history.push('/login');
        }
    };

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
                            <div className='svg-wrapper'>
                                <img src={channelIcon} alt="channel" className='svg' />
                            </div>
                            Your Channel
                        </div>
                        <div onClick={linkToSettings}>
                            <div className='svg-wrapper'>
                                <img src={settingsIcon} alt="settings" className='svg' />
                            </div>
                            Customize Channel
                        </div>
                        <div onClick={logoutUser}>
                            <div className='svg-wrapper'>
                                <img src={logoutIcon} alt="logout" className='svg' />
                            </div>
                            Sign Out
                        </div>
                    </div>
                </div>
            )}
        </div>

    )
}
