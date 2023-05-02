import React from "react";
import { Link } from "react-router-dom";
import "./Home.css"

function Home() {
    const dorms = [
        { id: 1, name: "สบายเพลส", address: "ถ.ฉลองกรุง ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร", price: 4500 },
        { id: 2, name: "APPLEHOUSE", address: "ซ.ฉลองกรุง1 แยก5 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร", price: 4800 },
        { id: 3, name: "อัจฉริยา", address: "ซ.เกกีงาม1 ถ.ฉลองกรุง1 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร", price: 5000 },
        { id: 4, name: "บ้านคุ้มเกล้า48", address: "ซ.48 ถ.คุ้มเกล้า ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร", price: 5000 },
        { id: 5, name: "BBCourt", address: "ซ.ฉลองกรุง 1 ถ.ฉลองกรุง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร", price: 4700 },
        { id: 6, name: "APHouse", address: "ซ.เกกีงาม 1 ถ.ฉลองกรุง 1 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร", price: 5300 },
        { id: 7, name: "บุรีไอริส", address: "ซ.ฉลองกรุง 1 แยก5 ถ.ฉลองกรุง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร", price: 6000 },
        { id: 8, name: "ออลสมายล์", address: "ถ.หลวงลาดกระบัง ทับยาว ลาดกระบัง กรุงเทพมหานคร", price: 5500 },
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