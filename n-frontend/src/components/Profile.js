import '../style/Profile.css';
import React,{useEffect, useState} from 'react';

function UserProfile(){

    const[name,setName] = useState('tewatgdafs')
    const[email,setEmail] = useState('atewatfd')
    const[username,setUsername] = useState('teawyg4awt')
    const[phone,setPhone] = useState('fdaea')
    const[reserlist,setReservation  ] = useState('fgyhwyrtaey5r')


    return(
        <div>
            <h5 className="your-profile">Your Profile</h5>
            <div className="card">
            <div className='user-photo'>

                </div>
                    <ul className='user-info'>
                        <li>Name             :  {name}</li>
                        <li>Email            :  {email}</li>
                        <li>Username         :  {username}</li>
                        <li>Phone            :  {phone}</li>
                        <li>Reservation list :  {reserlist}</li>
                    </ul> 
                    <div className='edit-profile'>
                    <button type='submit' >Edit Profile</button>
                    </div>
            </div>
        </div>
    )

}
export default UserProfile