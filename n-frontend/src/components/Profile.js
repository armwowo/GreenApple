import '../style/Profile.css';
import React,{useEffect, useState} from 'react';

function UserProfile(){
    const[name,setName] = useState('tewatgdafs')
    const[email,setEmail] = useState('atewatfd')
    const[username,setUsername] = useState('teawyg4awt')
    const[phone,setPhone] = useState('fdaea')
    const[reserlist,setReservation  ] = useState([])
    const[formUser,setUser] = useState({})
    const[checkinfo,setStatus] = useState(false)

    let use = "oakoak22"
    const datauser= async()=>{
        const res = await fetch(`http://127.0.0.1:8000/getuserdata?user=${use}`,{
            method:'GET'
        })
        res.json().then(res=>{setUser(res)
            setReservation(res.Reservation)})
        
        setStatus(true)
        
    }
    // const cancle= async()=>{
    //     const res = await fetch(`http://127.0.0.1:8000/getuserdata?user=${use}`,{
    //         method:'GET'
    //     })
    //     res.json().then(res=>{setUser(res)
    //         setReservation(res.Reservation)})
        
    //     setStatus(true)
        
    // }
    
    useEffect(()=>{ 
    
        datauser()
        
    },[])
    
    console.log(formUser.Reservation)
    return(
        <div>
            <h5 className="your-profile">Your Profile</h5>
            <div className="card">
            <div className='user-photo'>

                </div>
                    
                    <ul className='user-info'>
                        <li>Name             :  {formUser.Name}</li>
                        <li>Email            :  {formUser.Email}</li>
                        <li>Username         :  {formUser.Username}</li>
                        <li>Phone            :  {formUser.Phone_number}</li>
                        <div className='reser'>Reservation
                        
                        {reserlist.map((e)=>(
                            <ul>
                               <button className='cancle' type='submit' >cancle</button>
                                <li>check in      :{e.check_in} </li>
                                <li>room id     :{e.room_id} </li>
                                <li>room rental      :{e.room_rental} </li>
                                </ul>
                            
                        ))}</div>
                        {/* <li>Phone            :  {formUser.Reservation.room_id}</li> */}
                    </ul> 
                    {/* <div className='edit-profile'> */}
                    {/* <button type='submit' >Edit Profile</button> */}
                    {/* </div> */}
            </div>
        </div>
    )

}
export default UserProfile
