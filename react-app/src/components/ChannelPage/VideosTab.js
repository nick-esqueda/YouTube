import React from 'react'
import { Link } from 'react-router-dom';

import './VideosTab.css';

export default function VideosTab({ channel }) {
	
	
	return (
		<div id="videos-tab">
			<h4>Uploads</h4>

			<div className='video-row-grid'>
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
