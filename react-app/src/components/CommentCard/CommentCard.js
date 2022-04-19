import React from 'react'
import { useDispatch } from 'react-redux';
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './CommentCard.css';

export default function CommentCard({ comment }) {
    const dispatch = useDispatch();

    return (
        <div className='comment-container row-top'>
            <div style={{ width: '40px', height: '40px', minWidth: '40px', minHeight: '40px' }}>
                <ProfileIcon channel={comment.channel} />
            </div>

            <div className='comment-body col-left'>
                <div className='col-left'>
                    <span className='comment-user-handle'>{comment.channel.channelName}</span>
                    <span style={{ color: 'var(--color-gray)' }}>{comment.createdAt}</span>
                </div>
                <span className='comment-text'>{comment.content}</span>
            </div>
        </div>
    )
}
