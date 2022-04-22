import React, { useState } from 'react'
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';

import './SettingsPage.css';

export default function SettingsPage() {
	const dispatch = useDispatch();
	const history = useHistory();
	
	const [profileImageUrl, setProfileImageUrl] = useState('');
	const [bannerImageUrl, setBannerImageUrl] = useState('');
	const [about, setAbout] = useState('');
	
	const onSubmit = e => {
		e.preventDefault();
		
		// other stuff
	}
	
	return (
		<div id='settings-page' className=' test4'>
			<div className='test1 image-upload-container left1'>
				[profile picture upload here]
			</div>
			<div className='test2 image-upload-container left2'>
				[profile picture upload here]
			</div>
			
			<div className='test3 right'>
				[title and about section edit here]
				<form onSubmit={onSubmit}>
					<input type='text' name='about'
						id='about-input'
						value={about}
						onChange={e => setAbout(e.target.value)}
					/>
						
				</form>
			</div>
		</div>
	)
}
