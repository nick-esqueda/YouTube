import React, { useEffect, useRef, useState } from 'react'
import axios from 'axios';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';

import './VideoForm.css';
import addThumbnail from '../../static/icons/add-thumbnail.png';
import uploadVideo from '../../static/icons/upload-video.png';
import loadingWheel from '../../static/icons/loading-wheel.gif';
import { createVideo, editVideo, fetchVideo } from '../../store/videos';

export default function VideoForm() {
    const { videoId } = useParams();
    const history = useHistory();
    const dispatch = useDispatch();
    const thumbnailInputRef = useRef();
    const videoInputRef = useRef();
    const descriptionWrapperRef = useRef();
    const titleWrapperRef = useRef();
    const descriptionSpanRef = useRef();
    const titleSpanRef = useRef();

    const video = useSelector(state => state.videos[videoId]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [videoUrl, setVideoUrl] = useState('');
    const [thumbnailUrl, setThumbnailUrl] = useState('');
    const [showErrors, setShowErrors] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);

    useEffect(() => {
        const errors = [];
        if (!title) errors.push('Please provide a title for your video');
        if (title.length > 100) errors.push('Title must be shorter than 100 characters');
        if (description.length > 5000) errors.push('Sorry! Descriptions must be shorter than 5000 characters');
        if (!thumbnailUrl.startsWith('https://')) errors.push('Please choose a thumbnail first before uploading');
        if (!videoUrl) errors.push('Please choose a video first before submitting');

        setValidationErrors(errors);
    }, [title, description, videoUrl, thumbnailUrl]);

    useEffect(() => {
        (async () => {
            if (videoId) {
                const video = await dispatch(fetchVideo(videoId));
                setTitle(video.title);
                setDescription(video.description);
                setThumbnailUrl(video.thumbnailUrl);
                setVideoUrl(video.videoUrl);
            }
            setIsLoaded(true);
        })()
    }, [dispatch]);

    const s3Upload = async (file, type) => {
        if (!file) return console.log('upload a file first');
        const formData = new FormData();

        formData.append('file', file);

        if (type === "video") {
            setVideoUrl(loadingWheel);
            const { data: url } = await axios.post("/api/s3/upload/video", formData);
            setVideoUrl(url);
        } else if (type === "image") {
            setThumbnailUrl(loadingWheel);
            const { data: url } = await axios.post("/api/s3/upload/image", formData);
            setThumbnailUrl(url);
        }
    }

    const onSubmit = e => {
        e.preventDefault();

        if (validationErrors.length) return setShowErrors(true);

        if (!video) {
            // FOR VIDEO UPLOAD *******************************
            const video = {
                title, description, videoUrl, thumbnailUrl
            }

            dispatch(createVideo(video))
                .then(async video => {
                    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
                    return history.push(`/watch/${video.id}`);
                })
                .catch(async (data) => {
                    if (data && data.errors) {
                        setValidationErrors(data.errors);
                        setShowErrors(true);
                    }
                });

        } else {
            // FOR VIDEO EDIT **********************************
            const editedVideo = {
                id: video.id, title, description, thumbnailUrl
            }

            dispatch(editVideo(editedVideo))
                .then(async video => {
                    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
                    return history.push(`/watch/${video.id}`);
                })
                .catch(async (data) => {
                    if (data && data.errors) {
                        setValidationErrors(data.errors);
                        setShowErrors(true);
                    }
                });
        }
    }

    const autoGrow = (e) => {
        e.target.style.height = "36px";
        e.target.style.height = (e.target.scrollHeight) + "px";
    }


    return !isLoaded ? null : (
        <div id='upload-page'>
            <form onSubmit={onSubmit} id='video-upload-form' className='row-space-between'>
                <div className='left col-left'>
                    <h2>Details</h2>

                    <div className='input-wrapper col-left' ref={titleWrapperRef} style={(validationErrors.includes('Title must be shorter than 100 characters') || validationErrors.includes('Please provide a title for your video')) && showErrors ? { borderColor: 'var(--red)' } : {}}>
                        <span className='subcount' ref={titleSpanRef} style={(validationErrors.includes('Title must be shorter than 100 characters') || validationErrors.includes('Please provide a title for your video')) && showErrors ? { color: 'var(--red)' } : {}}
                        >Title (required)</span>
                        <textarea type='text'
                            id='title-input'
                            name="title"
                            placeholder="Add a title that describes your video"
                            value={title}
                            onChange={e => setTitle(e.target.value)}
                            onInput={autoGrow}
                            onFocus={e => {
                                titleWrapperRef.current.style.borderColor = 'var(--blue)';
                                titleSpanRef.current.style.color = 'var(--blue)';
                            }}
                            onBlur={e => {
                                titleWrapperRef.current.style.borderColor = ''
                                titleSpanRef.current.style.color = '';
                            }}
                        />
                        <div className='full-size row-right'>
                            <small className='character-count'
                                style={title.length > 100 ? { color: 'red' } : {}}
                            >{title.length}/100</small>
                        </div>
                    </div>

                    <div className='input-wrapper col-left' ref={descriptionWrapperRef} style={validationErrors.includes('Sorry! Descriptions must be shorter than 5000 characters') && showErrors ? { borderColor: 'var(--red)' } : {}}>
                        <span className='subcount' ref={descriptionSpanRef} style={validationErrors.includes('Sorry! Descriptions must be shorter than 5000 characters') && showErrors ? { color: 'var(--red)' } : {}}
                        >Description</span>
                        <textarea
                            type='text'
                            id='description-input'
                            className={validationErrors.includes('Sorry! Descriptions must be shorter than 5000 characters') ? 'red-outline' : ''}
                            placeholder='Tell viewers about your video'
                            name='description'
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                            onInput={autoGrow}
                            onFocus={e => {
                                descriptionWrapperRef.current.style.borderColor = 'var(--blue)';
                                descriptionSpanRef.current.style.color = 'var(--blue)';
                            }}
                            onBlur={e => {
                                descriptionWrapperRef.current.style.borderColor = ''
                                descriptionSpanRef.current.style.color = '';
                            }}
                        ></textarea>
                        <div className='full-size row-right'>
                            <small className='character-count'
                                style={description.length > 5000 ? { color: 'red' } : {}}
                            >{description.length}/5000</small>
                        </div>
                    </div>

                    <div className='col-left'>
                        <h4 style={{ fontWeight: 500, margin: '10px 0' }}>Thumbnail&nbsp;<span className='subcount'>(required)</span></h4>
                        <span className='subcount'>Upload a picture that shows what's in your video. A good thumbnail stands out and draws viewers' attention.</span>

                        <div className="image-preview col-center pointer" onClick={e => thumbnailInputRef.current.click()}>
                            {thumbnailUrl.startsWith('https://') ? (
                                <img
                                    src={thumbnailUrl}
                                    alt="thumbnail-preview"
                                    className=""
                                />
                            ) : (
                                <>
                                    <div className='svg-wrapper' style={{ width: "32px" }}>
                                        <img
                                            src={!thumbnailUrl ? addThumbnail : loadingWheel}
                                            alt="thumbnail-preview"
                                            className={!thumbnailUrl ? "svg" : ""}
                                        />
                                    </div>
                                    <span className='subcount'>{!thumbnailUrl ? "Upload Thumbnail" : "Processing image..."}</span>
                                </>
                            )}
                        </div>

                        <input type="file"
                            accept="image/*"
                            name="artwork"
                            ref={thumbnailInputRef}
                            hidden={true}
                            onChange={e => s3Upload(e.target.files[0], 'image')}
                        />
                    </div>
                </div>

                <div className='right col-space-between'>
                    <div className='video-preview-wrapper' style={validationErrors.includes('Please choose a video first before submitting') && showErrors ? { borderColor: 'var(--red)' } : {}}>
                        {videoUrl.startsWith('https://')
                            ? (
                                <iframe
                                    src={videoUrl ? videoUrl : uploadVideo}
                                    title="YouTube video player"
                                    frameBorder="0"
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                    allowFullScreen
                                    className=''
                                ></iframe>
                            ) : (
                                <div className='pointer' onClick={e => videoInputRef.current.click()}>
                                    <div className='svg-wrapper' style={{ height: "50px" }}>
                                        <img
                                            src={!videoUrl ? uploadVideo : loadingWheel}
                                            alt="thumbnail-preview"
                                            className={!videoUrl ? "svg" : ""}
                                            style={{ width: "40px", height: "40px" }}
                                        />
                                    </div>
                                    <span className='subcount'>{!videoUrl ? "Select Video" : "Processing video..."}</span>
                                </div>
                            )}
                    </div>

                    <div className='row-space-between' style={video ? { visibility: 'hidden' } : { width: "100%" }}>
                        <div className='col-left'>
                            <h4 style={{ fontWeight: 500, margin: '10px 0' }}>Choose a video file to upload</h4>
                            <span className='subcount'>Your video won't be posted just yet.</span>
                        </div>

                        <button
                            type="button"
                            className="btn btn--blue"
                            onClick={e => videoInputRef.current.click()}
                        >
                            {!videoUrl
                                ? "SELECT FILE"
                                : "CHANGE FILE"
                            }
                        </button>

                        <input type="file"
                            accept=".mp4, .mov, .wmv"
                            name="video"
                            ref={videoInputRef}
                            hidden={true}
                            onChange={e => {
                                if (e.target.files[0].size < 150 * 1024 ** 2) {
                                    s3Upload(e.target.files[0], 'video');
                                } else {
                                    e.target.value = null;
                                    window.alert('Oops, your file is too big! Please upload a video no larger than 150MB.');
                                }
                            }}
                        />
                    </div>

                    <div className='error-container col-right col-bottom'>
                        {showErrors && validationErrors.map(err => (
                            <div key={err} className='right-align'>{err}</div>
                        ))}
                    </div>

                    <div style={{ margin: '12px 0' }}>
                        <button type='submit' className='btn btn--blue-outline'>{video ? "SUBMIT CHANGES" : "UPLOAD VIDEO"}</button>
                    </div>
                </div>

            </form >


        </div >
    )
}
