// ACTION VARIABLES ***************************************
const ADD_VIDEO = 'videos/LOAD_VIDEOS';
const LOAD_VIDEOS = 'posts/LOAD_VIDEOS';
const LOAD_ADDITIONAL_VIDEOS = 'videos/LOAD_ADDITIONAL_VIDEOS';
const REMOVE_VIDEO = 'videos/REMOVE_VIDEO';


// ACTION CREATORS ****************************************
// POSTS
const addVideo = (video) => {
    return {
        type: ADD_VIDEO,
        post
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
        postId
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


// REDUCER ************************************************
const videosReducer = (state = {}, action) => {
    
    switch (action.type) {
        
        default:
            return state;
    }
}

export default videosReducer;
