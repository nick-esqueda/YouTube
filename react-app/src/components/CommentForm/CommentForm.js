import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createComment } from '../../store/videos';
import ProfileIcon from '../ProfileIcon/ProfileIcon';


import './CommentForm.css';

export default function CommentForm({ videoId }) {
    const dispatch = useDispatch();
    const sessionUser = useSelector(state => state.session.user);
    const [content, setContent] = useState('');
    const [showCharCount, setShowCharCount] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);

    useEffect(() => {
        const errors = [];
        if (!content.length) errors.push('!content');
        if (content.length > 255) errors.push('content>255');

        setValidationErrors(errors);
    }, [content]);

    const onSubmit = (e) => {
        e.preventDefault();
        if (validationErrors.length) return;

        const comment = {
            videoId, content
        }

        dispatch(createComment(comment))
            .then(_ => {
                setContent('');
            })
            .catch(async (data) => {
                if (data && data.errors) {
                    setValidationErrors(data.errors);
                }
            });
    }


    return (
        <div id='comment-form-wrapper' className='row-left'>
            <div style={{ minWidth: "40px", height: "40px", marginRight: '20px' }}>
                <ProfileIcon channel={sessionUser} />
            </div>


            <form onSubmit={onSubmit} onFocus={() => setShowCharCount(true)} onBlur={() => setShowCharCount(false)}
                className=''
            >
                <input
                    id='comment-input'
                    name='content'
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    placeholder='Add a comment...'
                    autoComplete='off'
                />

                {showCharCount && (
                    <>
                        <div className='row-space-between'>
                            <button type='button'
                                id='comment-cancel'
                                className='btn'
                            >CANCEL</button>
                            <button type='submit'
                                id='comment-submit'
                                style={{ cursor: validationErrors.length ? 'not-allowed' : 'pointer' }}
                                className='btn btn--blue'
                            >COMMENT</button>
                        </div>

                        <small style={content.length > 255 || content.length === 0 ? { color: 'var(--red)' } : {}}
                        >{content.length}/255</small>
                    </>
                )}
            </form>
        </div>

    )
}
