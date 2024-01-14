import React, { useEffect, useState } from 'react'
import { useDispatch } from 'react-redux';
import { clearVideosState, fetchRandomVideos } from '../../store/videos';

import './HomePage.css';
import VideoCard from '../VideoCard/VideoCard';
import LoadingWheel from '../LoadingWheel/LoadingWheel';

export default function HomePage() {
    const dispatch = useDispatch();

    const [videos, setVideos] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [nextPage, setNextPage] = useState(2);

    useEffect(() => {
        (async () => {
            const videoArr = await dispatch(fetchRandomVideos(1))
            setVideos(videoArr);
            setIsLoaded(true);
        })()
        
        return () => dispatch(clearVideosState());
    }, [dispatch]);

    useEffect(() => {
        const scrollingFunction = async () => {
            if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
                window.removeEventListener('scroll', scrollingFunction);
                const newVideos = await dispatch(fetchRandomVideos(nextPage));
                setVideos(prevVideos => [...prevVideos, ...newVideos]);
                setNextPage(prev => prev + 1);
            }
        }

        window.addEventListener('scroll', scrollingFunction);

        return () => {
            window.removeEventListener('scroll', scrollingFunction);
        }
    }, [nextPage, dispatch]);

    return !isLoaded ? <LoadingWheel /> : (
        <div id='home-page' className='col-space-even'>
            <div className='video-row-grid'>
                {videos.map(video => (
                    <VideoCard key={video.id} videoId={video.id} />
                ))}
            </div>

            <LoadingWheel isCentered={false} />
        </div>
    )
}
