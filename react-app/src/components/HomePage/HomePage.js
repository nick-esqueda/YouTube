import React, { useEffect, useState } from 'react'
import { useDispatch } from 'react-redux';
import { fetchHomeVideos } from '../../store/videos';
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './HomePage.css';

export default function HomePage() {
    const dispatch = useDispatch();

    // trading this out so that we don't have to Object.values the useSelector
    // const videos = useSelector(state => state.videos);
    const [videos, setVideos] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [nextPage, setNextPage] = useState(2);

    useEffect(() => {
        (async () => {
            const videoArr = await dispatch(fetchHomeVideos(1))
            console.log(videoArr, '\n\n\n');
            setVideos(videoArr);
            setIsLoaded(true);
        })()
    }, [dispatch]);

    useEffect(() => {
        // TODO try setting a new isLoaded to false then true to display loading spinner when getting next page?
        const scrolling_function = async () => {
            if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
                window.removeEventListener('scroll', scrolling_function);
                const newVideos = await dispatch(fetchHomeVideos(nextPage));
                setVideos(prevVideos => [...prevVideos, ...newVideos]);
                setNextPage(prev => prev + 1);
            }
        }

        window.addEventListener('scroll', scrolling_function);

        return () => {
            window.removeEventListener('scroll', scrolling_function);
        }
    }, [nextPage]);


    return !isLoaded ? null : (
        <div id='home-page' className='col-space-even'>
            <div className='video-row-grid'>
                {videos.map(video => (
                    <div key={video.id} className='video-grid-item col-top'>
                        <div className='thumbnail-wrapper col-top'>
                            <img src={video.thumbnailUrl} alt='thumbnail'
                                className='thumbnail'
                            />
                        </div>

                        <div className='video-thumbnail-details row-left row-top'>
                            <div style={{ width: "36px", minWidth: '36px', height: "36px", marginRight: '12px' }}>
                                <ProfileIcon channel={video.channel} />
                            </div>
                            <div className='col-left'>
                                <h4 className='line-clamp2'>{video.title}</h4>
                                <span className='line-clamp2'>{video.channel.channelName}</span>
                                <span className='line-clamp2'>[# of views] * {video.createdAt}</span>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}
