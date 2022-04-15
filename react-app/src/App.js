import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import { authenticate } from './store/session';
import Header from './components/Header/Header';
import Navbar from './components/Navbar/Navbar';
import ChannelPage from './components/ChannelPage/ChannelPage';
import SettingsPage from './components/SettingsPage/SettingsPage';

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
				<ProtectedRoute path='/channels/:channelId'>
					<ChannelPage />
				</ProtectedRoute>
				<ProtectedRoute path="/settings/:channelId">
					<SettingsPage />
				</ProtectedRoute>
				<ProtectedRoute path='/' exact={true} >
					<h1>My Home Page</h1>
				</ProtectedRoute>
				
				<Route>
					<h2>Sorry! We could not find the page you were looking for.</h2>
				</Route>
			</Switch>
		</BrowserRouter>
	);
}

export default App;
