import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./Home.css"
import Sliderp from "./components/Sliderp";


function Home() {
    const [data,getdata ]=useState([]);
    const [filed,getfile] = useState(false);
    const [value,getvalue ]=useState({});
    const [errors,setEarror] = useState(false);
    const [price,setPrice] = useState([0,10000])
    const [filterList,setlistfiler] = useState([]);
    const Mockdata= async()=>{
        const res = await fetch('http://127.0.0.1:8000/firstpagedata')
        res.json().then(res=>getdata(res))
        .catch(err =>setEarror(err) )
    }
    const filterPrice = async()=>{
        const res = await fetch(`http://127.0.0.1:8000/searchByPrice/?minimum=${price[0]}&maximum=${price[1]}`)
        res.json().then(res=>setlistfiler(res))
        .catch(err =>setEarror(err) )
        
    }
    useEffect(()=>{
        Mockdata();
    },[])
    useEffect(()=>{
        filterPrice();
    },[price])
    console.log(filterList) 
    
    //const output = console.log(data.map(value => value._Dormitory__dor_name))

    return (
        <div className="Home_container">
        <h1>หอพัก ในเขตลาดกระบัง</h1>
        <div className="flex">
            <div className="list_dor">
                <ul>
                    {filterList && filterList.map((dorm) => (
                    
                    <li key={dorm.id}>
                        <Link to={`/Detail/${dorm.id}`}>
                                <h3>{dorm.name}</h3>
                                <img src={`images/${dorm.name.toLowerCase()}.jpg`} alt={dorm.name} />
                            <p>{dorm.address}</p>
                            <p>{dorm.price} บาท/เดือน</p>
                            </Link>
                        </li>
                    
                    ))}
                </ul>
            </div>
            <div className="height">
                <Sliderp price={setPrice}/>
            </div>
        </div>
    </div>
    );
}
export default Home