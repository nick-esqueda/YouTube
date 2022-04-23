import React, { useEffect, useRef, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { editChannel } from '../../store/channels';
import axios from 'axios';

import './SettingsPage.css';
import defaultPfp from '../../static/default-profile-image.png';
import loadingWheel from '../../static/icons/loading-wheel.gif';
import addThumbnail from '../../static/icons/add-thumbnail.png';

export default function SettingsPage() {
	const dispatch = useDispatch();
	const history = useHistory();
	const pfpInputRef = useRef();
	const bannerInputRef = useRef();

	const sessionUser = useSelector(state => state.session.user);
	const [profileImageUrl, setProfileImageUrl] = useState(sessionUser.profileImageUrl);
	const [bannerImageUrl, setBannerImageUrl] = useState(sessionUser.bannerImageUrl ? sessionUser.bannerImageUrl : '');
	const [about, setAbout] = useState(sessionUser.about ? sessionUser.about : '');
	const [showErrors, setShowErrors] = useState(false);
	const [validationErrors, setValidationErrors] = useState([]);

	useEffect(() => {
		const errors = [];
		if (about.length > 5000) errors.push('Sorry! Your channel description must be shorter than 5000 characters');

		setValidationErrors(errors);
	}, [about]);


	const s3Upload = async (file, type) => {
		if (!file) return console.error('upload a file first');
		const formData = new FormData();

		formData.append('file', file);

		if (type === 'profile') {
			setProfileImageUrl(loadingWheel);
			const { data: url } = await axios.post("/api/s3/upload/image", formData);
			setProfileImageUrl(url);
		} else if (type === 'banner') {
			setBannerImageUrl(loadingWheel);
			const { data: url } = await axios.post("/api/s3/upload/image", formData);
			setBannerImageUrl(url);
		}
	}

	const onSubmit = e => {
		e.preventDefault();
		
		if (validationErrors.length) return setShowErrors(true);

		const editedChannel = {
			id: sessionUser.id, profileImageUrl, bannerImageUrl, about
		}			

		dispatch(editChannel(editedChannel))
			.then(_ => {
				return history.push(`/channels/${sessionUser.id}/about`);
			})
			.catch(async (data) => {
				if (data && data.errors) {
					// setValidationErrors(data.errors);
					console.log(data.errors);
				}
			});
	}

	return (
		<div id='settings-page' className='test4'>
			<form onSubmit={onSubmit}>
				<div className='test1 image-upload-container left1'>
					<div className="image-preview col-center pointer" onClick={() => pfpInputRef.current.click()}>
						{profileImageUrl.startsWith('https://') ? (
							<img
								src={profileImageUrl}
								alt="pfp-preview"
								className=""
							/>
						) : (
							<img
								src={defaultPfp}
								alt='pfp-preview'
								className=''
							/>
						)}
					</div>

					<input type="file"
						accept="image/*"
						name="profileImageUrl"
						ref={pfpInputRef}
						hidden={true}
						onChange={e => s3Upload(e.target.files[0], 'profile')}
					/>
				</div>

				<div className='test2 image-upload-container left2'>
					<div className="image-preview col-center pointer" onClick={() => bannerInputRef.current.click()}>
						{bannerImageUrl.startsWith('https://') ? (
							<img
								src={bannerImageUrl}
								alt="pfp-preview"
								className=""
							/>
						) : (
							<>
								<div className='svg-wrapper' style={{ width: "32px" }}>
									<img
										src={!bannerImageUrl ? addThumbnail : loadingWheel}
										alt="banner-preview"
										className={!bannerImageUrl ? "svg" : ""}
									/>
								</div>
								<span className='subcount'>{!bannerImageUrl ? "Upload Banner Image" : "Processing image..."}</span>
							</>
						)}
					</div>

					<input type="file"
						accept="image/*"
						name="bannerImageUrl"
						ref={bannerInputRef}
						hidden={true}
						onChange={e => s3Upload(e.target.files[0], 'banner')}
					/>
				</div>

				<div className='test3 right'>
					<div>
						<textarea
							type='text'
							id='about-input'
							className={validationErrors.includes('Sorry! Your channel description must be shorter than 5000 characters') ? 'red-outline' : ''}
							placeholder='Tell everyone about your channel'
							name='about'
							value={about}
							onChange={(e) => setAbout(e.target.value)}
						// onInput={autoGrow}
						// onFocus={e => {
						// 	descriptionWrapperRef.current.style.borderColor = 'var(--blue)';
						// 	descriptionSpanRef.current.style.color = 'var(--blue)';
						// }}
						// onBlur={e => {
						// 	descriptionWrapperRef.current.style.borderColor = ''
						// 	descriptionSpanRef.current.style.color = '';
						// }}
						></textarea>
					</div>
				</div>

				<div className='error-container col-right col-bottom'>
					{showErrors && validationErrors.map(err => (
						<div key={err} className='right-align'>{err}</div>
					))}
				</div>

				<div style={{ margin: '12px 0' }}>
					<button type='button' className='btn btn--blue-outline' 
						onClick={() => history.push(`/channels/${sessionUser.id}/about`)}
					>CANCEL CHANGES</button>
					<button type='submit' className='btn btn--blue-outline'>SUBMIT CHANGES</button>
				</div>

			</form>
		</div >
	)
}
