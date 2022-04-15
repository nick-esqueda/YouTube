// ACTION VARIABLES ***************************************
const ADD_VIDEO = 'videos/LOAD_VIDEOS';
const LOAD_VIDEOS = 'videos/LOAD_VIDEOS';
const LOAD_ADDITIONAL_VIDEOS = 'videos/LOAD_ADDITIONAL_VIDEOS';
const REMOVE_VIDEO = 'videos/REMOVE_VIDEO';


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



// THUNK ACTION CREATORS **********************************
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



// REDUCER ************************************************
const videosReducer = (state = {}, action) => {
    
    switch (action.type) {
        
        default:
            return state;
    }
}

export default videosReducer;
