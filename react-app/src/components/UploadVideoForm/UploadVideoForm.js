import React, { useState } from 'react'
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';

import './UploadVideoForm.css';

export default function UploadVideoForm() {
    const history = useHistory();
    const dispatch = useDispatch();
    
    const [title, setTitle] = useState();
    const [description, setDescription] = useState();
    const [videoUrl, setVideoUrl] = useState();
    const [thumbnailUrl, setThumbnailUrl] = useState();
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

	const s3upload = async (file) => {
		if (!file) return console.log('upload a file first');
		const formData = new FormData()

		formData.append('file', file)

		const res = await axios.post("/api/s3/upload/", formData);

		return res.data;
	}

    
    return (
        <div>
            adfasdfasdf
            <div>
                <iframe width="560" height="315"
                    src={`https://youtube-bucket-nick-esqueda.s3.amazonaws.com/lizard-vibing.mp4`}
                    title="YouTube video player"
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                ></iframe>
            </div>
        </div>
    )
}
