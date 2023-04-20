import { useState } from "react";
import "./Login.css"


function Login() {
    const [username , setUsername] = useState('')
    const [password , setPassword] = useState('')
    const [isLoggedIn, setIsLoggedIn] = useState(false)

    
    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch(`http://127.0.0.1:8000/login?username=${username}&password=${password}`, {
          method: 'POST'
        });
        const data = await response.json();
        console.log(data);
        if (data.Status.success) {
            setIsLoggedIn(true)
        } else {
            setIsLoggedIn(false)
        }
    };

    return (
        <div className="login-form-container">
            {isLoggedIn ? (
                <h2>Login suc!</h2>
            ) : (
                <form className="login-form" onSubmit={handleSubmit}>
                    <h2 className="Top">Login</h2>
                    <label htmlFor="username">Username</label>
                    <input value={username} onChange={(e) => setUsername(e.target.value)}type="text" placeholder="Username" />
                    <label htmlFor="password">Password</label>
                    <input value={password} onChange={(e) => setPassword(e.target.value)}type="password" placeholder="Password" />
                    <button type="submit">Login</button>
                </form>
            )}
        </div>
    )
}

export default Login