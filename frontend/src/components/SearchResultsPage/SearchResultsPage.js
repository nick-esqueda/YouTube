import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useLocation } from 'react-router-dom/cjs/react-router-dom'
import { clearVideosState, searchVideos } from '../../store/videos';
import loadingWheel from '../../static/icons/loading-wheel.gif';

import './SearchResultsPage.css';
import VideoCard from '../VideoCard/VideoCard';

export default function SearchResultsPage() {
  const dispatch = useDispatch();
  const location = useLocation();
  const query = new URLSearchParams(location.search).get("q");

  // must use isLoaded to prevent showing noResultsMessage before API response.
  const [isLoaded, setIsLoaded] = useState(false);
  const searchResultsIdList = useSelector(state => state.videos.idList);

  useEffect(() => {
    setIsLoaded(false);
    dispatch(searchVideos(query))
      .then(() => setIsLoaded(true));

    return () => dispatch(clearVideosState());
  }, [dispatch, query]);

  const renderedSearchResults = searchResultsIdList?.map(videoId => (
    <VideoCard key={videoId} videoId={videoId}
      videoDetailsStyle={'large'} isVerticalOrientation={false} />
  ));

  const noResultsMessage = (
    <span className='subcount' style={{ margin: '12px', fontSize: '12px' }}>
      We couldn't find any results for "{query}". Please try searching with other keywords.
    </span>
  );

  return !isLoaded ? <img src={loadingWheel} alt='loading-wheel' style={{ width: "30px" }} className='absolute-center' /> : (
    <div id='search-results-page'>
      {searchResultsIdList.length > 0
        ? <div className='search-results-container'>{renderedSearchResults}</div>
        : noResultsMessage}
    </div>
  )
}
