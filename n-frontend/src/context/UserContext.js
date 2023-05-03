import React, {createContext} from "react";

export const UserContext = createContext();

export const UserProvider = (props) =>{
    const  [token,setToken] = useState(localStorage.getItem("aweomeLeadsToken"));
    
    useEffect(() =>{

    })
}