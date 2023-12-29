import { getTimeElapsed } from "../utils";

// ACTION VARIABLES ***************************************
const ADD_COMMENT = 'comments/ADD_COMMENT';
const LOAD_COMMENTS = 'comments/LOAD_COMMENTS'
const UPDATE_COMMENT = 'comments/UPDATE_COMMENT';
const REMOVE_COMMENT = 'comments/REMOVE_COMMENT';

// ACTION CREATORS ****************************************
const addComment = (comment) => {
    return {
        type: ADD_COMMENT,
        comment
    }
}

const loadComments = (comments) => {
    return {
        type: LOAD_COMMENTS,
        comments
    }
}

const updateComment = (comment) => {
    return {
        type: UPDATE_COMMENT,
        comment
    }
}

const removeComment = (videoId, commentId) => {
    return {
        type: REMOVE_COMMENT,
        videoId,
        commentId
    }
}

// THUNK ACTION CREATORS **********************************
export const fetchVideosComments = videoId => async dispatch => {
    const res = await fetch(`${process.env.REACT_APP_BASE_URL}/api/videos/${videoId}/comments`);

    if (res.ok) {
        const videosComments = await res.json();
        dispatch(loadComments(videosComments));
        return videosComments;
    }
}

export const createComment = comment => async dispatch => {
    const res = await fetch(`${process.env.REACT_APP_BASE_URL}/api/videos/${comment.videoId}/comments/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(comment)
    });

    if (res.ok) {
        const newComment = await res.json();
        dispatch(addComment(newComment));
        return newComment;
    } else {
        const errors = await res.json();
        throw errors;
    }
}

export const editComment = comment => async dispatch => {
    const res = await fetch(`${process.env.REACT_APP_BASE_URL}/api/videos/${comment.videoId}/comments/${comment.id}/`, {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(comment)
    });

    if (res.ok) {
        const editedComment = await res.json();
        dispatch(updateComment(editedComment));
        return editedComment;
    }
}

export const deleteComment = (commentId, videoId) => async dispatch => {
    const res = await fetch(`${process.env.REACT_APP_BASE_URL}/api/videos/${videoId}/comments/${commentId}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (res.ok) {
        const commentId = await res.json();
        dispatch(removeComment(videoId, commentId));
        return { videoId, commentId };
    }
}


// REDUCER ************************************************
const commentsReducer = (state = [], action) => {
    switch (action.type) {
        case ADD_COMMENT: {
            const comment = action.comment;
            comment.createdAt = getTimeElapsed(comment.createdAt);
            return [comment, ...state];
        }
            
        case LOAD_COMMENTS: {
            const comments = action.comments;
            return comments;
        }

        case UPDATE_COMMENT: {
            const updatedComment = action.comment;
            updatedComment.createdAt = getTimeElapsed(updatedComment.createdAt); // TODO: add as new property on backend?
            const newState = [...state];
            const commentIdxInState = newState.findIndex(comment => comment.id === updatedComment.id);
            newState[commentIdxInState] = updatedComment;
            return newState;
        }

        case REMOVE_COMMENT: {
            return state.filter(comment => comment.id !== action.commentId);
        }

        default:
            return state;

    }
}

export default commentsReducer;
