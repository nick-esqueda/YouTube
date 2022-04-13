import React from 'react'

import './SearchHeader';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

export default function SearchHeader() {
    
    const onSubmit = e => {
        e.preventDefault();
        console.log('search submission');
    }
    
    return (
        <div className='search'>
            <form className="header__search" onSubmit={onSubmit}>
                <input type="text" placeholder="search"
                    className=""
                />
                <FontAwesomeIcon icon={faSearch} style={{ color: 'var(--color-dark-gray)' }} />
            </form>
        </div>
    )
}
