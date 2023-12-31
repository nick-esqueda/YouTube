import React from 'react'

import './Navbar.css';
import home from '../../static/icons/home.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub, faLinkedin } from '@fortawesome/free-brands-svg-icons';
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
            {/* <Link to={`/`}>
                <div className='svg-wrapper disabled'>
                    <img src={explore} alt='apps-menu' className='svg' />
                    Explore
                </div>
            </Link> */}
            {/* <Link to={`/`}>
                <div className='svg-wrapper disabled'>
                    <img src={subscriptions} alt='bell-icon' className='svg' />
                    Subscriptions
                </div>
            </Link> */}
            {/* <Link to={`/`}>
                <div className='svg-wrapper disabled'>
                    <img src={library} alt='bell-icon' className='svg' />
                    Library
                </div>
            </Link> */}
            <a href='https://github.com/nick-esqueda/YouTube' target="_blank" rel="noreferrer">
                <FontAwesomeIcon icon={faGithub} className='link-logo' style={{ fontSize: '24px', color: 'var(--gray-light)', marginBottom: '6px' }} />
                GitHub
            </a>
            <a href='https://www.linkedin.com/in/nick-esqueda/' target="_blank" rel="noreferrer">
                <FontAwesomeIcon icon={faLinkedin} className='link-logo' style={{ fontSize: '24px', color: 'var(--gray-light)', marginBottom: '6px' }} />
                LinkedIn
            </a>
        </nav>
    )
}
