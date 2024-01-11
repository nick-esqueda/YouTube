import { customFetch } from "../utils";
import { createNormalizedState, updateNormalizedState } from "./utils";

// ACTION VARIABLES ***************************************
const ADD_VIDEO = 'videos/ADD_VIDEO';
const LOAD_VIDEOS = 'videos/LOAD_VIDEOS';
const LOAD_ADDITIONAL_VIDEOS = 'videos/LOAD_ADDITIONAL_VIDEOS';
const UPDATE_VIDEO = 'videos/UPDATE_VIDEO';
const REMOVE_VIDEO = 'videos/REMOVE_VIDEO';
const CLEAR_VIDEOS = 'videos/CLEAR_VIDEOS';

// ACTION CREATORS ****************************************
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

const updateVideo = (video) => {
    return {
        type: UPDATE_VIDEO,
        video
    }
}

const removeVideo = (videoId) => {
    return {
        type: REMOVE_VIDEO,
        videoId
    }
}

export const clearVideosState = () => {
    return {
        type: CLEAR_VIDEOS
    }
}

// THUNK ACTION CREATORS **********************************
export const fetchVideo = (videoId) => async dispatch => {
    const res = await customFetch(`/api/videos/${videoId}/`);

    if (res.ok) {
        const video = await res.json();
        dispatch(addVideo(video));
        return video;
    }
}

export const fetchRandomVideos = (pageNum = 1) => async dispatch => {
    const res = await customFetch(`/api/videos/pages/${pageNum}/`);

    if (res.ok) {
        const videos = await res.json();
        if (pageNum === 1) dispatch(loadVideos(videos));
        else dispatch(loadAdditionalVideos(videos));
        return videos;
    }
}

export const fetchChannelsVideos = (channelId, pageNum = 1) => async dispatch => {
    const res = await customFetch(`/api/channels/${channelId}/videos/pages/${pageNum}/`);

    if (res.ok) {
        const videos = await res.json();
        if (pageNum === 1) dispatch(loadVideos(videos));
        else dispatch(loadAdditionalVideos(videos));
        return videos;
    }
}

export const createVideo = video => async dispatch => {
    const res = await customFetch(`/api/videos/`, {
        method: 'POST',
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
    const res = await customFetch(`/api/videos/${video.id}/`, {
        method: "PATCH",
        body: JSON.stringify(video)
    });

    if (res.ok) {
        const editedVideo = await res.json();
        dispatch(updateVideo(editedVideo));
        return editedVideo;
    }
}

export const deleteVideo = (videoId) => async dispatch => {
    const res = await customFetch(`/api/videos/${videoId}/`, {
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

export const searchVideos = (query) => async (dispatch) => {
    const res = await fetch(`${process.env.REACT_APP_BASE_URL}/api/search?` 
        + new URLSearchParams({query}));
    
    if (res.ok) {
        const videos = await res.json();
        dispatch(loadVideos(videos));
        return videos;
    }
}


// REDUCER ************************************************
const defaultState = {
    idList: [],
    entities: {},
}
const videosReducer = (state = defaultState, action) => {
    switch (action.type) {
        case LOAD_VIDEOS: {
            return createNormalizedState(action.videos);
        }

        case LOAD_ADDITIONAL_VIDEOS: {
            return updateNormalizedState(action.videos, state);
        }

        case ADD_VIDEO: {
            const video = action.video;
            const dateParts = video.createdAt.split(' ');
            video.createdAt = `${dateParts[2]} ${dateParts[1]}, ${dateParts[3]}`;

            return {
                idList: [video.id, ...state.idList],
                entities: {
                    ...state.entities,
                    [video.id]: video
                }
            }
        }

        // TODO: TEST UPDATE VIDEO
        case UPDATE_VIDEO: {
            const video = action.video;
            const dateParts = video.createdAt.split(' ');
            video.createdAt = `${dateParts[2]} ${dateParts[1]}, ${dateParts[3]}`;

            return {
                idList: [...state.idList],
                entities: {
                    ...state.entities,
                    [video.id]: video
                }
            }
        }

        case REMOVE_VIDEO: {
            const videoId = action.videoId;
            const newIdList = state.idList.filter(id => id !== videoId);
            const newEntities = {...state.entities};
            delete newEntities[videoId];

            return {
                idList: newIdList,
                entities: newEntities
            }
        }

        case CLEAR_VIDEOS: {
            return {
                idList: [],
                entities: {}
            };
        }

        default:
            return state;

    }
}

export default videosReducer;
