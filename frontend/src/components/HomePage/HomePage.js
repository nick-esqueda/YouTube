import React, { useEffect, useState } from 'react'
import { useDispatch } from 'react-redux';
import { fetchRandomVideos } from '../../store/videos';

import './HomePage.css';
import loadingWheel from '../../static/icons/loading-wheel.gif';
import VideoCard from '../VideoCard/VideoCard';

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

    return !isLoaded ? <img src={loadingWheel} alt='loading-wheel' style={{ width: "50px" }} className='absolute-center' /> : (
        <div id='home-page' className='col-space-even'>
            <div className='video-row-grid'>
                {videos.map(video => (
                    <VideoCard key={video.id} videoId={video.id} />
                ))}
            </div>

            <img src={loadingWheel} alt='loading-wheel' style={{ width: '50px', height: '50px', margin: '10px 0 120px' }} />
        </div>
    )
}
