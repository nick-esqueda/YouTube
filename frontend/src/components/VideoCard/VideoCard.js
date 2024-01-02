import React from 'react'
import { Link } from 'react-router-dom/cjs/react-router-dom';
import { useSelector } from 'react-redux'
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './VideoCard.css';

export default function VideoCard({ videoId }) {
  const video = useSelector(state => state.videos[videoId]);

  return (
    <div className='video-grid-item'>
      <Link to={`/watch/${video.id}`} className='thumbnail-wrapper col-top'>
        <img src={video.thumbnailUrl} alt='thumbnail'
          className='thumbnail'
        />
      </Link>

      <div className='video-thumbnail-details row-left row-top'>
        <div className='video-thumbnail-details-left'>
          <ProfileIcon channel={video.channel} />
        </div>
        <div className='video-thumbnail-details-right col-left'>
          <h4 className='line-clamp2'>{video.title}</h4>
          <span className='line-clamp2'>{video.channel.channelName}</span>
          <span className='line-clamp2'>{video.createdAt}</span>
        </div>
      </div>
    </div>
  )
}
