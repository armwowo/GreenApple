import React from "react";
import { Link } from "react-router-dom";
import "./Home.css"

function Home() {
    const dorms = [
        { id: 1, name: "สบายเพลส", address: "ถ.ฉลองกรุง ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร", price: 4500 },
        { id: 2, name: "Dorm B", address: "789/012 Road, Bangkok", price: 2500 },
        { id: 3, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
        { id: 4, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
        { id: 5, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
        { id: 6, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
        { id: 7, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
        { id: 8, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
        { id: 9, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
        { id: 10, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
    ];
    return (
        <div className="Home_container">
        <h1>หอพัก ในเขตลาดกระบัง</h1>
        <div>
            <ul>
                {dorms.map((dorm) => (
                <Link to={`/${dorm.name}`}>
                    <li key={dorm.id}>
                            <h3>{dorm.name}</h3>
                            <img src={`images/${dorm.name.toLowerCase()}.jpg`} alt={dorm.name} />
                        <p>{dorm.address}</p>
                        <p>{dorm.price} บาท/เดือน</p>
                    </li>
                </Link>
                ))}
            </ul>
        </div>
    </div>
    );
}
export default Home