import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom'
import { fetchVideo } from '../../store/videos';

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
        <div>
            <div>VideoPage - Video ID: {videoId}</div>

            <div className='video-wrapper'>
                <iframe width="560" height="315"
                    src={`https://www.youtube.com/embed/${video.videoUrl}`}
                    title="YouTube video player"
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                ></iframe>
            </div>

            <div className='video-info'>
                <span>{video.title}</span>
                <span>{video.description}</span>
                <img src={video.thumbnailUrl} alt='thumbnail' />
            </div>
        </div>
    )
}
