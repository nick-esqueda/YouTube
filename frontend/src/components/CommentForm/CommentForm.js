import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createComment, editComment } from '../../store/comments';
import ProfileIcon from '../ProfileIcon/ProfileIcon';

import './CommentForm.css';

export default function CommentForm({ videoId, comment, setShowEdit, editInputRef }) {
    const dispatch = useDispatch();
    const sessionUser = useSelector(state => state.session.user);
    const [content, setContent] = useState(comment ? comment.content : '');
    const [showCharCount, setShowCharCount] = useState(comment ? true : false);
    const [validationErrors, setValidationErrors] = useState([]);

    useEffect(() => {
        const errors = [];
        if (!content.length) errors.push('!content');
        if (content.length > 255) errors.push('content>255');

        setValidationErrors(errors);
    }, [content]);

    const onSubmitCreate = (e) => {
        e.preventDefault();
        if (validationErrors.length) return;

        const comment = {
            videoId, content
        }

        dispatch(createComment(comment))
            .then(_ => {
                setContent('');
                setShowCharCount(false);
            })
            .catch(async (data) => {
                if (data && data.errors) {
                    setValidationErrors(data.errors);
                }
            });
    }

    const onSubmitEdit = (e) => {
        e.preventDefault();
        if (validationErrors.length) return;

        const editedComment = {
            ...comment, content
        }

        dispatch(editComment(editedComment))
            .then(_ => {
                setContent('');
                setShowCharCount(false);
                if (comment) setShowEdit(false);
            })
            .catch(async (data) => {
                if (data && data.errors) {
                    setValidationErrors(data.errors);
                }
            });
    }

    const cancelSubmitCreate = (e) => {
        e.preventDefault();
        setContent('');
        setShowCharCount(false);
    }

    const cancelSubmitEdit = (e) => {
        e.preventDefault();
        setContent(comment.content);
        setShowCharCount(false);
        setShowEdit(false);
    }


    return (
        <div id='comment-form-wrapper' className='row-left row-top' style={comment ? { margin: 0 } : {}}>
            {comment ? null : (
                <div style={{ minWidth: "40px", height: "40px", marginRight: '20px' }}>
                    <ProfileIcon channel={sessionUser} />
                </div>
            )}


            <form onSubmit={comment ? onSubmitEdit : onSubmitCreate} onFocus={() => setShowCharCount(true)}
                id='comment-form'
            >
                <input
                    id='comment-input'
                    name='content'
                    placeholder='Add a comment...'
                    autoComplete='off'
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    ref={editInputRef}
                />

                {showCharCount && (
                    <div className='row-space-between'>
                        <small style={content.length > 255 || content.length === 0 ? { color: '#fe3b3b' } : { color: 'var(--gray-light)' }}
                        >{content.length}/255</small>

                        <div className='row-right'>
                            <button type='button'
                                id='comment-cancel'
                                className='btn'
                                onClick={comment ? cancelSubmitEdit : cancelSubmitCreate}
                            >CANCEL</button>

                            <button type='submit'
                                id='comment-submit'
                                style={{ cursor: validationErrors.length ? 'not-allowed' : 'pointer' }}
                                className='btn btn--blue'
                            >{comment ? "SAVE" : "COMMENT"}</button>
                        </div>
                    </div>
                )}
            </form>
        </div>

    )
}
