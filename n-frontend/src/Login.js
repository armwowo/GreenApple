import React, { useState } from "react";
import "./Login.css"

function Login() {
    const [username , setUsername] = useState("")
    const [password , setPassword] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(username);
    }
    return (
        <div className="login-form-container">
            <form className="login-form" onSubmit={handleSubmit}>
                <label className="Top">Login</label>
                <label htmlFor="username">Username</label>
                <input value={username} onChange={(e) => setUsername(e.target.value)}type="username" placeholder="Username" />
                <label htmlFor="password">Password</label>
                <input value={password} onChange={(e) => setPassword(e.target.value)}type="password" placeholder="Password" />
                <button>Login</button>
            </form>
        </div>
    )
}

export default Login