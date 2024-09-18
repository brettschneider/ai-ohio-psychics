import { createContext, useContext, useReducer } from "react";

const initialState = () => {
    return {
        token: null,
        userName: null,
        chatOpen: false,
    }
};

const applicationReducer = (state, action) => {
    switch (action.type) {
        case "LOGIN":
            return { ...state, token: action.token, userName: action.userName }
        case "LOGOUT":
            return { ...state, token: null, userName: null }
        case "OPEN_CHAT":
            return { ...state, chatOpen: true }
        case "CLOSE_CHAT":
            return { ...state, chatOpen: false }
        default:
            return state
    }
}

const StateContext = createContext(null);

export const StateProvider = ({ children }) => {
    const [state, dispatch] = useReducer(applicationReducer, initialState())
    return (
        <StateContext.Provider value={{ state, dispatch }}>
            {children}
        </StateContext.Provider>
    )
}

export const useStateDispatch = () => {
    const context = useContext(StateContext)
    if (!context) {
        throw new Error("useStateDispatch must be used within a StateProvider")
    }
    return context;
}