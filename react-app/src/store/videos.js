import { normalizeOneLevel } from "./utils";

// ACTION VARIABLES ***************************************
const ADD_VIDEO = 'videos/ADD_VIDEO';
const LOAD_VIDEOS = 'videos/LOAD_VIDEOS';
const LOAD_ADDITIONAL_VIDEOS = 'videos/LOAD_ADDITIONAL_VIDEOS';
const REMOVE_VIDEO = 'videos/REMOVE_VIDEO';

const ADD_COMMENT = 'comments/ADD_COMMENT';
const UPDATE_COMMENT = 'comments/UPDATE_COMMENT';
const REMOVE_COMMENT = 'comments/REMOVE_COMMENT';


// ACTION CREATORS ****************************************
// VIDEOS
const addVideo = (video) => {
    return {
        type: ADD_VIDEO,
        video
    }
}

const loadVideos = (videos) => {
    return {
        type: LOAD_VIDEOS,
        videos
    }
}

const loadAdditionalVideos = (videos) => {
    return {
        type: LOAD_ADDITIONAL_VIDEOS,
        videos
    }
}

const removeVideo = (videoId) => {
    return {
        type: REMOVE_VIDEO,
        videoId
    }
}

// COMMENTS
const addComment = (comment) => {
    return {
        type: ADD_COMMENT,
        comment
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
export const fetchVideo = (videoId) => async dispatch => {
    const res = await fetch(`/api/videos/${videoId}`);

    if (res.ok) {
        const video = await res.json();
        dispatch(addVideo(video));
        return video;
    }
}

export const fetchHomeVideos = (pageNum = 1) => async dispatch => {
    const res = await fetch(`/api/videos/pages/${pageNum}/`);

    if (res.ok) {
        const videos = await res.json();
        if (pageNum === 1) dispatch(loadVideos(videos));
        else dispatch(loadAdditionalVideos(videos));
        return videos;
    }
}

export const fetchChannelVideos = (channelId, pageNum = 1) => async dispatch => {
    const res = await fetch(`/api/channels/videos/${channelId}/pages/${pageNum}/`);

    if (res.ok) {
        const videos = await res.json();
        if (pageNum === 1) dispatch(loadVideos(videos));
        else dispatch(loadAdditionalVideos(videos));
        return videos;
    }
}

export const createVideo = video => async dispatch => {
    const res = await fetch('/api/videos/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(video)
    });

    if (res.ok) {
        const newVideo = await res.json();
        dispatch(addVideo(newVideo));
        return newVideo;
    } else {
        const errors = await res.json();
        throw errors
    }
}

export const editVideo = video => async dispatch => {
    const res = await fetch(`/api/videos/${video.id}/`, {
        method: "PATCH",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(video)
    });

    if (res.ok) {
        const editedVideo = await res.json();
        dispatch(addVideo(editedVideo));
        return editedVideo;
    }
}

export const deleteVideo = (videoId) => async dispatch => {
    const res = await fetch(`/api/videos/${videoId}/`, {
        method: 'DELETE',
    });

    if (res.ok) {
        const data = await res.json();
        // if delete is authorized, data will be an integer (videoId)
        if (data.notAuthorized === undefined) {
            dispatch(removeVideo(videoId));
            return videoId;
        } else {
            console.error(data);
        }
    }
}

// COMMENTS ///////////////////
export const createComment = comment => async dispatch => {
    const res = await fetch(`/api/videos/${comment.videoId}/comments/`, {
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
    }
}

export const editComment = comment => async dispatch => {
    const res = await fetch(`/api/videos/${comment.videoId}/comments/${comment.id}/`, {
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
    const res = await fetch(`/api/videos/${videoId}/comments/${commentId}/`, {
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
const videosReducer = (state = {}, action) => {
    let newState = { ...state }

    switch (action.type) {

        case LOAD_VIDEOS: {
            return {
                ...normalizeOneLevel(action.videos)
            }
        }

        case LOAD_ADDITIONAL_VIDEOS: {
            return {
                ...state,
                ...normalizeOneLevel(action.videos)
            }
        }

        case ADD_VIDEO: {
            const dateParts = action.video.createdAt.split(' ');
            action.video.createdAt = `${dateParts[2]} ${dateParts[1]}, ${dateParts[3]}`;
            newState[action.video.id] = action.video
            return newState;
        }

        case REMOVE_VIDEO: {
            delete newState[action.videoId];
            return newState;
        }

        // COMMENTS //////////////////////////
        case ADD_COMMENT: {
            const videoId = action.comment.videoId;
            return {
                ...state,
                [videoId]: {
                    ...state[videoId],
                    comments: [action.comment, ...state[videoId].comments]
                }
            }
        }

        case UPDATE_COMMENT: {
            const commentId = action.comment.id;
            const newCommentsArray = [...state[commentId].comments];
            const commentIndex = newCommentsArray.findIndex(comment => comment.id === commentId);
            newCommentsArray[commentIndex] = action.comment;

            return {
                ...state,
                [action.comment.videoId]: {
                    ...state[action.comment.videoId],
                    comments: newCommentsArray
                }
            }
        }

        case REMOVE_COMMENT: {
            const arrayWithoutComment = state[action.videoId].comments.filter(comment => comment.id !== action.commentId);
            return {
                ...state,
                [action.videoId]: {
                    ...state[action.videoId],
                    comments: arrayWithoutComment
                }
            }
        }

        default:
            return state;

    }
}

export default videosReducer;
