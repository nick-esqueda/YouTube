import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Link, Redirect } from 'react-router-dom';
import { login, signUp } from '../../store/session';

import './LoginSignup.css';
import logo from '../../static/yt_logo_rgb_dark.png';

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
		}
	};

	const loginDemoUser = async () => {
		await dispatch(login('demo@aa.io', 'password'))
	}

	const updateUsername = (e) => {
		setUsername(e.target.value);
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
			<form onSubmit={onSignUp} id="signup-form">
				<div style={{ marginBottom: '42px' }}>
					<img src={logo} alt='logo' style={{ width: '160px' }} />
				</div>

				<div>
					{errors.map((error, ind) => (
						<div key={ind}>{error}</div>
					))}
				</div>

				<h2 style={{ fontSize: '20px', fontWeight: '500' }}>Your Channel Name</h2>
				<input
					type='text'
					name='username'
					placeholder='Pick a channel name'
					onChange={updateUsername}
					value={username}
				></input>

				<h2 style={{ fontSize: '20px', fontWeight: '500' }}>Email</h2>
				<input
					type='text'
					name='email'
					placeholder='Enter your email'
					onChange={updateEmail}
					value={email}
				></input>

				<h2 style={{ fontSize: '20px', fontWeight: '500' }}>Password</h2>
				<input
					type='password'
					name='password'
					placeholder='Enter a password'
					onChange={updatePassword}
					value={password}
				></input>

				<h2 style={{ fontSize: '20px', fontWeight: '500' }}>Confirm Password</h2>
				<input
					type='password'
					name='repeat_password'
					placeholder='Confirm your password'
					onChange={updateRepeatPassword}
					value={repeatPassword}
					required={true}
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
