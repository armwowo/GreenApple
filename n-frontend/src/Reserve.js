import React from "react";
import { useState } from "react";
import { Link } from "react-router-dom";
import Login from "./Login";
import "./Reserve.css"

function Reserve() {
    const [id , setId] = useState('')
    const [username, setUsername] = useState('');
    const [email , setEmail] = useState('')
    const [dormitory , setDormitory] = useState('')
    const [room_id , setRoom_id] = useState('')
    const [room_rental, setRoom_rental] = useState('')
    const [check_in  , setCheck_in ] = useState('')

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(id);
    }
    return (
        <div className="reserve_form_container">
            <form className="reserve-form" onSubmit={handleSubmit}>
                <h2 className="Top">Reservation Form</h2>

                <label htmlFor="id">Reservation ID</label>
                <input value={id} onChange={(e) => setId(e.target.value)}type="text" placeholder="Reservation ID" />
                
                <label htmlFor="email">Email</label>
                <input value={email} onChange={(e) => setEmail(e.target.value)}type="text" placeholder="Email" />
                
                <label htmlFor="dormitory">Dormitory name</label>
                <input value={dormitory} onChange={(e) => setDormitory(e.target.value)}type="text" placeholder="Dormitory name" />
                
                <label htmlFor="room_id">Room ID</label>
                <input value={room_id} onChange={(e) => setRoom_id(e.target.value)}type="text" placeholder="Room ID" />
                
                <label htmlFor="room_rental">Rental</label>
                <input value={room_rental} onChange={(e) => setRoom_rental(e.target.value)}type="text" placeholder="Room Rental" />
                
                <label htmlFor="check_in">Date CheckIn</label>
                <input value={check_in} onChange={(e) => setCheck_in(e.target.value)}type="text" placeholder="Date CheckIn" />
            </form>
        </div>
    );
}
export default Reserve