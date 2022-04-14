import React, { useEffect, useState } from 'react'
import { NavLink, Route, Router, Switch, useParams, useRouteMatch } from 'react-router-dom';

import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './ChannelPage.css';

export default function ChannelPage() {
	const { path, url } = useRouteMatch();
	const [channel, setChannel] = useState({});
	const [activeTab, setActiveTab] = useState(1);
	const { channelId } = useParams();

	useEffect(() => {
		if (!channelId) {
			return;
		}
		(async () => {
			const response = await fetch(`/api/channels/${channelId}`);
			const channel = await response.json();
			setChannel(channel);
		})();
	}, [channelId]);

	return (
		<div id='channel-page' className='test'>
			<div id='channel-header'>
				{!channel.bannerImageUrl ? null : (
					<div id='channel-banner'>
						<img src={channel.bannerImageUrl} alt="banner" />
					</div>
				)}

				<div id='channel-header__actions' className='col-left'>
					<div className='channel-info row-space-between full-size'>
						<div style={{ minWidth: "80px", height: "80px", marginRight: '20px' }}>
							<ProfileIcon channel={channel} />
						</div>
						
						<div className='col-left full-size'>
							<h2>{channel.channelName}</h2>
							<span className='subcount'>[# of subscribers]</span>
						</div>
						
						<button className='btn btn--red disabled'>
							subscribe
						</button>
					</div>
					
					<div className='tabs row-space-between test4'>
						<div id='channel__tabs-container' className='row-space-even'>
							<NavLink to={`${url}/home`}
								className={activeTab === 1 ? 'tab active-tab' : 'tab'}
								onClick={() => setActiveTab(1)}
							>HOME</NavLink>
							<NavLink to={`${url}/videos`}
								className={activeTab === 2 ? 'tab active-tab' : 'tab'}
								onClick={() => setActiveTab(2)}
							>VIDEOS</NavLink>
							<NavLink to={`${url}/channels`}
								className={activeTab === 3 ? 'tab active-tab' : 'tab'}
								onClick={() => setActiveTab(3)}
							>CHANNELS</NavLink>
							<NavLink to={`${url}/about`}
								className={activeTab === 3 ? 'tab active-tab' : 'tab'}
								onClick={() => setActiveTab(3)}
							>ABOUT</NavLink>
						</div>
					</div>
				</div>
			</div>
			
			<Switch>
				<Route exact path={path}>
					route 1
				</Route>
				<Route exact path={`${path}/home`}>
					<h1>route 2</h1>
				</Route>
				<Route exact path={`${path}/videos`}>
					route 3
				</Route>
				<Route exact path={`${path}/channels`}>
					route 4
				</Route>
				<Route exact path={`${path}/about`}>
					route 5
				</Route>
			</Switch>
		</div>
	)
}
