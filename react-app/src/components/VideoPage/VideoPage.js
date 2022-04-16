import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom'
import { fetchVideo } from '../../store/videos';

import './VideoPage.css';

export default function VideoPage() {
    const { videoId } = useParams();
    const dispatch = useDispatch();

    const video = useSelector(state => state.videos[videoId]);
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        (async () => {
            const video = await dispatch(fetchVideo(videoId));
            console.log(video);
            setIsLoaded(true);
        })()
    }, [dispatch])

    return !isLoaded ? null : (
        <div id='video-page' className='test2'>
            <div className='left'>
                <div className='video-wrapper'>
                    <iframe width="560" height="315"
                        src={`https://www.youtube.com/embed/${video.videoUrl}`}
                        title="YouTube video player"
                        frameBorder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen
                    ></iframe>
                </div>

                <div className='video-info col-left test3'>
                    <h4>{video.title}</h4>
                    <span className='subcount'>[# of views] * {video.createdAt}</span>
                </div>
                
                <div className='video-description test4'>
                    <span>{video.description}</span>
                    
                </div>
            </div>
            
            <div className='right test1'>
                fj adfjaadjajkfjkfd adf
            </div>
        </div>
    )
}
