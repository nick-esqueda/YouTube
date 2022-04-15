import React, { useEffect, useState } from 'react'
import { useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom'
import { fetchVideo } from '../../store/videos';

export default function VideoPage() {
    const { videoId } = useParams();
    const dispatch = useDispatch();
    
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        (async () => {
            await dispatch(fetchVideo(videoId));
            setIsLoaded(true);
        })()
    }, [dispatch])
    
    return (
        <div>VideoPage - Video ID: {videoId}</div>
    )
}
