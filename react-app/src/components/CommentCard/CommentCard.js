import React, { useEffect, useRef, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import threeDots from '../../static/icons/three-dots.png';
import pencil from '../../static/icons/pencil.png';
import trash from '../../static/icons/trash.png';
import './CommentCard.css';
import { deleteComment } from '../../store/videos';
import CommentForm from '../CommentForm/CommentForm';

export default function CommentCard({ comment, video }) {
    const dispatch = useDispatch();
    const sessionUser = useSelector(state => state.session.user);
    const editInputRef = useRef();
    const [showDots, setShowDots] = useState(false);
    const [showMenu, setShowMenu] = useState(false);
    const [showEdit, setShowEdit] = useState(false);

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
    
    useEffect(() => editInputRef.current?.focus(), [showEdit]);

    const openMenu = () => {
        if (showMenu) return;
        setShowMenu(true);
    };
    
    const confirmDelete = e => {
        if (window.confirm('Are you sure you would like to delete your comment?')) {
            dispatch(deleteComment(comment.id, video.id));
        }
    }

    
    return (
        <div className='comment-container row-top' onMouseEnter={() => setShowDots(true)} onMouseLeave={() => setShowDots(false)}>
            <div style={{ width: '40px', height: '40px', minWidth: '40px', minHeight: '40px' }}>
                <ProfileIcon channel={comment.channel} />
            </div>

            <div className='comment-body col-left'>
                {showEdit ? (
                    <CommentForm comment={comment} setShowEdit={setShowEdit} editInputRef={editInputRef} />
                ) : (
                    <>
                        <div className='col-left'>
                            <span className='comment-user-handle'>{comment.channel.channelName}</span>
                            <span style={{ color: 'var(--color-gray)' }}>{comment.createdAt}</span>
                        </div>
                        <span className='comment-text'>{comment.content}</span>
                    </>
                )}
            </div>

            {comment.channel.id === sessionUser.id && showDots && (
                <div className='svg-wrapper pointer' onClick={openMenu}>
                    <img src={threeDots} alt="menu-icon" className="svg" />
                </div>
            )}

            {showMenu && (
                <div id='comment-dropdown' className='col-left dropdown-section'>
                    <div onClick={() => setShowEdit(true)} className='row-space-between'>
                        <div className='svg-wrapper'>
                            <img src={pencil} alt="edit" className='svg' />
                        </div>
                        Edit
                    </div>
                    <div onClick={confirmDelete} className='row-space-between'>
                        <div className='svg-wrapper'>
                            <img src={trash} alt="delete" className='svg' />
                        </div>
                        Delete
                    </div>
                </div>
            )}
        </div>
    )
}
