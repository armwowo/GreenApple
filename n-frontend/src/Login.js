import { useState } from "react";
import { Link, Navigate} from "react-router-dom";
import "./Login.css"
import axios from "axios";
import UserProfile from "./components/Profile";


function Login() {
    const [username , setUsername] = useState('')
    const [password , setPassword] = useState('')
    const [isLoggedIn, setIsLoggedIn] = useState(false)
    // const [navi,setNavi] = useState({})
    const [message,setMessage] = useState("")
    

    // const onSubmitlogin=async(e)=>{
    //     e.preventDefault();
    //     await axios.post(`http://127.0.0.1:8000/login?username=${username}&password=${password}`)
    //     .then(response => {
    //         console.log(response)
    //         localStorage.setItem("auth_token", response.data.result.access_token);
    //         localStorage.setItem("auth_token_type", response.data.result.token_type);
    //     }).catch((error)=>{
    //         console.log(error);
    //     })

    // }

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch(`http://127.0.0.1:8000/login?username=${username}&password=${password}`, {
          method: 'POST'
        });
        const data = await response.json();
        console.log(data)
        if (data!="unsuccess") {
            setIsLoggedIn(true)
        } else { 
            setIsLoggedIn(false)
            setMessage("Invalid username or password")  
        }
        // setLoginForm({"username":username , "password":password})
        
    };
    

    return (
        <div className="login-form-container">
            {isLoggedIn ? (
                <Navigate  to={"/"}/>
                // <UserProfile userData = {username}/>

            
            ) : (
                <form className="login-form" onSubmit={handleSubmit}>
                    <h2 className="Top">Login</h2>
                    <label htmlFor="username">Username</label>
                    <input value={username} onChange={(e) => setUsername(e.target.value)}type="text" placeholder="Username" />
                    <label htmlFor="password">Password</label>
                    <input value={password} onChange={(e) => setPassword(e.target.value)}type="password" placeholder="Password" />
                    <button type="submit">Login</button>
                    <div className="message-error">{message}</div>
                </form>
            )}
        </div>
    )
}

export default Login