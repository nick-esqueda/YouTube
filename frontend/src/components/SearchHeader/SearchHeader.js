import React, { useState } from 'react'

import searchIcon from '../../static/icons/search.png';
import { useHistory } from 'react-router-dom/cjs/react-router-dom';
import './SearchHeader.css';

export default function SearchHeader() {
    const history = useHistory();

    const [searchQuery, setSearchQuery] = useState("");

    const onSubmit = (e) => {
        e.preventDefault();
        history.push(`/results?q=${searchQuery}`);
    }
    
    const updateSearchQuery = (e) => {
        setSearchQuery(e.target.value);
    }

    return (
        <div className='search full-size'>
            <form className="header__search row-space-between full-size" onSubmit={onSubmit}>
                <input type="text" 
                    placeholder="Search" 
                    value={searchQuery}
                    onChange={updateSearchQuery}
                />

                <button type='submit' className='search-submit-button'>
                    <img src={searchIcon} alt='search-icon' className='svg' style={{ width: '24px', height: '24px' }} />
                </button>
            </form>
        </div>
    )
}
