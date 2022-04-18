import React, { useEffect, useState, useRef } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom'
import { editVideo, fetchVideo } from '../../store/videos';
import axios from 'axios';

import './EditVideoPage.css';

export default function EditVideoPage() {
    const { videoId } = useParams();
    const dispatch = useDispatch();
    const history = useHistory();
    const thumbnailInputRef = useRef();

    const video = useSelector(state => state.videos[videoId]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [thumbnailUrl, setThumbnailUrl] = useState('');
    const [showErrors, setShowErrors] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);

    useEffect(() => {
        (async () => {
            const video = await dispatch(fetchVideo(videoId));
            setTitle(video.title);
            setDescription(video.description);
            setThumbnailUrl(video.thumbnailUrl);
            setIsLoaded(true);
        })()
    }, [dispatch])

    useEffect(() => {
        const errors = [];
        if (title.length > 100) errors.push('Title must be shorter than 100 characters');
        if (!title) errors.push('Please provide a title for your video.');
        if (description.length > 5000) errors.push('Sorry! Descriptions must be shorter than 5000 characters')
        if (!thumbnailUrl) errors.push('Please choose a thumbnail first before uploading.')
        setValidationErrors(errors);
        if (errors.length) setShowErrors(true);
        else setShowErrors(false);
    }, [title, description, thumbnailUrl]);

    const s3Upload = async (file, type) => {
        if (!file) return console.log('upload a file first');
        const formData = new FormData()

        formData.append('file', file)

        const { data: url } = await axios.post("/api/s3/upload/image", formData);
        setThumbnailUrl(url);
    }

    const onSubmit = e => {
        e.preventDefault();

        if (validationErrors.length) return setShowErrors(true);

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




    return !isLoaded ? null : (
        <div id='edit-page'>
            <div>
                <iframe width="560" height="315"
                    src={video.videoUrl}
                    title="YouTube video player"
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                    className='test1 video-preview'
                ></iframe>
            </div>

            <div className="image-preview">
                <img
                    src={thumbnailUrl}
                    alt="thumbnail-preview"
                    className=""
                />
            </div>


            <form onSubmit={onSubmit} id='video-upload-form'>
                <div>
                    <button
                        type="button"
                        className="btn"
                        style={{ width: '150px' }}
                        onClick={e => thumbnailInputRef.current.click()}
                    >
                        choose new thumbnail
                    </button>
                </div>

                <input type="file"
                    accept="image/*"
                    name="artwork"
                    ref={thumbnailInputRef}
                    hidden={true}
                    onChange={e => s3Upload(e.target.files[0], 'image')}
                />


                <div>
                    <input type='text'
                        id='title-input'
                        name="title"
                        className={validationErrors.includes('Title must be shorter than 100 characters') ? 'red-outline' : ''}
                        placeholder="Add a title that describes your video."
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                    />
                    <small className='character-count'
                        style={title.length > 100 ? { color: 'red' } : {}}
                    >{title.length}/100</small>
                </div>


                <div>
                    <textarea
                        type='text'
                        id='description-input'
                        className={validationErrors.includes('Sorry! Descriptions must be shorter than 5000 characters') ? 'red-outline' : ''}
                        rows={4}
                        placeholder='Tell viewers about your video'
                        name='description'
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                    ></textarea>
                    <small className='character-count'
                        style={description.length > 255 ? { color: 'red' } : {}}
                    >{description.length}/5000</small>
                </div>

                <div>
                    <button type='button' 
                        className='btn' 
                        onClick={e => history.push(`/watch/${video.id}`)}
                    >Cancel Changes</button>
                    <button type='submit' className='btn btn--blue-outline'>Submit</button>
                </div>
            </form>

            {showErrors && (
                <div className='error-container'>
                    {validationErrors.map(err => (
                        <div key={err}>{err}</div>
                    ))}
                </div>
            )}
        </div>
    )
}
