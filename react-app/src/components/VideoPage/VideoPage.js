import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom'
import { deleteVideo, fetchVideo } from '../../store/videos';
import CommentCard from '../CommentCard/CommentCard';
import CommentForm from '../CommentForm/CommentForm';
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './VideoPage.css';

export default function VideoPage() {
    const { videoId } = useParams();
    const dispatch = useDispatch();
    const history = useHistory();

    const sessionUser = useSelector(state => state.session.user);
    const video = useSelector(state => state.videos[videoId]);
    const [showMore, setShowMore] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        (async () => {
            await dispatch(fetchVideo(videoId));
            setIsLoaded(true);
        })()
    }, [dispatch])

    const confirmDelete = async e => {
		if (window.confirm('Are you sure you want to delete your video?')) {
            if (window.confirm('Video deletion is permanent and cannot be undone. Do you wish to continue?')) {
                setIsLoaded(false);
                await dispatch(deleteVideo(video.id));
                return history.push('/');
            }
		}
	}
    
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

                <div className='video-info row-space-between'>
                    <div className='col-left'>
                        <h4>{video.title}</h4>
                        <span className='subcount'>{video.createdAt}</span>
                    </div>
                    <div className='row-space-between'>
                        {sessionUser.id !== video.channel.id ? null : (
                            <>
                                <button
                                    className='btn btn--blue-outline'
                                    onClick={e => history.push(`/videos/${video.id}/edit`)}
                                >edit</button>
                                <button
                                    className='btn btn--red-outline'
                                    onClick={confirmDelete}
                                >delete</button>
                            </>
                        )}
                    </div>
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
                
                
                <div id='comments-section' className='full-size col-left'>
                    <CommentForm videoId={video.id} />
                    
                    {video.comments.map(comment => (
                        <CommentCard key={comment.id} comment={comment} video={video} />
                    ))}
                </div>
                
            </div>

        </div>
    )
}
