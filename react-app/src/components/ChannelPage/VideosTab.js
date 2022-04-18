import React from 'react'
import { Link } from 'react-router-dom';
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './VideosTab.css';

export default function VideosTab({ channel }) {
  console.log(channel);
  return (
    // <div style={{ margin: '24px', color: 'var(--gray-light)' }}>[Sorry! This page is currently under construction!]</div>
    <>
      <h4>Uploads</h4>

      {/* <div className='uploads-grid test2' >

      </div> */}

      <div className='video-row-grid'>
        {channel.videos.map(video => (
          <div key={video.id} className='video-grid-item col-top'>
            <Link to={`/watch/${video.id}`} className='thumbnail-wrapper col-top'>
              <img src={video.thumbnailUrl} alt='thumbnail'
                className='thumbnail'
              />
            </Link>

            <div className='video-thumbnail-details row-left row-top'>
              <div style={{ width: "36px", minWidth: '36px', height: "36px", marginRight: '12px' }}>
                <ProfileIcon channel={video.channel} />
              </div>
              <div className='col-left'>
                <h4 className='line-clamp2'>{video.title}</h4>
                <span className='line-clamp2'>{channel.channelName}</span>
                <span className='line-clamp2'>[# of views] * {video.createdAt}</span>
              </div>
            </div>
          </div>
        ))}
      </div>

    </>
  )
}
