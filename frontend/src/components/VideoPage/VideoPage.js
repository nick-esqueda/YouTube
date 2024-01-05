import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom'
import { fetchVideo } from '../../store/videos';
import { fetchVideosComments } from '../../store/comments';
import CommentCard from '../CommentCard/CommentCard';
import CommentForm from '../CommentForm/CommentForm';
import ProfileIcon from '../ProfileIcon/ProfileIcon';
import SuggestedVideos from './SuggestedVideos';

import loadingWheel from '../../static/icons/loading-wheel.gif';
import './VideoPage.css';
import VideoInfo from './VideoInfo';

export default function VideoPage() {
    const { videoId } = useParams();
    const dispatch = useDispatch();

    const sessionUser = useSelector(state => state.session.user);
    const video = useSelector(state => state.videos[videoId]);
    const videosComments = useSelector(state => state.comments);
    const [showMore, setShowMore] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        (async () => {
            dispatch(fetchVideosComments(videoId));
            await dispatch(fetchVideo(videoId));
            setIsLoaded(true);
        })()
    }, [dispatch, videoId]);

    return !isLoaded ? <img src={loadingWheel} alt='loading-wheel' style={{ width: "30px", left: 'calc(50% - 72px)' }} className='absolute-center' /> : (
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

                <VideoInfo />

                <div className='video-description row-left row-top'>
                    <div style={{ minWidth: "52px", height: "52px", marginRight: '20px' }}>
                        <ProfileIcon channel={video.channel} />
                    </div>


                    <div className='col-left'>
                        <div className='col-space-even full-size channel-and-subs'>
                            <h4>{video.channel.channelName}</h4>
                            <span className='subcount' style={{ visibility: 'hidden' }}>[# of subscribers]</span>
                        </div>

                        <p className={showMore ? "show-more" : "show-less"}>{video.description}</p>
                        {!showMore
                            ? <span
                                className='subcount pointer show'
                                style={!video.description ? { display: 'none' } : {}}
                                onClick={e => setShowMore(true)}
                            >SHOW MORE</span>
                            : <span
                                className='subcount pointer show'
                                style={!video.description ? { display: 'none' } : {}}
                                onClick={e => setShowMore(false)}
                            >SHOW LESS</span>
                        }
                    </div>
                </div>


                <div id='comments-section' className='full-size col-left'>
                    {videosComments.length} comments

                    {sessionUser && (<CommentForm videoId={video.id} />)}

                    {videosComments.map(comment => (
                        <CommentCard key={comment.id} comment={comment} video={video} />
                    ))}
                </div>

            </div>

            <div className='right left-align'>
                <SuggestedVideos videoId={videoId} />
            </div>
        </div>
    )
}
