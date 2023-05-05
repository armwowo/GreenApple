import React, { useEffect, useState } from "react";
import {Link} from "react-router-dom"

import "../style/Detail.css";

function Detail(props) {
    const cat = []
    const id = props.id
    const [dorm,setDorm] = useState([])
    const [faci,setFac] = useState({})
    const checkfaci = []
    const [price,setPrice] = useState([])
    const detailDorm =async()=>{
      const res = await fetch(`http://127.0.0.1:8000/getdatadorm`,{
          method:'GET'
      })
      const temp = await res.json()
      // console.log(temp.dor_list)
      setDorm(temp.dor_list[id])

  }

    useEffect(()=>{
      
    
    if(dorm.length!=0){
      setFac(dorm._Dormitory__Fac)
      
      setPrice([Math.min(...dorm._Dormitory__price),Math.max(...dorm._Dormitory__price)])
      for (var i in faci){
            if(faci[i]==1){
              // console.log("true")
              checkfaci.push("Trueใ")
            }else{
              // console.log("false")
              checkfaci.push("False")}
          
          }
      
    }else{detailDorm()}
     
    console.log(checkfaci)
    },[dorm])

    console.log(faci)
    // useState(()=>{
    //   if(faci.length!=0){
    //     console.log("check")
    //   for (var i in faci){
    //     if(faci[i]==1){
    //       setCheckfaci([...checkfaci,"True"])
    //     }else{setCheckfaci([...checkfaci,"False"])}}}
    //     else{console.log(faci.length)}
    // },[faci])
    // console.log(checkfaci)

  return (

    <div className="Page">
    <div className="Detail_Container">
      <h1>{dorm._Dormitory__dor_name}</h1>
      <p className="Address">{dorm._Dormitory__address}</p>
      <div>
        <table className="Top_table">
          <tr>
            <th> {/*เบอร์โทร */}
                <h4>เบอร์โทรติดต่อ : {dorm._Dormitory__phone}</h4>
            </th>
            <th> {/*ราคา */}
              <h2>ค่าเช่า</h2>
              <h4>ราคา {price[0]} - {price[1]} บาท/เดือน</h4>
            </th>
          </tr>
        </table>
      </div>
      <div className="Dor_photo">
        <table>
          <tr>
            <td>
              <img src={`images/aphouse_pic.jpg`}/>
            </td>
            <td>
              <h2>รายละเอียด</h2>
              <p>{dorm._Dormitory__detail}<br/></p>
              <h5>*** หอพักปลอดของมึนเมาและสารเสพติด ขออนุญาตรับเฉพาะผู้พักที่ไม่ดื่มของมึนเมา ไม่สูบบุหรี่</h5>
              <button>สถานะ :</button>
            </td>
          </tr>
        </table>
      </div>
      <div className="Detail_table">
        <h2>ตารางค่าใช้จ่าย</h2>
        <table>
          <tr>
            <th>รายเดือน</th>
            {/* <th>เงินประกัน</th>
            <th>จ่ายล่วงหน้า</th> */}
            <th>ค่าไฟ</th>
            <th>ค่าน้ำ</th>
          </tr>
          <tr>
            <td>{price[0] }- {price[1]}บาท/เดือน</td>
            {/* <td>1 เดือน</td>
            <td></td> */}
            <td>{dorm._Dormitory__electric} บาท/เดือน</td>
            <td>{dorm._Dormitory__water} บาท/ยูนิต</td>
          </tr>
        </table>
      </div>
      <div className="Facility">
        <h2>สิ่งอำนวยความสะดวก:</h2>

        <table>
          <td>
            <tr className={checkfaci[0]}>
              <img src={`images/${checkfaci[0]}.jpg`}/>สัตว์เลี้ยง</tr>
            <tr className={checkfaci[1]}>
              <img src={`images/${checkfaci[1]}.jpg`}/>EV Charger</tr>
            <tr className={checkfaci[2]}>
              <img src={`images/${checkfaci[2]}.jpg`}/>ร้านเสริมสวย</tr>
              <tr className={checkfaci[3]}>
              <img src={`images/${checkfaci[3]}.jpg`}/>ร้านซักรีด</tr>
            <tr className={checkfaci[4]}>
              <img src={`images/${checkfaci[4]}.jpg`}/>ร้านค้า</tr>
            <tr className={checkfaci[5]}>
              <img src={`images/${checkfaci[5]}.jpg`}/>ร้านอาหาร</tr>
            <tr className={checkfaci[6]}>
              <img src={`images/${checkfaci[6]}.jpg`}/>รปภ</tr>
            
            
          </td>

          <td>
          <tr className={checkfaci[7]}>
              <img src={`images/${checkfaci[7]}.jpg`}/>CCTV</tr> 
          <tr className={checkfaci[8]}>
              <img src={`images/${checkfaci[8]}.jpg`}/>Finger Print</tr>
          <tr className={checkfaci[9]}>
              <img src={`images/${checkfaci[9]}.jpg`}/>คีย์การ์ด</tr>
            <tr className={checkfaci[10]}>
              <img src={`images/${checkfaci[10]}.jpg`}/>ฟิตเนส</tr>
            <tr className={checkfaci[11]}>
              <img src={`images/${checkfaci[11]}.jpg`}/>สระว่ายน้ำ</tr>
            <tr className={checkfaci[12]}>
              <img src={`images/${checkfaci[12]}.jpg`}/>ลิฟต์</tr>
            <tr className={checkfaci[13]}>
              <img src={`images/${checkfaci[13]}.jpg`}/>ลานจอดรถ</tr>
            <tr className={checkfaci[14]}>
              <img src={`images/${checkfaci[14]}.jpg`}/>สูบบุหรี่</tr>
          </td>
        </table>
      </div>
      <Link to={`/Reserve`}>
        <button className="Reserve">จองห้องพัก</button>
      </Link>
    </div>
  </div>
  );
}

export default Detail;