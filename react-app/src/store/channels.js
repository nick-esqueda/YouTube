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

export const editChannel = (channel) => async dispatch => {
    const res = await fetch(`/api/channels/${channel.id}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(channel),
    })
    
    if (res.ok) {
        const editedChannel = await res.json();
        dispatch(addChannel(editedChannel));
        return editedChannel;
    } else {
        const errors = await res.json();
        throw errors;
    }
}


// REDUCER ************************************************
const channelsReducer = (state = {}, action) => {
    let newState = { ...state };
    
    switch (action.type) {
        
        case ADD_CHANNEL: {
            const dateParts = action.channel.createdAt.split(' ');
            action.channel.createdAt = `${dateParts[2]} ${dateParts[1]}, ${dateParts[3]}`;
            
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
