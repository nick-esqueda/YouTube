import React, { useEffect } from 'react'

import './VideosTab.css';
import { useDispatch, useSelector } from 'react-redux';
import VideoCard from '../VideoCard/VideoCard';
import { clearVideosState, fetchChannelsVideos } from '../../store/videos';
import { useParams } from 'react-router-dom/cjs/react-router-dom';

export default function VideosTab() {
	const { channelId } = useParams();
	const dispatch = useDispatch();

	const channelVideosIdList = useSelector(state => state.videos.idList);

	useEffect(() => {
		dispatch(fetchChannelsVideos(channelId, 1));
		return () => dispatch(clearVideosState());
	}, [dispatch, channelId]);

	const renderedVideos = channelVideosIdList?.map(videoId => (
		<VideoCard videoId={videoId} showChannelDetails={false} />
	));

	return !channelVideosIdList ? null : (
		<div id="videos-tab">
			{
				channelVideosIdList.length === 0
					? <span className='subcount'>This channel does not have any videos yet.</span>
					: <h4>Uploads</h4>
			}

			<div className='video-row-grid row-left'>
				{renderedVideos}
			</div>
		</div>
	)
}
