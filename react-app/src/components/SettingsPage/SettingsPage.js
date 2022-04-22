import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { editChannel } from '../../store/channels';

import './SettingsPage.css';

export default function SettingsPage() {
	const dispatch = useDispatch();
	const history = useHistory();

	const sessionUser = useSelector(state => state.session.user);
	const [profileImageUrl, setProfileImageUrl] = useState(sessionUser.profileImageUrl);
	const [bannerImageUrl, setBannerImageUrl] = useState(sessionUser.bannerImageUrl);
	const [about, setAbout] = useState(sessionUser.about ? sessionUser.about : '');
	
	console.log('session user', sessionUser);
	console.log('profile image', profileImageUrl);
	console.log('banner image', bannerImageUrl);

	const onSubmit = e => {
		e.preventDefault();

		const editedChannel = {
			id: sessionUser.id, profileImageUrl, bannerImageUrl, about
		}

		dispatch(editChannel(editedChannel))
			.then(_ => {
				return history.push(`/channels/${sessionUser.id}`)
			})
			.catch(async (data) => {
				if (data && data.errors) {
					// setValidationErrors(data.errors);
					console.log(data.errors);
				}
			});


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
