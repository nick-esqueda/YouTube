import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useLocation } from 'react-router-dom/cjs/react-router-dom'
import { searchVideos } from '../../store/videos';
import VideoCardLarge from '../VideoCardLarge/VideoCardLarge';

import './SearchResultsPage.css';

export default function SearchResultsPage() {
  const dispatch = useDispatch();
  const location = useLocation();

  let searchResults = useSelector(state => state.videos);
  searchResults = Object.values(searchResults);

  const query = new URLSearchParams(location.search).get("q");

  useEffect(() => {
    dispatch(searchVideos(query));
  }, [dispatch, query]);

  // TODO: message when no results, or at bottom of results.
  return (
    <div id='search-results-page'>
      {searchResults.length > 0
        ? (<div className='search-results-container'>
          {searchResults.map(video => <VideoCardLarge key={video.id} videoId={video.id} />)}
        </div>)
        : (<span className='subcount' style={{ margin: '12px', fontSize: '12px' }}>
          We couldn't find any results for "{query}". Please try searching with other keywords.
        </span>)
      }
    </div>
  )
}
