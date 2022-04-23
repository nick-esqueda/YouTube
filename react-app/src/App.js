import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/LoginSignup/LoginForm';
import SignupForm from './components/LoginSignup/SignupForm';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import { authenticate } from './store/session';
import Header from './components/Header/Header';
import Navbar from './components/Navbar/Navbar';
import ChannelPage from './components/ChannelPage/ChannelPage';
import SettingsPage from './components/SettingsPage/SettingsPage';
import VideoPage from './components/VideoPage/VideoPage';
import HomePage from './components/HomePage/HomePage';
import VideoForm from './components/VideoForm/VideoForm';
import PageNotFound from './components/PageNotFound/PageNotFound';

function App() {
	const dispatch = useDispatch();
	const [loaded, setLoaded] = useState(false);

	useEffect(() => {
		(async () => {
			await dispatch(authenticate());
			setLoaded(true);
		})();
	}, [dispatch]);


	return !loaded ? null : (
		<BrowserRouter>
			<Header />
			<Switch>
				<Route path='/login' exact={true}>
					<Navbar />
					<LoginForm />
				</Route>

				<Route path='/signup' exact={true}>
					<Navbar />
					<SignupForm />
				</Route>

				<ProtectedRoute path='/users' exact={true} >
					<Navbar />
					<UsersList />
				</ProtectedRoute>

				<Route path='/watch/:videoId' exact={true}>
					<VideoPage />
				</Route>

				<ProtectedRoute path='/upload' exact={true}>
					<Navbar />
					<VideoForm />
				</ProtectedRoute>

				<ProtectedRoute path='/videos/:videoId/edit' exact={true}>
					<Navbar />
					<VideoForm />
				</ProtectedRoute>

				<ProtectedRoute path='/channels/:channelId'>
					<Navbar />
					<ChannelPage />
				</ProtectedRoute>

				<ProtectedRoute path="/settings/:channelId">
					<Navbar />
					<SettingsPage />
				</ProtectedRoute>

				<Route path='/' exact={true} >
					<Navbar />
					<HomePage />
				</Route>

				<Route>
					<Navbar />
					<PageNotFound />
				</Route>
			</Switch>
		</BrowserRouter>
	);
}

export default App;
