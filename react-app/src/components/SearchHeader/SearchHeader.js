import React from 'react'

import './SearchHeader';
import searchIcon from '../../static/icons/search.png';

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
                <img src={searchIcon} alt='search-icon' className='svg' />
            </form>
        </div>
    )
}
