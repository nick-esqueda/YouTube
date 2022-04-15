import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import Header from './components/Header/Header';
import Navbar from './components/Navbar/Navbar';
import ChannelPage from './components/ChannelPage/ChannelPage';
import VideoPage from './components/VideoPage/VideoPage';
import HomePage from './components/HomePage/HomePage';
import UploadVideoForm from './components/UploadVideoForm/UploadVideoForm';

function App() {
	const [loaded, setLoaded] = useState(false);
	const dispatch = useDispatch();

	useEffect(() => {
		(async () => {
			await dispatch(authenticate());
			setLoaded(true);
		})();
	}, [dispatch]);

	if (!loaded) {
		return null;
	}

	return (
		<BrowserRouter>
			<Header />
			<Navbar />
			<Switch>
				<Route path='/login' exact={true}>
					<LoginForm />
				</Route>
				
				<Route path='/sign-up' exact={true}>
					<SignUpForm />
				</Route>
				
				<ProtectedRoute path='/users' exact={true} >
					<UsersList />
				</ProtectedRoute>
				
				<Route path='/watch/:videoId' exact={true}>
					<VideoPage />
				</Route>
				
				<ProtectedRoute path='/upload' exact={true}>
					<UploadVideoForm />
				</ProtectedRoute>
				
				<ProtectedRoute path='/channels/:channelId'>
					<ChannelPage />
				</ProtectedRoute>
				
				<ProtectedRoute path='/' exact={true} >
					<HomePage />
				</ProtectedRoute>
				
			</Switch>
		</BrowserRouter>
	);
}

export default App;
