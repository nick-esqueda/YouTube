import React from 'react'
import { Link } from 'react-router-dom/cjs/react-router-dom';
import { useSelector } from 'react-redux'
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './VideoCard.css';

export default function VideoCard({ videoId, showChannelDetails = true }) {
  const video = useSelector(state => state.videos.entities[videoId]);

  let renderedVideoDetails;
  const renderedTitle = <h4 className='line-clamp2'>{video?.title}</h4>;
  const renderedChannelName = <span className='line-clamp2'>{video?.channel.channelName}</span>;
  const renderedCreatedAt = <span className='line-clamp2'>{video?.createdAt}</span>;

  if (showChannelDetails) {
    renderedVideoDetails = (
      <>
        <div className='video-thumbnail-details-left'>
          <ProfileIcon channel={video?.channel} />
        </div>
        <div className='video-thumbnail-details-right col-left'>
          {renderedTitle}
          {renderedChannelName}
          {renderedCreatedAt}
        </div>
      </>
    );
  } else {
    renderedVideoDetails = (
      <div className='col-left'>
        {renderedTitle}
        {renderedCreatedAt}
      </div>
    );
  }

  const videoThumbnail = (
    <Link to={`/watch/${video?.id}`} className='thumbnail-wrapper col-top'>
      <img src={video?.thumbnailUrl} alt='thumbnail'
        className='thumbnail'
      />
    </Link>
  );

  return (
    <div className='full-size col-top'>
      {videoThumbnail}

      <div className='video-thumbnail-details row-left row-top'>
        {renderedVideoDetails}
      </div>
    </div>
  )
}
