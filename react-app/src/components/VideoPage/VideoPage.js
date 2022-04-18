import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom'
import { fetchVideo } from '../../store/videos';
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './VideoPage.css';

export default function VideoPage() {
    const { videoId } = useParams();
    const dispatch = useDispatch();

    const video = useSelector(state => state.videos[videoId]);
    const [showMore, setShowMore] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        (async () => {
            await dispatch(fetchVideo(videoId));
            setIsLoaded(true);
        })()
    }, [dispatch])

    return !isLoaded ? null : (
        <div id='video-page' className=''>
            <div className='left'>
                <div className='video-wrapper'>
                    <iframe
                        src={video.videoUrl.includes('amazonaws') ? video.videoUrl : `https://www.youtube.com/embed/${video.videoUrl}`}
                        title="YouTube video player"
                        frameBorder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen
                    ></iframe>
                </div>

                <div className='video-info col-left'>
                    <h4>{video.title}</h4>
                    <span className='subcount'>[# of views] * {video.createdAt}</span>
                </div>


                <div className='video-description row-left row-top'>
                    <div style={{ minWidth: "52px", height: "52px", marginRight: '20px' }}>
                        <ProfileIcon channel={video.channel} />
                    </div>


                    <div className='col-left'>
                        <div className='col-space-even full-size channel-and-subs'>
                            <h4>{video.channel.channelName}</h4>
                            <span className='subcount'>[# of subscribers]</span>
                        </div>
                        
                        <p className={showMore ? "show-more" : "show-less"}>{video.description}</p>
                        {!showMore
                            ? <span
                                className='subcount pointer show'
                                onClick={e => setShowMore(true)}
                            >SHOW MORE</span>
                            : <span
                                className='subcount pointer show'
                                onClick={e => setShowMore(false)}
                            >SHOW LESS</span>
                        }
                    </div>
                </div>
            </div>


            {/* <div className='right test1'>
                fj adfjaadjajkfjkfd adf
            </div> */}
        </div>
    )
}
