import { getTimeElapsed, sortByCreatedAt } from "../utils";
import { customFetch } from "../utils";

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
    const res = await customFetch(`/api/channels/${channelId}/`);
    
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
            const channel = action.channel;
            const dateParts = channel.createdAt.split(' ');
            channel.createdAt = `${dateParts[2]} ${dateParts[1]}, ${dateParts[3]}`;
            newState[channel.id] = channel;
            return newState;
        }
        
        default: {
            return state;
        }
    }
}

export default channelsReducer;
