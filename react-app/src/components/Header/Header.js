import React from 'react'

import './Header.css';
import logo from '../../static/yt_logo_rgb_dark.png'
import hamburger from '../../static/icons/hamburger.png';
import newVideo from '../../static/icons/new-video.png';
import appsMenu from '../../static/icons/apps-menu.png';
import bellIcon from '../../static/icons/bell-icon.png';
import avatar from '../../static/icons/avatar.png';
import ProfileIcon from '../ProfileIcon/ProfileIcon';
import SearchHeader from '../SearchHeader/SearchHeader';
import { Link, useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';

export default function Header() {
	const history = useHistory();
	const sessionUser = useSelector(state => state.session.user);

	const loggedOut = (
		<div id='header__right' className='row-space-even'>
			<div style={{ visibility: 'hidden' }}>
				<img src={appsMenu} alt='apps-menu' className='svg' />
			</div>
			<div className='pfp-wrapper-nav'>
				<Link to={`/signup`} className='btn btn--blue-outline sign-in-btn'>
					<div className='svg-wrapper' style={{ width: 'auto', marginRight: '8px' }}>
						<img src={avatar} alt='apps-menu' className='svg-blue' />
					</div>
					<span>SIGN UP</span>
				</Link>
			</div>
		</div>
	)

	return (
		<header id='header' className='row-space-between'>
			<div id='header__left' className='row-space-even'>
				<div className='svg-wrapper' style={{ visibility: 'hidden' }}>
					<img src={hamburger} alt="menu-icon" className="svg" />
				</div>

				<Link to={`/`} className="logo-wrapper">
					<img src={logo} alt='logo' id='header__logo' className='' />
				</Link>
			</div>

			<div id='header__middle' style={{ visibility: 'hidden' }}>
				<SearchHeader />
			</div>


			{!sessionUser ? loggedOut : (
				<div id='header__right' className='row-right'>
					<div className='svg-wrapper pointer' onClick={_ => history.push('/upload')}>
						<img src={newVideo} alt='bell-icon' className='svg' />
					</div>
					{/* <div className='svg-wrapper disabled'>
						<img src={appsMenu} alt='apps-menu' className='svg' />
					</div> */}
					{/* <div className='svg-wrapper disabled'>
						<img src={bellIcon} alt='bell-icon' className='svg' />
					</div> */}
					<div className='pfp-wrapper-nav'>
						<ProfileIcon channel={sessionUser} isNav={true} />
					</div>
				</div>
			)}
		</header>
	)
}
