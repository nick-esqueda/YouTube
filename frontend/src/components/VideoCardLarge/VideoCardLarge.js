import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom/cjs/react-router-dom';

import './VideoCardLarge.css';
import ProfileIcon from '../ProfileIcon/ProfileIcon';

export default function VideoCardLarge({ videoId }) {
  const video = useSelector(state => state.videos.entities[videoId]);

  return (
    <div className='video-card-large full-size row-top row-left'>
      <Link to={`/watch/${video.id}`} className='thumbnail-wrapper col-top'>
        <img src={video.thumbnailUrl} alt='thumbnail'
          className='thumbnail'
        />
      </Link>

      <div className='video-card-large-details col-top'>
        <div className='col-left' style={{ marginBottom: '14px'}}>
          <h4 className='line-clamp2'>{video.title}</h4>
          <span className='line-clamp2'>{video.createdAt}</span>
        </div>
        <div className='row-left'>
          <div style={{ minWidth: "28px", height: "28px", marginRight: '10px' }}>
            <ProfileIcon channel={video.channel} />
          </div>
          <span className='line-clamp2'>{video.channel.channelName}</span>
        </div>
        <span className='line-clamp2' style={{ margin: '12px 0'}}>
          {video.description}
        </span>
      </div>
    </div>
  )
}
