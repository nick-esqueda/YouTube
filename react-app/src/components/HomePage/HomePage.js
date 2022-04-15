import React, { useEffect, useState } from 'react'
import { useDispatch } from 'react-redux';
import { fetchHomeVideos } from '../../store/videos';

import './HomePage.css';

export default function HomePage() {
    const dispatch = useDispatch();

    // trading this out so that we don't have to Object.values the useSelector
    // const videos = useSelector(state => state.videos);
    const [videos, setVideos] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [pageNum, setPageNum] = useState(2);

    useEffect(() => {
        (async () => {
            const videoArr = await dispatch(fetchHomeVideos(1))
            console.log(videoArr, '\n\n\n');
            setVideos(videoArr);
            setIsLoaded(true);
        })()
    }, [dispatch]);

    useEffect(() => {
        // try setting a new isLoaded to false then true to display loading spinner when getting next page?

    }, [pageNum])

    return !isLoaded ? null : (
        <div id='home-page' className='test1 col-space-even'>
            <div className='video-row-grid test2'>
                {videos.map(video => (
                    <div key={video.id} className='video-grid-item-container'>
                        <img src={video.thumbnailUrl} alt='thumbnail'
                            className='thumbnail'
                        />
                    </div>

                ))}
            </div>
        </div>
    )
}
