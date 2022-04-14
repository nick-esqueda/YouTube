import React from 'react'

import './Header.css';
import logo from '../../static/yt_logo_rgb_dark.png'
import hamburger from '../../static/icons/hamburger.png';
import newVideo from '../../static/icons/new-video.png';
import appsMenu from '../../static/icons/apps-menu.png';
import bellIcon from '../../static/icons/bell-icon.png';
import ProfileIcon from '../ProfileIcon/ProfileIcon';
import SearchHeader from '../SearchHeader/SearchHeader';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

export default function Header() {
	const sessionUser = useSelector(state => state.session.user);
	
	return (
		<header id='header' className='row-space-between'>
			<div id='header__left' className='row-space-even'>
				<div className='svg-wrapper'>
					<img src={hamburger} alt="menu-icon" className="svg" />
				</div>

				<Link to={`/`} className="logo-wrapper">
					<img src={logo} alt='logo' id='header__logo' className='' />
				</Link>
			</div>

			<div id='header__middle' className=''>
				<SearchHeader />
			</div>


			<div id='header__right' className='row-space-even'>
				<div className='svg-wrapper'>
					<img src={newVideo} alt='bell-icon' className='svg' />
				</div>
				<div className='svg-wrapper'>
					<img src={appsMenu} alt='apps-menu' className='svg' />

				</div>
				<div className='svg-wrapper'>
					<img src={bellIcon} alt='bell-icon' className='svg' />
				</div>
				<div className='pfp-wrapper-nav'>
					<ProfileIcon channel={sessionUser} />
				</div>
			</div>
		</header>
	)
}
