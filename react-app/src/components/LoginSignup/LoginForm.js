import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link, Redirect } from 'react-router-dom';
import { login } from '../../store/session';

import './LoginSignup.css';
import logo from '../../static/yt_logo_rgb_dark.png';

const LoginForm = () => {
	const [errors, setErrors] = useState([]);
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const user = useSelector(state => state.session.user);
	const dispatch = useDispatch();

	const onLogin = async (e) => {
		e.preventDefault();
		const data = await dispatch(login(email, password));
		if (data) {
			setErrors(data);
		}
	};

	const loginDemoUser = async () => {
		await dispatch(login('demo@aa.io', 'password'));
	}

	const updateEmail = (e) => {
		setEmail(e.target.value);
	};

	const updatePassword = (e) => {
		setPassword(e.target.value);
	};

	if (user) {
		return <Redirect to='/' />;
	}

	return (
		<div id="login-page">
			<form onSubmit={onLogin} id='login-form'>
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

				<h2 style={{ fontSize: '18px', fontWeight: '500' }}>Email</h2>
				<input
					name='email'
					type='text'
					placeholder='Enter your email'
					value={email}
					onChange={updateEmail}
					style={
						errors.find(
							err => err.toUpperCase() === 'EMAIL : THIS FIELD IS REQUIRED.'
								|| err.toUpperCase() === 'EMAIL : EMAIL PROVIDED NOT FOUND.')
							? { borderColor: 'var(--red)' }
							: {}
					}
				/>

				<h2 style={{ fontSize: '18px', fontWeight: '500' }}>Password</h2>
				<input
					name='password'
					type='password'
					placeholder='Enter your password'
					value={password}
					onChange={updatePassword}
					style={
						errors.find(
							err => err.toUpperCase() === 'PASSWORD : THIS FIELD IS REQUIRED.'
								|| err.toUpperCase() === 'PASSWORD : PASSWORD WAS INCORRECT.'
								|| err.toUpperCase() === 'PASSWORD : NO SUCH USER EXISTS.')
							? { borderColor: 'var(--red)' }
							: {}
					}
				/>

				<div className='row-space-between row-bottom' style={{ gap: '16px' }}>
					<Link to='/signup' style={{ color: 'var(--blue)', fontSize: '14px' }}>Don't have an account yet?</Link>

					<div className='row-right'>
						<button type='button' onClick={loginDemoUser} className='btn'>demo</button>
						<button type='submit' className='btn btn--blue-outline'>Login</button>
					</div>
				</div>
			</form>
		</div>
	);
};

export default LoginForm;
