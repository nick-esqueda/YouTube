import React, { useEffect, useRef, useState } from 'react'
import axios from 'axios';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';

import './UploadVideoForm.css';

export default function UploadVideoForm() {
    const history = useHistory();
    const dispatch = useDispatch();
    const thumbnailInputRef = useRef();

    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [videoUrl, setVideoUrl] = useState('');
    const [thumbnailUrl, setThumbnailUrl] = useState(''); // can put a default image before image upload here
    const [showErrors, setShowErrors] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);

    useEffect(() => {
        const errors = [];
        if (title.length > 100) errors.push('Title must be less than 100 characters');
        if (!title) errors.push('Please provide a title for your video.');
        if (description.length > 5000) errors.push('Sorry! Descriptions must be shorter than 5000 characters.')
        if (!thumbnailUrl) errors.push('Please choose a thumbnail first before uploading.')
        if (!videoUrl) errors.push('Please upload a video first before submitting.')
        setValidationErrors(errors);
    }, [title, description, videoUrl, thumbnailUrl]);

    const s3Upload = async (file, type) => {
        if (!file) return console.log('upload a file first');
        const formData = new FormData()

        formData.append('file', file)

        if (type === "video") {
            const { data: url } = await axios.post("/api/s3/upload/video", formData);
            setVideoUrl(url);
        } else if (type === "image") {
            const { data: url } = await axios.post("/api/s3/upload/image", formData);
            setThumbnailUrl(url);
        }
    }

    
    return (
        <div>
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


            <form>
                <div className="image_preview">
                    <img
                        src={thumbnailUrl}
                        alt="thumbnail-preview"
                        className=""
                    >
                    </img>
                    <button
                        type="button"
                        className="btn"
                        style={{ width: '150px' }}
                        onClick={e => thumbnailInputRef.current.click()}
                    >
                        upload image
                    </button>

                    <input type="file"
                        accept=".jpg, .jpeg, .png"
                        name="artwork"
                        ref={thumbnailInputRef}
                        hidden={true}
                        onChange={e => s3Upload(e.target.files[0], 'image')}
                    />
                </div>

                <div id='video-upload'>
                    UPLOAD VIDEO HERE
                    <input type="file"
                        accept=".mp4, .mov, .wmv"
                        name="video"
                        onChange={e => s3Upload(e.target.files[0], 'video')}
                    />
                </div>
            </form>
        </div>
    )
}
