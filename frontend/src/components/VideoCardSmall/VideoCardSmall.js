import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom/cjs/react-router-dom';

import './VideoCardSmall.css';

export default function VideoCardSmall({ videoId }) {
  const video = useSelector(state => state.videos[videoId]);

  return (
    <div className='video-card-small row-left row-top'>
      <Link to={`/watch/${video.id}`} className='thumbnail-wrapper col-top'>
        <img src={video.thumbnailUrl} alt='thumbnail'
          className='thumbnail'
        />
      </Link>

      <div className='video-card-small-details col-left col-top'>
        <h4 className='line-clamp2'>{video.title}</h4>
        <span className='line-clamp2'>{video.channel.channelName}</span>
        <span className='line-clamp2'>{video.createdAt}</span>
      </div>
    </div>
  )
}
