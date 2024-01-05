import React, { useEffect, useState } from 'react'
import VideoCardSmall from '../VideoCardSmall/VideoCardSmall'
import loadingWheel from '../../static/icons/loading-wheel.gif';
import { useDispatch } from 'react-redux';
import { fetchRandomVideos } from '../../store/videos';

import './VideoPage.css';

export default function SuggestedVideos({ videoId }) {
  const dispatch = useDispatch();

  const [isLoaded, setIsLoaded] = useState(false);
  const [nextPage, setNextPage] = useState(3);
  const [suggestedVideos, setSuggestedVideos] = useState([]);

  useEffect(() => {
    (async () => {
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
      const suggestedVideos = await dispatch(fetchRandomVideos(2));
      setSuggestedVideos(suggestedVideos);
      setIsLoaded(true);
    })()
  }, [dispatch, videoId]);

  useEffect(() => {
    const scrollingFunction = async () => {
      if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        window.removeEventListener('scroll', scrollingFunction);
        const newVideos = await dispatch(fetchRandomVideos(nextPage));
        setSuggestedVideos(prevVideos => [...prevVideos, ...newVideos]);
        setNextPage(prev => prev + 1);
      }
    }

    window.addEventListener('scroll', scrollingFunction);

    return () => {
      window.removeEventListener('scroll', scrollingFunction);
    }
  }, [nextPage, dispatch]);

  return !isLoaded ? null : (
    <>
      <div className='suggested-videos-container col-left'>
        {suggestedVideos.map(video => {
          // the video being viewed should not be in suggested videos list.
          if (video.id === videoId) {
            return null;
          }
          return <VideoCardSmall key={video.id} videoId={video.id} />
        })}
      </div>

      <img src={loadingWheel} alt='loading-wheel' style={{ width: '25px', height: '25px', margin: '25px' }} />
    </>
  )
}
