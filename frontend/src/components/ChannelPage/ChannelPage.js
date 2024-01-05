import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, Route, Switch, useParams, useRouteMatch } from 'react-router-dom';
import { fetchChannel } from '../../store/channels';
import { fetchChannelsVideos } from '../../store/videos';

import ProfileIcon from '../ProfileIcon/ProfileIcon';
import AboutTab from './AboutTab';
import ChannelsTab from './ChannelsTab';
import VideosTab from './VideosTab';

import './ChannelPage.css';
import LoadingWheel from '../LoadingWheel/LoadingWheel';

export default function ChannelPage() {
	const { channelId } = useParams();
	const { path, url } = useRouteMatch();
	const dispatch = useDispatch();
	const channel = useSelector(state => state.channels[channelId]);
	const [isLoaded, setIsLoaded] = useState(false);
	// const [activeTab, setActiveTab] = useState(1);

	useEffect(() => {
		if (!channelId) return;
		(async () => {
			await dispatch(fetchChannel(channelId));
			await dispatch(fetchChannelsVideos(channelId, 1));
			setIsLoaded(true);
		})();
	}, [dispatch, channelId]);

	return !isLoaded ? <LoadingWheel /> : (
		<div id='channel-page' className='col-top'>
			<div id='channel-header'>
				{!channel.bannerImageUrl ? null : (
					<div id='channel-banner'>
						<img src={channel.bannerImageUrl} onError={() => document.getElementById('channel-banner').remove()} alt="banner" />
					</div>
				)}

				<div style={{ width: '100%', backgroundColor: 'var(--gray-darkest)' }}>
					<div id='channel-header__actions' className='col-left'>
						<div className='channel-info row-space-between full-size'>
							<div style={{ minWidth: "80px", height: "80px", marginRight: '20px' }}>
								<ProfileIcon channel={channel} />
							</div>

							<div className='col-left full-size'>
								<h2>{channel.channelName}</h2>
								<span className='subcount' style={{ visibility: 'hidden' }}>[# of subscribers]</span>
							</div>

							{/* <button className='btn btn--red disabled'>
								SUBSCRIBE
							</button> */}
						</div>

						<div className='tabs row-space-between'>
							<div id='channel__tabs-container' className='row-space-even'>
								{/* <NavLink to={`${url}/home`}
									className='tab'
									activeClassName="active-tab"
								>HOME</NavLink> */}
								<NavLink to={`${url}/videos`}
									className='tab'
									activeClassName="active-tab"
								>VIDEOS</NavLink>
								{/* <NavLink to={`${url}/channels`}
									className='tab'
									activeClassName="active-tab"
								>CHANNELS</NavLink> */}
								<NavLink to={`${url}/about`}
									className='tab'
									activeClassName="active-tab"
								>ABOUT</NavLink>
							</div>
						</div>
					</div>
				</div>
			</div>

			<Switch>
				<Route exact path={`${path}/home`}>
					{/* <User /> */}
				</Route>
				<Route exact path={`${path}/videos`}>
					<VideosTab />
				</Route>
				<Route exact path={`${path}/channels`}>
					<ChannelsTab channel={channel} />
				</Route>
				<Route exact path={`${path}/about`}>
					<AboutTab channel={channel} />
				</Route>
			</Switch>
		</div>
	)
}
