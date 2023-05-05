import React, { useEffect, useState } from "react";
import "../style/Detail.css";

function Detail(props) {
    
    const cat = []
    const [dorm,setDorm] = useState([])
    const detailDorm =async()=>{
      const res = await fetch(`http://127.0.0.1:8000/getdatadorm`,{
          method:'GET'
      })
      const temp = await res.json()
      // console.log(temp.dor_list)
      setDorm(temp.dor_list)

  }

    useEffect(()=>{
      
    detailDorm()
    },[])
    // console.log(dorm)
    const test = dorm.map((element)=>{
      console.log(element)
    })

  return (
    <div className="Page">
      <div className="Detail_Container">
        {/* {dorm.map(()=>)} */}

          <h1>สบายเพลส</h1>
          <p className="Address">ถ.ฉลองกรุง ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร</p>
          <div>
            <table className="Top_table">
              <tr>
                <th> {/*เบอร์โทร */}
                    <h4>เบอร์โทรติดต่อ : 0993429897</h4>
                </th>
                <th> {/*ราคา */}
                  <h2>ค่าเช่า</h2>
                  <h4>ราคา 3,000 บาท/เดือน</h4>
                  <h4>ราคา 600 บาท/วัน</h4>
                </th>
              </tr>
            </table>
          </div>
          <div className="Dor_photo">
            <table>
              <tr>
                <td>
                  {/* <img src={`images/sabaiplace_pic.jpg`}/> */}
                </td>
                <td>
                  <h2>รายละเอียด</h2>
                  <p>ห้องเช่า สบายเพลส เป็น ห้องพักตั้งอยู่ที่ ซอย ฉลองกรุง 31/1 หน้านิคมอุตสาหกรรมลาดกระบัง ใกล้พระจอมเกล้าลาดกระบัง และ สนามบิน สุวรรณภูมิ เป็นที่พักในอุดมคติสำหรับ
                    คนทำงานที่ นิคมลาดกระบัง นักเรียน นักศึกษา เทคโน พระจอมเกล้าลาดกระบัง คนทำงานที่สนามบิน สุวรรณภูมิ</p>
                </td>
              </tr>
            </table>
          </div>
          <div className="Detail_table">
            <h2>ตารางค่าใช้จ่าย</h2>
            <table>
              <tr>
                <th>รายเดือน</th>
                <th>รายวัน</th>
                <th>เงินประกัน</th>
                <th>จ่ายล่วงหน้า</th>
                <th>ค่าไฟ</th>
                <th>ค่าน้ำ</th>
              </tr>
              <tr>
                <td>4500 บาท/เดือน</td>
                <td>600 บาท/วัน</td>
                <td>1 เดือน</td>
                <td>1 เดือน</td>
                <td>8 บาท/ยูนิต</td>
                <td>15 บาท/ยูนิต<br/> ขั้นต่ำ 100 บาท/เดือน</td>
              </tr>
            </table>
          </div>
          <div className="Facility">
            <h2>สิ่งอำนวยความสะดวก:</h2>
            <table>
              <td>
                <tr>fg</tr>
                <tr>dg</tr>
              </td>
              <td>
                <tr>fg</tr>
                <tr>dg</tr>
              </td>
            </table>
          </div>
      </div>
    </div>
  );
}

export default Detail;