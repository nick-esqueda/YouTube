import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom'
import { fetchVideo } from '../../store/videos';

import './VideoPage.css';

export default function VideoPage() {
    const { videoId } = useParams();
    const dispatch = useDispatch();

    const video = useSelector(state => state.videos[videoId]);
    const [showMore, setShowMore] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        (async () => {
            const video = await dispatch(fetchVideo(videoId));
            console.log(video);
            setIsLoaded(true);
        })()
    }, [dispatch])

    return !isLoaded ? null : (
        <div id='video-page' className=''>
            <div className='left'>
                <div className='video-wrapper'>
                    <iframe
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

                <div className='video-description col-left test4'>
                    <p className={showMore ? "show-more" : "show-less"}>{video.description}</p>
                    {!showMore
                        ? <span
                            className='subcount pointer'
                            onClick={e => setShowMore(true)}
                        >SHOW MORE</span>
                        : <span
                            className='subcount pointer'
                            onClick={e => setShowMore(false)}
                        >SHOW LESS</span>
                    }
                </div>
            </div>

            <div className='right test1'>
                fj adfjaadjajkfjkfd adf
            </div>
        </div>
    )
}
