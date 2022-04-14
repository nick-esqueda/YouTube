import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom';

import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './ChannelPage.css';

export default function ChannelPage() {
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

				<div id='channel-header__actions' className='test2'>
					<div className='channel-info row-space-between full-size test3'>
						<div style={{ width: "80px", height: "80px" }}>
							<ProfileIcon />
						</div>
					</div>
					<div className='tabs row-space-between test4'>
						<div id='channel__tabs-container' className='row-space-even'>
							<div
								className={activeTab === 1 ? 'tab active-tab' : 'tab'}
								onClick={() => setActiveTab(1)}
							>HOME</div>
							<div
								className={activeTab === 2 ? 'tab active-tab' : 'tab'}
								onClick={() => setActiveTab(2)}
							>VIDEOS</div>
							<div
								className={activeTab === 3 ? 'tab active-tab' : 'tab'}
								onClick={() => setActiveTab(3)}
							>CHANNELS</div>
							<div
								className={activeTab === 3 ? 'tab active-tab' : 'tab'}
								onClick={() => setActiveTab(3)}
							>ABOUT</div>
						</div>

					</div>
				</div>
			</div>
		</div>
	)
}
