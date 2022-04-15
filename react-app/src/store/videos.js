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

// const loadVideos = (videos) => {
//     return {
//         type: LOAD_VIDEOS,
//         videos
//     }
// }

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



// REDUCER ************************************************
const videosReducer = (state = {}, action) => {
    
    switch (action.type) {
        
        default:
            return state;
    }
}

export default videosReducer;
