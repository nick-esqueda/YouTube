import React from 'react'
import { Link } from 'react-router-dom';

import pageNotFound from '../../static/404.png';
import './PageNotFound.css';

export default function PageNotFound() {
    return (
        <div id='not-found-wrapper'>
            <img src={pageNotFound} alt='page-not-found' id='not-found-image' />
            <Link to={'/'} className='btn btn--blue' id='go-back-home'>Go Back Home</Link>
        </div>
    )
}
