import React from "react";
import { Link } from "react-router-dom";
import "./ออลสมายล์.css";

function Allsmile() {
  return (
    <div className="Page">
      <div className="Detail_Container">
        <h1>ออลสมายล์ แมนชั่น</h1>
        <p className="Address">ถ.หลวงลาดกระบัง ทับยาว ลาดกระบัง กรุงเทพมหานคร</p>
        <div>
          <table className="Top_table">
            <tr>
              <th> {/*เบอร์โทร */}
                  <h4>เบอร์โทรติดต่อ : 0955358037</h4>
                  <h4>หรือเบอร์ : 027380911</h4>
              </th>
              <th> {/*ราคา */}
                <h2>ค่าเช่า</h2>
                <h4>ราคา 5,500 บาท/เดือน</h4>
                <h4>ราคา 599 บาท/วัน</h4>
              </th>
            </tr>
          </table>
        </div>
        <div className="Dor_photo">
          <table>
            <tr>
              <td>
                <img src={`images/allsmile_pic.jpg`}/>
              </td>
              <td>
                <h2>รายละเอียด</h2>
                <p>ใกล้สนามบิน สุวรรณภูมิ สำนักงานเขต เทคโนลาดกระบัง มหาวิทาลัยกรุงเทพสุวรรณภูมิ <br/>
                    เทสโก้โลตัส บีควิก และ อื่นๆอีกมากมาย พร้อมเฟอร์นิเจอร์ เเอร์ อินเตอร์เนท พร้อมที่จอดรถภายในพื้นที่ และมีร้านค้าต่างๆ อยู่ในพื้นที่
                    ตึกใหม่พร้อมเปิดรับผู้เช่าแล้ววันนี้ติดต่อเพื่อขอรายละเอียดเพิ่มเติมได้แล้ววันนี้ พร้อมโปรโมชั่นพิเศษสำหรับผู้เช่าที่ทำสัญญาภายในเดือนกันยายน พ.ศ. 2565 นี้!<br/>
                    Line ID : @357cgyob<br/>
                    Facebook page :</p>
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
              <th>รายวัน</th>
              <th>เงินประกัน</th>
              <th>จ่ายล่วงหน้า</th>
              <th>ค่าไฟ</th>
              <th>ค่าน้ำ</th>
            </tr>
            <tr>
              <td>5,500 บาท/เดือน</td>
              <td>599 บาท/วัน</td>
              <td>1 เดือน</td>
              <td>-</td>
              <td>8 บาท/ยูนิต</td>
              <td>19 บาท/ยูนิต</td>
            </tr>
          </table>
        </div>
        <div className="Facility">
          <h2>สิ่งอำนวยความสะดวก:</h2>
          <table>
            <td>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>เครื่องปรับอากาศ</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>เฟอร์นิเจอร์-ตู้ เตียง</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>เครื่องทำน้ำอุ่น</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>พัดลม</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>มี TV ให้</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ตู้เย็น</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>โทรศัพท์สายตรง</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>อนุญาตให้เลี้ยงสัตว์</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>อนุญาตให้สูบบุหรี่ในหอพัก</tr>
            </td>
            <td>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ที่จอดรถ</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ที่จอดรถมอเตอร์ไซต์ / จักรยาน</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ลิฟต์</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>สระว่ายน้ำ</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>โรงยิม/ฟิตเนส</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>อินเตอร์เน็ตไร้สาย (WIFI) ในห้อง</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>เคเบิลทีวี / ดาวเทียม</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>มีระบบรักษาความปลอดภัย (keycard)</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>มีระบบรักษาความปลอดภัย (สแกนลายนิ้วมือ)</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>กล้องวงจรปิด (CCTV)</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>รปภ.</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ร้านขายอาหาร</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ร้านค่า ร้านสะดวกซื้อ</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ร้านซัก-รีด / มีบริการเครื่องซักผ้า</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ร้านทำผม-เสริมสวย</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>สถานี charge รถไฟฟ้า</tr>
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

export default Allsmile;