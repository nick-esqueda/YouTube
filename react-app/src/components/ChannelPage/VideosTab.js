import React from 'react'
import { Link } from 'react-router-dom';
import { sortByCreatedAt } from '../../utils';

import './VideosTab.css';

export default function VideosTab({ channel }) {
	
	// console.log(channel.videos);
	// sortByCreatedAt(channel.videos);
	// console.log(channel.videos);

	return (
		<div id="videos-tab">
			{channel.videos.length === 0
				? <span className='subcount'>This channel does not have any videos yet.</span>
				: <h4>Uploads</h4>
			}

			<div className='video-row-grid row-left'>
				{channel.videos.map(video => (
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
