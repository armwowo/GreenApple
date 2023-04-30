import React from "react";
import "./Home.css"

function Home() {
    const dorms = [
        { id: 1, name: "Dorm A", address: "123/456 Road, Bangkok", price: 3000 },
        { id: 2, name: "Dorm B", address: "789/012 Road, Bangkok", price: 2500 },
        { id: 3, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
      ];
    return (
    <div className="Home_container">
        <h1>หอพัก ในเขตลาดกระบัง</h1>
        <div>
            <ul>
                {dorms.map((dorm) => (
                <li key={dorm.id}>
                    <h3>{dorm.name}</h3>
                    <p>{dorm.address}</p>
                    <p>{dorm.price} baht/month</p>
                </li>
                ))}
            </ul>
        </div>
    </div>
    );
}
export default Home