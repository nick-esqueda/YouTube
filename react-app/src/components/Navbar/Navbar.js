import React from 'react'

import './Navbar.css';
import home from '../../static/icons/home.png';
import explore from '../../static/icons/explore.png';
import subscriptions from '../../static/icons/subscriptions.png';
import library from '../../static/icons/library.png';
import { Link } from 'react-router-dom';

export default function Navbar() {
    return (
        <nav id="nav">
            <Link to={`/`}>
                <div className='svg-wrapper'>
                    <img src={home} alt='bell-icon' className='svg' />
                    Home
                </div>
            </Link>
            <Link to={`/`}>
                <div className='svg-wrapper disabled'>
                    <img src={explore} alt='apps-menu' className='svg' />
                    Explore
                </div>
            </Link>
            <Link to={`/`}>
                <div className='svg-wrapper disabled'>
                    <img src={subscriptions} alt='bell-icon' className='svg' />
                    Subscriptions
                </div>
            </Link>
            <Link to={`/`}>
                <div className='svg-wrapper disabled'>
                    <img src={library} alt='bell-icon' className='svg' />
                    Library
                </div>
            </Link>
        </nav>
    )
}
