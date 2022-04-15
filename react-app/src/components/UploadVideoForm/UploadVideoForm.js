import React from 'react'

import './UploadVideoForm.css';

export default function UploadVideoForm() {
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
