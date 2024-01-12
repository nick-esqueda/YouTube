import React from 'react'
import { Link } from 'react-router-dom/cjs/react-router-dom';
import { useSelector } from 'react-redux'
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './VideoCard.css';


export default function VideoCard({ videoId, videoDetailsStyle, isVerticalOrientation = true }) {
  const video = useSelector(state => state.videos.entities[videoId]);

  const renderedVideoDetails = getVideoCardDetailsFromName(videoDetailsStyle, video);

  const videoThumbnail = (
    <Link to={`/watch/${video?.id}`}
      className={isVerticalOrientation ? 'thumbnail-wrapper-vertical' : 'thumbnail-wrapper-horizontal'}
    >
      <img src={video?.thumbnailUrl} alt='thumbnail' className='thumbnail' />
    </Link>
  );

  return (
    <div className={
      'video-card full-size ' + (isVerticalOrientation ? 'col-top' : 'row-top row-left')
    }>
      {videoThumbnail}
      {renderedVideoDetails}
    </div >
  )
}


const getVideoCardDetailsFromName = (name, video) => {
  if (!video) {
    return;
  }

  const renderedTitle = <h4 className='line-clamp2'>{video.title}</h4>;
  const renderedChannelName = <span className='line-clamp2'>{video.channel.channelName}</span>;
  const renderedCreatedAt = <span className='line-clamp2'>{video.createdAt}</span>;

  switch (name) {
    case 'small': {
      return (
        <div className='video-card-small-details col-left col-top'>
          {renderedTitle}
          {renderedChannelName}
          {renderedCreatedAt}
        </div>
      );
    }
    case 'mediumNoChannelInfo': {
      return (
        <div className='video-thumbnail-details row-left row-top'>
          <div className='col-left'>
            {renderedTitle}
            {renderedCreatedAt}
          </div>
        </div>
      );
    }
    case 'medium': {
      return (
        <div className='video-thumbnail-details row-left row-top'>
          <div className='video-thumbnail-details-left'>
            <ProfileIcon channel={video?.channel} />
          </div>
          <div className='video-thumbnail-details-right col-left'>
            {renderedTitle}
            {renderedChannelName}
            {renderedCreatedAt}
          </div>
        </div>
      );
    }
    case 'large': {
      return (
        <div className='video-card-large-details col-top'>
          <div className='col-left' style={{ marginBottom: '14px' }}>
            {renderedTitle}
            {renderedCreatedAt}
          </div>
          <div className='row-left'>
            <div style={{ minWidth: "28px", height: "28px", marginRight: '10px' }}>
              <ProfileIcon channel={video.channel} />
            </div>
            <span className='line-clamp2'>{video.channel.channelName}</span>
          </div>
          <span className='line-clamp2' style={{ margin: '12px 0' }}>
            {video.description}
          </span>
        </div>
      );
    }
    default:
      console.error("please specify the videoDetailsStyle prop.");
      return "please specify the videoDetailsStyle prop."
  }
}
