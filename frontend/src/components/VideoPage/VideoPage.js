import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom/cjs/react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom'
import { deleteVideo, fetchRandomVideos, fetchVideo } from '../../store/videos';
import { fetchVideosComments } from '../../store/comments';
import CommentCard from '../CommentCard/CommentCard';
import CommentForm from '../CommentForm/CommentForm';
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import loadingWheel from '../../static/icons/loading-wheel.gif';
import threeDots from '../../static/icons/three-dots.png';
import pencil from '../../static/icons/pencil.png';
import trash from '../../static/icons/trash.png';
import './VideoPage.css';
import VideoCard from '../VideoCard/VideoCard';
import VideoCardSmall from '../VideoCardSmall/VideoCardSmall';
import SuggestedVideos from './SuggestedVideos';

export default function VideoPage() {
    const { videoId } = useParams();
    const dispatch = useDispatch();
    const history = useHistory();

    const sessionUser = useSelector(state => state.session.user);
    const video = useSelector(state => state.videos[videoId]);
    const videosComments = useSelector(state => state.comments);
    const [randomVideos, setRandomVideos] = useState([]);
    const [showMenu, setShowMenu] = useState(false);
    const [showMore, setShowMore] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        (async () => {
            dispatch(fetchVideosComments(videoId));
            await dispatch(fetchVideo(videoId));
            const randomVideos = await dispatch(fetchRandomVideos(2));
            setRandomVideos(randomVideos);
            setIsLoaded(true);
        })()
    }, [dispatch, videoId]);

    useEffect(() => {
        if (!showMenu) return;

        const closeMenu = () => {
            setShowMenu(false);
        };

        document.addEventListener('click', closeMenu);

        return () => {
            setShowMenu(false);
            document.removeEventListener("click", closeMenu);
        }
    }, [showMenu]);

    const openMenu = () => {
        if (showMenu) return;
        setShowMenu(true);
    };

    const confirmDelete = async e => {
        if (window.confirm('Are you sure you want to delete your video?')) {
            if (window.confirm('Video deletion is permanent and cannot be undone. Do you wish to continue?')) {
                setIsLoaded(false);
                await dispatch(deleteVideo(video.id));
                return history.push('/');
            }
        }
    }

    return !isLoaded ? <img src={loadingWheel} alt='loading-wheel' style={{ width: "50px", left: 'calc(50% - 72px)' }} className='absolute-center' /> : (
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

                    {/* <div className='row-space-between'>
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
                    </div> */}

                    {video.channelId === sessionUser?.id && (
                        <div className='svg-wrapper pointer' onClick={openMenu}>
                            <img src={threeDots} alt="menu-icon" className="svg" />
                        </div>
                    )}

                    {showMenu && (
                        <div id='video-dropdown' className='col-left dropdown-section'>
                            <div onClick={() => history.push(`/videos/${video.id}/edit`)} className='row-space-between'>
                                <div className='svg-wrapper'>
                                    <img src={pencil} alt="edit" className='svg' />
                                </div>
                                Edit Video
                            </div>
                            <div onClick={confirmDelete} className='row-space-between'>
                                <div className='svg-wrapper'>
                                    <img src={trash} alt="delete" className='svg' />
                                </div>
                                Delete Video
                            </div>
                        </div>
                    )}
                </div>


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
                <SuggestedVideos />
            </div>
        </div>
    )
}
