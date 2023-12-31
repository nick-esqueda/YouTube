import React from 'react'
import { Link } from 'react-router-dom';
import { sortByCreatedAt } from '../../utils';

import './VideosTab.css';
import { useSelector } from 'react-redux';

export default function VideosTab() {
	let channelsVideos = useSelector(state => state.videos);
	channelsVideos = Object.values(channelsVideos);

	return (
		<div id="videos-tab">
			{channelsVideos.length === 0
				? <span className='subcount'>This channel does not have any videos yet.</span>
				: <h4>Uploads</h4>
			}

			<div className='video-row-grid row-left'>
				{channelsVideos.map(video => (
					<div key={video.id} className='video-grid-item col-top'>
						<Link to={`/watch/${video.id}`} className='thumbnail-wrapper col-top'>
							<img src={video.thumbnailUrl} alt='thumbnail'
								className='thumbnail'
							/>
						</Link>

						<div className='video-thumbnail-details row-left row-top'>
							<div className='col-left'>
								<h4 className='line-clamp2'>{video.title}</h4>
								<span className='line-clamp2'>{video.createdAt}</span>
							</div>
						</div>
					</div>
				))}
			</div>

		</div>
	)
}
