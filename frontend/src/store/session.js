import { customFetch } from "../utils";

// ACTION VARIABLES ***************************************
const SET_USER = 'session/SET_USER';
const REMOVE_USER = 'session/REMOVE_USER';

// ACTION CREATORS ****************************************
const setUser = (user) => ({
  type: SET_USER,
  payload: user
});

const removeUser = () => ({
  type: REMOVE_USER,
})

// THUNK ACTION CREATORS **********************************
export const authenticate = () => async (dispatch) => {
  const response = await customFetch(`/api/auth/`);

  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
  
    dispatch(setUser(data));
  }
}

export const login = (email, password) => async (dispatch) => {
  const response = await customFetch(`/api/auth/login`, {
    method: 'POST',
    body: JSON.stringify({
      email,
      password
    })
  });
  
  
  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data))
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ['An error occurred. Please try again.']
  }

}

export const logout = () => async (dispatch) => {
  const response = await customFetch(`/api/auth/logout`);

  if (response.ok) {
    dispatch(removeUser());
  }
};


export const signUp = (channelName, email, password) => async (dispatch) => {
  const response = await customFetch(`/api/auth/signup`, {
    method: 'POST',
    body: JSON.stringify({
      channelName,
      email,
      password,
    })
  });
  
  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data))
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ['An error occurred. Please try again.']
  }
}


// REDUCER ************************************************
const initialState = { user: null };
export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { user: action.payload }
    case REMOVE_USER:
      return { user: null }
    default:
      return state;
  }
}
