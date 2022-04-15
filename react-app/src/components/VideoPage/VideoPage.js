import React from 'react'
import { useParams } from 'react-router-dom'

export default function VideoPage() {
    const { videoId } = useParams();

    return (
        <div>VideoPage - Video ID: {videoId}</div>
    )
}
