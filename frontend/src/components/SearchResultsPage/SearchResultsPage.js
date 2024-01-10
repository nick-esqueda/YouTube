import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useLocation } from 'react-router-dom/cjs/react-router-dom'
import { clearVideosState, searchVideos } from '../../store/videos';
import VideoCardLarge from '../VideoCardLarge/VideoCardLarge';
import loadingWheel from '../../static/icons/loading-wheel.gif';

import './SearchResultsPage.css';

export default function SearchResultsPage() {
  const dispatch = useDispatch();
  const location = useLocation();
  const query = new URLSearchParams(location.search).get("q");

  const [isLoaded, setIsLoaded] = useState(false);
  let searchResults = useSelector(state => state.videos);
  searchResults = Object.values(searchResults);

  useEffect(() => {
    setIsLoaded(false);
    dispatch(searchVideos(query))
      .then(() => setIsLoaded(true));

    return () => dispatch(clearVideosState());
  }, [dispatch, query]);

  const renderedSearchResults = searchResults.map(video => (
    <VideoCardLarge key={video.id} videoId={video.id} />
  ));

  const noResultsMessage = (
    <span className='subcount' style={{ margin: '12px', fontSize: '12px' }}>
      We couldn't find any results for "{query}". Please try searching with other keywords.
    </span>
  );

  return !isLoaded ? <img src={loadingWheel} alt='loading-wheel' style={{ width: "30px" }} className='absolute-center' /> : (
    <div id='search-results-page'>
      {searchResults.length > 0
        ? <div className='search-results-container'>{renderedSearchResults}</div>
        : noResultsMessage}
    </div>
  )
}
