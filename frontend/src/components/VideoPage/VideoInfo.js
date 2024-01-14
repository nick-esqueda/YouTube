import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom'
import { deleteVideo, toggleVideoLike, toggleVideoDislike, } from '../../store/videos';

import threeDots from '../../static/icons/three-dots.png';
import pencil from '../../static/icons/pencil.png';
import trash from '../../static/icons/trash.png';
import './VideoPage.css';


export default function VideoInfo() {
  const { videoId } = useParams();
  const dispatch = useDispatch();
  const history = useHistory();

  const sessionUser = useSelector(state => state.session.user);
  const video = useSelector(state => state.videos.entities[videoId]);
  const isLiked = useSelector(state => state.videos.entities[videoId]?.isLikedByCurrentUser);
  const isDisliked = useSelector(state => state.videos.entities[videoId]?.isDislikedByCurrentUser);
  const videoLikeCount = useSelector(state => state.videos.entities[videoId]?.likeCount);
  const videoDislikeCount = useSelector(state => state.videos.entities[videoId]?.dislikeCount);
  const [showMenu, setShowMenu] = useState(false);

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = () => {
      setShowMenu(false);
    };

    document.addEventListener('click', closeMenu);

    return () => {
      setShowMenu(false);
      document.removeEventListener("click", closeMenu);
    }
  }, [showMenu]);


  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  const confirmDelete = async e => {
    if (window.confirm('Are you sure you want to delete your video?')) {
      if (window.confirm('Video deletion is permanent and cannot be undone. Do you wish to continue?')) {
        // setIsLoaded(false); // need this? it was here before refactor
        await dispatch(deleteVideo(video.id));
        return history.push('/');
      }
    }
  }

  const toggleLike = async () => {
    // user cannot dislike and like a video simultaneously.
    // so the dislike must be removed before liking.
    if (isDisliked) {
      dispatch(toggleVideoDislike(videoId));
    }
    dispatch(toggleVideoLike(videoId));
  }

  const toggleDislike = async () => {
    // user cannot like and dislike a video simultaneously.
    // so the like must be removed before disliking.
    if (isLiked) {
      dispatch(toggleVideoLike(videoId));
    }
    dispatch(toggleVideoDislike(videoId));

  }

  return !video ? null : (
    <div className='video-info row-space-between'>
      <div className='col-left'>
        <h4>{video.title}</h4>
        <span className='subcount'>{video.createdAt}</span>
      </div>

      <div className='row-space-between' style={{ width: "150px" }}>
        <button onClick={toggleLike} style={{ color: isLiked ? 'green' : 'white' }}>
          likes: {videoLikeCount}</button>
        <button onClick={toggleDislike} style={{ color: isDisliked ? 'red' : 'white' }}>
          dislikes: {videoDislikeCount}</button>
      </div>


      {video.channelId === sessionUser?.id && (
        <div className='svg-wrapper pointer' onClick={openMenu}>
          <img src={threeDots} alt="menu-icon" className="svg" />
        </div>
      )}

      {showMenu && (
        <div id='video-dropdown' className='col-left dropdown-section'>
          <div onClick={() => history.push(`/videos/${video.id}/edit`)} className='row-space-between'>
            <div className='svg-wrapper'>
              <img src={pencil} alt="edit" className='svg' />
            </div>
            Edit Video
          </div>
          <div onClick={confirmDelete} className='row-space-between'>
            <div className='svg-wrapper'>
              <img src={trash} alt="delete" className='svg' />
            </div>
            Delete Video
          </div>
        </div>
      )}
    </div>

  )
}
