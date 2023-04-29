import { useState } from "react";
import "./Register.css"

function Register() {
    const [name , setName] = useState("")
    const [lastname , setLastname] = useState("")
    const [email , setEmail] = useState("")
    const [username , setUsername] = useState("")
    const [password , setPassword] = useState("")
    const [user_phone , setUser_phone] = useState("")
    const [role , setRole] = useState("")

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch(`http://127.0.0.1:8000/register?username=${username}&password=${password}`, {
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
        <div className="register-form-container">
            <form className="register-form" onSubmit={handleSubmit}>
                <h2 className="Top">Register</h2>
                <label htmlFor="lastname">Your Role</label>
                <input value={role} onChange={(e) => setRole(e.target.value)}type="role" placeholder="Owner or User" />
                <label htmlFor="name">Name</label>
                <input value={name} onChange={(e) => setName(e.target.value)}type="name" placeholder="Name" />
                <label htmlFor="lastname">Lastname</label>
                <input value={lastname} onChange={(e) => setLastname(e.target.value)}type="lastname" placeholder="Lastname" />
                <label htmlFor="email">Email</label>
                <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="Email" />
                <label htmlFor="username">Username</label>
                <input value={username} onChange={(e) => setUsername(e.target.value)}type="username" placeholder="Username" />
                <label htmlFor="password">Password</label>
                <input value={password} onChange={(e) => setPassword(e.target.value)}type="password" placeholder="Password" />
                <label htmlFor="user_phone">Phone Number</label>
                <input value={user_phone} onChange={(e) => setUser_phone(e.target.value)}type="user_phone" placeholder="Phone Number" />
                <button>Submit</button>
            </form>
        </div>
    )
}
export default Register