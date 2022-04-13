import React from 'react'

import './Header.css';
import logo from '../../static/yt_logo_rgb_dark.png'
import hamburger from '../../static/icons/hamburger.png';

export default function Header() {
  return (
    <header id='header' className='row-space-between'>
      <div id='header__left' className='row-space-even'>
        <div className='hamburger'>
          <img src={hamburger} className="svg" />
        </div>
        
        <div className="logo-wrapper">
          <img src={logo} alt='logo' id='header__logo' className='' />
        </div>
      </div>

      ausdfasdjfaskdjfasdf
    </header>
  )
}
