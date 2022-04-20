import { getTimeElapsed } from "../utils";

// ACTION VARIABLES ***************************************
const ADD_CHANNEL = 'channels/ADD_CHANNEL';


// ACTION CREATORS ****************************************
const addChannel = (channel) => {
    return {
        type: ADD_CHANNEL,
        channel
    }
}


// THUNK ACTION CREATORS **********************************
export const fetchChannel = (channelId) => async dispatch => {
    const res = await fetch(`/api/channels/${channelId}/`);
    
    if (res.ok) {
        const channel = await res.json();
        dispatch(addChannel(channel));
        return channel;
    }
}


// REDUCER ************************************************
const channelsReducer = (state = {}, action) => {
    let newState = { ...state };
    
    switch (action.type) {
        
        case ADD_CHANNEL: {
            action.channel.videos.forEach(video => {
                video.createdAt = getTimeElapsed(video.createdAt);
            })
            
            newState[action.channel.id] = action.channel;
            return newState;
        }
        
        default: {
            return state;
        }
    }
}

export default channelsReducer;
