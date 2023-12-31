import React from 'react'

import './SearchHeader.css';
import searchIcon from '../../static/icons/search.png';

export default function SearchHeader() {

    const onSubmit = e => {
        e.preventDefault();
    }

    return (
        <div className='search full-size'>
            <form className="header__search row-space-between full-size" onSubmit={onSubmit}>
                <input type="text" placeholder="Search"
                    className=""
                />

                <button type='submit' className='search-submit-button'>
                    <img src={searchIcon} alt='search-icon' className='svg' style={{ width: '24px', height: '24px' }} />
                </button>
            </form>
        </div>
    )
}
