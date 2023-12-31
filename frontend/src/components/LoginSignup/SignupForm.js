import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Link, Redirect } from 'react-router-dom';
import { login, signUp } from '../../store/session';

import './LoginSignup.css';
import logo from '../../static/yt_logo_rgb_dark.png';
import bgVideo from '../../static/youtube-rewind.mp4';

const SignUpForm = () => {
	const [errors, setErrors] = useState([]);
	const [username, setUsername] = useState('');
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [repeatPassword, setRepeatPassword] = useState('');
	const user = useSelector(state => state.session.user);
	const dispatch = useDispatch();

	const onSignUp = async (e) => {
		e.preventDefault();
		if (password === repeatPassword) {
			const data = await dispatch(signUp(username, email, password));
			if (data) {
				setErrors(data)
			}
		} else {
			setErrors(['password : Passwords do not match.']);
		}
	};

	const loginDemoUser = async () => {
		await dispatch(login('demo@aa.io', 'password'))
	}

	const updateUsername = (e) => {
		setUsername(e.target.value.replace(/[^a-zA-Z0-9\s]/g, ''));
	};

	const updateEmail = (e) => {
		setEmail(e.target.value);
	};

	const updatePassword = (e) => {
		setPassword(e.target.value);
	};

	const updateRepeatPassword = (e) => {
		setRepeatPassword(e.target.value);
	};

	if (user) {
		return <Redirect to='/' />;
	}

	return (
		<div id='signup-page'>
			<div>
				<video id="bg-video" autoPlay muted loop>
					<source src={bgVideo} type="video/mp4" />
				</video>
			</div>
			
			<form onSubmit={onSignUp} id="signup-form">
				<div style={{ marginBottom: '48px' }}>
					<Link to='/'>
						<img src={logo} alt='logo' style={{ width: '140px' }} />
					</Link>
				</div>

				<div className='col-right' style={{ marginBottom: '16px' }}>
					{errors.map((error, ind) => (
						<span key={ind} className="subcount">{error.toUpperCase()}</span>
					))}
				</div>

				<h2 style={{ fontSize: '18px', fontWeight: '500' }}>Your Channel Name</h2>
				<input
					type='text'
					name='username'
					placeholder='Pick a channel name'
					onChange={updateUsername}
					value={username}
					style={
						errors.find(
							err => err.toUpperCase() === 'CHANNELNAME : THIS FIELD IS REQUIRED.'
								|| err.toUpperCase() === 'CHANNELNAME : USERNAME IS ALREADY IN USE.'
								|| err.toUpperCase() === 'CHANNELNAME : FIRST CHARACTER MUST BE A LETTER.'
						)
							? { borderColor: 'var(--red)' }
							: {}
					}

				></input>

				<h2 style={{ fontSize: '18px', fontWeight: '500' }}>Email</h2>
				<input
					type='text'
					name='email'
					placeholder='Enter your email'
					onChange={updateEmail}
					value={email}
					style={
						errors.find(
							err => err.toUpperCase() === 'EMAIL : THIS FIELD IS REQUIRED.'
								|| err.toUpperCase() === 'EMAIL : EMAIL ADDRESS IS ALREADY IN USE.'
								|| err.toUpperCase() === 'EMAIL : INVALID EMAIL ADDRESS.'
						)
							? { borderColor: 'var(--red)' }
							: {}
					}

				></input>

				<h2 style={{ fontSize: '18px', fontWeight: '500' }}>Password</h2>
				<input
					type='password'
					name='password'
					placeholder='Enter a password'
					onChange={updatePassword}
					value={password}
					style={
						errors.find(
							err => err.toUpperCase() === 'PASSWORD : THIS FIELD IS REQUIRED.'
								|| err.toUpperCase() === 'PASSWORD : PASSWORDS DO NOT MATCH.'
								|| err.toUpperCase() === 'PASSWORD : FIELD MUST BE AT LEAST 8 CHARACTERS LONG.'
						)
							? { borderColor: 'var(--red)' }
							: {}
					}

				></input>

				<h2 style={{ fontSize: '18px', fontWeight: '500' }}>Confirm Password</h2>
				<input
					type='password'
					name='repeat_password'
					placeholder='Confirm your password'
					onChange={updateRepeatPassword}
					value={repeatPassword}
					style={
						errors.find(
							err => err.toUpperCase() === 'PASSWORD : PASSWORDS DO NOT MATCH.'
						)
							? { borderColor: 'var(--red)' }
							: {}
					}
				// required={true}	
				></input>

				<div className='row-space-between row-bottom' style={{ gap: '16px' }}>
					<Link to='/login' style={{ color: 'var(--blue)', fontSize: '14px' }}>Already have an account?</Link>

					<div className='row-right'>
						<button type='button' onClick={loginDemoUser} className='btn'>demo</button>
						<button type='submit' className='btn btn--blue-outline'>Sign Up</button>
					</div>
				</div>

			</form>
		</div>
	);
};

export default SignUpForm;
