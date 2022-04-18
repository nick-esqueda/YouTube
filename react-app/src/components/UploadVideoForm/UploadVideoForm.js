import React, { useEffect, useRef, useState } from 'react'
import axios from 'axios';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';

import './UploadVideoForm.css';
import { createVideo } from '../../store/videos';

export default function UploadVideoForm() {
    const history = useHistory();
    const dispatch = useDispatch();
    const thumbnailInputRef = useRef();

    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [videoUrl, setVideoUrl] = useState('');
    const [thumbnailImageUrl, setThumbnailImageUrl] = useState(''); // can put a default image before image upload here
    const [showErrors, setShowErrors] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);

    useEffect(() => {
        const errors = [];
        if (title.length > 100) errors.push('Title must be shorter than 100 characters');
        if (!title) errors.push('Please provide a title for your video.');
        if (description.length > 5000) errors.push('Sorry! Descriptions must be shorter than 5000 characters')
        if (!thumbnailImageUrl) errors.push('Please choose a thumbnail first before uploading.')
        if (!videoUrl) errors.push('Please upload a video first before submitting.')
        setValidationErrors(errors);
        if (errors.length) setShowErrors(true);
        else setShowErrors(false);
    }, [title, description, videoUrl, thumbnailImageUrl]);

    const s3Upload = async (file, type) => {
        if (!file) return console.log('upload a file first');
        const formData = new FormData()

        formData.append('file', file)

        if (type === "video") {
            const { data: url } = await axios.post("/api/s3/upload/video", formData);
            setVideoUrl(url);
        } else if (type === "image") {
            const { data: url } = await axios.post("/api/s3/upload/image", formData);
            setThumbnailImageUrl(url);
        }
    }

    const onSubmit = e => {
        e.preventDefault();

        if (validationErrors.length) return setShowErrors(true);

        const video = {
            title, description, videoUrl, thumbnailImageUrl
        }

        dispatch(createVideo(video))
            .then(async video => {
                // if (video.errors !== undefined) throw 'aksjdfkj'
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


    return (
        <div id='upload-page'>
            <div>
                <iframe width="560" height="315"
                    src={videoUrl}
                    title="YouTube video player"
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                    className='test1 video-preview'
                ></iframe>
            </div>

            {thumbnailImageUrl && (
                <div className="image-preview">
                    <img
                        src={thumbnailImageUrl}
                        alt="thumbnail-preview"
                        className=""
                    />
                </div>
            )}


            <form onSubmit={onSubmit} id='video-upload-form'>
                <div>
                    <button
                        type="button"
                        className="btn"
                        style={{ width: '150px' }}
                        onClick={e => thumbnailInputRef.current.click()}
                    >
                        upload image
                    </button>
                </div>

                <input type="file"
                    accept="image/*"
                    name="artwork"
                    ref={thumbnailInputRef}
                    hidden={true}
                    onChange={e => s3Upload(e.target.files[0], 'image')}
                />


                <div id='video-upload'>
                    UPLOAD VIDEO HERE
                    <input type="file"
                        accept=".mp4, .mov, .wmv"
                        name="video"
                        onChange={e => s3Upload(e.target.files[0], 'video')}
                    />
                </div>


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
