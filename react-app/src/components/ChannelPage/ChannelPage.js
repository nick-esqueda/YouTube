import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom';

import './ChannelPage.css';

export default function ChannelPage() {
	const [channel, setChannel] = useState({});
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
				
				<div id='channel-header__actions' className='test'>
					
				</div>
			</div>
		</div>
	)
}
